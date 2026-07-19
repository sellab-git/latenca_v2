# Latenca — the product (single-session blueprint)

**The one goal, everything serves it:** *one 10-minute session with a stranger → maximize the probability they confidently buy a wall they absolutely love.*

**The spine:** Photo → the AI shows a bold, complete wall on *their* room → they react → it escalates to a better, bolder wall → until one is inevitable → "make it real" → buy. Zero questions. Zero labels. Zero explanation. The AI leads with conviction; the user only reacts; the wall is the hero; the AI disappears.

---

## Minute by minute

### 0:00–0:15 — Enter. Take the photo. (No questions.)
**User sees:** one line — *"Let's design your wall. Show it to me."* — and the camera. Take or upload a photo of the actual wall. (Fallback if they won't: *"No photo? Pick the room closest to yours"* → a few realistic room archetypes. Weaker, because we lose *their* wall as the closer, so we push the photo hard — but never block them.)
**AI does:** nothing yet. This is the only input the product ever demands.

### 0:15–0:35 — The reveal (the whole game lives here).
**User sees:** their room, now with a **complete, bold, grounded wall on it** — at true scale, correct perspective, matched to their light, respecting the furniture. One confident line: *"Here's what I'd do."* No spinner theatre, no "analyzing you." Just: *whoa.*
**AI does (in that ~15s):** parses the photo into a **room brief** — segments the wall, estimates real dimensions and scale (furniture/known objects or phone depth as the ruler), reads palette, light direction and temperature, room type, focal point, what's already there, architectural features (windows, mouldings, sofa line). From the room it seeds a **prior** over what belongs here, generates the top-K complete compositions (one statement piece / a pair / a gallery wall / mirror + art / shelf / deliberately sparse), scores them by *fit × boldness*, and renders the highest-expected-value **bold-but-grounded** one onto the photo. The first move is calibrated to be *bold yet plausible* — so even if it's not "the one," it reads as a real designer's opinion, not a random guess.

### 0:35–~4:30 — The design conversation (the crescendo).
**User sees:** one bold wall at a time, full-bleed on their room. Two reactions, always:
- **"More like this"** (a tap) — I like where this is going.
- **"Not this"** (a swipe away) — go a different way.
Occasionally, only at a genuine fork, a single **"Which of these two?"** — the one time contrast appears.
No prices. No style names. No percentages. No "here's how I understood you." Each reaction is answered by the **next, better, bolder wall.** The walls visibly get righter.
**AI does:** after every reaction it updates its internal read and chooses the next opinion (mechanics below). Each proposal does double duty — it's the most beautiful wall it can offer *and* the one whose reaction will teach it the most. It never shows something worse to learn; beauty first, learning as the tie-breaker. It's climbing toward a peak, not averaging toward safe.

### ~4:30–5:00 — The inevitable.
**User sees:** a wall that makes them stop — *"oh, that's it."* The AI senses convergence and, instead of continuing, presents that wall **large and calm**, held. The emotion is *"I'd never have thought of that — and now I can't imagine the room without it."*
**AI does:** detects convergence (its top candidate is stable and strongly liked), stops proposing, resolves the physical implementation silently (which prints, size, frame, finish — all already visible in the design), and prepares the close.

### 5:00–5:45 — See it real (delight → confidence).
**User sees:** the winning wall rendered convincingly in *their* room — true scale, their light, maybe a quiet day→evening toggle so they trust it at any hour. This is *seeing is believing*: their own eyes remove the last doubt. No AI claim needed.
**AI does:** high-fidelity final render(s); confirms scale/fit; nothing shown about the machinery.

### 5:45–8:30 — Commerce emerges (as "make it real").
**User sees:** for the first time, a price — **once, bundled, simple.** *"Your wall — [1 large piece + oak frame], everything included, $X, arrives in ~5 days."* Frame, size, material, hanging kit already decided *as part of the design* — not a configurator. One screen: confirm + pay. Reassurance in one line: *free returns, signed certificate.*
**AI does:** turns the design into a real order (SKUs, print spec, framing, fulfilment). Commerce is the **implementation of the design**, never a separate shopping act.

### 8:30–10:00 — Buy + reassure.
**User sees:** pay (Apple/Google Pay one-tap). *"It's being made for you."* Zero-risk close. Done.

---

## The engine — how the AI decides its next opinion (the core mechanic)
It holds an internal read of the user's taste as a region in a latent design space, **seeded by the room** (the room already implies most of it). Loop:
1. Generate candidate complete walls (top-K by expected appeal given the current read + the room).
2. **Show = argmax(appeal), tie-broken by information-gain.** Beauty is the constraint; learning is the tie-breaker. Consecutive proposals deliberately differ along *one* meaningful dimension (density, scale, boldness, warmth, symmetry) so the reaction quietly reveals that dimension's value — active learning wearing a designer's conviction.
3. Update on reaction:
   - **"More like this"** → concentrate around that region; next move = a **bolder push in that direction** (crescendo) + resolve the next-biggest uncertainty.
   - **"Not this"** → down-weight it; if it was an early or confident bet, make a **big jump** to a different region. (The first rejection is the most informative event in the whole session — it triggers the largest exploratory leap, never a small nudge.)
4. Track convergence (is the top candidate stable and strongly liked?). When yes → stop and land.

## The 10 answers, directly
1. **Full journey:** open → photo → bold reveal → react/escalate (a few cycles) → inevitable wall → see it real → one bundled price → pay. ~10 min, most of it the design conversation, purchase is a fast tail.
2. **What the AI does internally per stage:** idle → (on photo) room brief + taste prior + generate/score/render first bold wall → (per reaction) posterior update + next opinion by beauty-then-info-gain → (on convergence) resolve physical spec + final render → order.
3. **What the user sees per stage:** camera → their room redesigned → one bold wall at a time + two reactions → the inevitable wall held large → it real in their room → one price → confirmation. Never: analysis, labels, percentages, explanations, prices until the end.
4. **How it picks the next opinion:** beauty-first, information-gain as tie-breaker; "more"→bolder same direction, "not this"→jump; each proposal probes one dimension.
5. **When the first opinion is wrong:** it costs one tap. "Not this" triggers the *biggest* jump (a genuinely different direction, not a variation), no apology, no "let me understand you" — just *"Okay — then this."* The first move is grounded enough that "wrong" means "redirect," not "bounce."
6. **How many cycles:** first wall <30s; a "that's the one" candidate typically within **3–5 reactions**; hard-land by **~7**. Allow buying from move 1. If it hasn't landed by ~7, force a final **"these two — which is more you?"** to close, rather than proposing forever (endless proposing destroys the "it got me" feeling).
7. **How commerce emerges:** invisibly, only at the end, as *making the chosen design real* — one bundled price, physical options already decided as design decisions, one-screen checkout. Never a shopping mode.
8. **How we know it's time to buy:** convergence signals — an explicit "love it," or rejections stop and only tiny tweaks remain, or the user keeps returning to one wall. The AI *offers* the close at that peak (gently, still skippable). It also closes on fatigue signals (rapid rejections, no love) via the forced two-way contrast.
9. **What info the AI actually needs:** the **photo** (≈80% — room type, scale, palette, light, style, existing objects, architecture) + the **reactions** during the session (the last 20% — the personal delta). Nothing else. No name, no budget upfront, no style label, no questionnaire.
10. **What stays invisible:** the taste model, the active-learning/uncertainty, dimension-probing, style taxonomies (Japandi et al. never shown), any confidence %, the step count, the physical-config logic, and **price until the very end.** The user sees only their room, bold walls, and two reactions.

## The failure modes (and how the design refuses them)
- **Photo friction / no photo** → one-tap capture; realistic room fallback so no one is blocked; but the photo is heavily incentivised because it powers both the wow and the close.
- **Bad first move → bounce** → first move is *bold but room-grounded and lowest-risk-bold*; a rejection is a mild redirect and triggers a big informative jump.
- **Never landing / fatigue** → cap ~7, detect convergence, and force a final two-way contrast; never propose endlessly.
- **Delight without purchase** → "see it real in your room" + one bundled price + zero-risk returns converts *want* into *bought*; price appears once, late, simple.
- **Regret risk** → inevitability + seeing-on-their-wall + easy returns.

## The one capability everything rests on
None of this matters if the render isn't **real**: art placed at true scale, correct perspective, occluded by furniture, matched to the room's light — and the *design opinion* itself has to be **surprising-yet-inevitable**, not a safe average. That is the hard core. The interaction is solved; the bet is now: *can the model author a bold, grounded, correct wall on a stranger's real room, and get righter from two-button reactions, inside ten minutes?*

## The thinnest thing to build first (to test the one goal, not the tech)
Don't build the app. Build the **Wizard-of-Oz**: a human designer behind the curtain playing the AI.
1. Take real wall photos from 5 strangers.
2. A designer pre-renders a bold first wall on each (Photoshop / an image model), then, live, responds to "more/not this" with the next pre-prepared bold wall.
3. Measure the only two things that matter: **did they say some version of "I'd never have thought of that — but yes, that's it"**, and **would they actually pay right now?**
If strangers hit *loved-and-would-buy* in one sitting with a human faking the AI, the product is proven and the remaining work is automating the designer. If they don't, no amount of UI saves it — and we learn that for the price of an afternoon.
