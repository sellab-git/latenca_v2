# Latenca — Challenging the product model (design decision doc)

## Context for you (the reader)
Latenca is a product for choosing art for your walls. We already built a strong Home page and a complete **AI Design Journey** — an 8-step guided flow (room → wall photo → visual taste calibration → AI analysis → style profile → one explained recommendation shown on a wall → guided customize → final wall), with a rising "confidence" meter and a first-person "designer" voice. Reviewers agreed it's very good UX.

**But that's the problem.** It's the best possible *questionnaire*. Any AI startup could build it. We want to stop iterating mockups and question the product model itself — to find the thing that doesn't exist yet, the way Figma changed design, Cursor changed coding, Perplexity changed search, and Midjourney changed image generation.

This is not a visual task. Not v2. Not a better questionnaire. We want a new category. This document lists the flawed assumptions and proposes 5 fundamentally different experience models. **We have not built new screens** — we design those only after choosing a model.

## The lever those four products share
None of them won with a better onboarding. They all made the same move:
1. **They showed the result FIRST** (answer, code, image, design) before the user specified anything.
2. **They replaced specification with reaction** — the user doesn't *describe* what they want; they *react* to a concrete artifact (accept/reject, variant, remix).
3. **Intent is DISCOVERED in a loop**, not extracted by an upfront form.
4. **The AI has agency** — it proposes, it doesn't just execute.

Our current flow does the opposite: 8 steps of questions, then the effect. That's why it feels like a form.

**The reframe in one sentence:** Latenca should stop being a system that **ASKS** what you want and become one that **SHOWS** you art on your wall and learns from what you **reach for**. Taste is recognized, not described.

## Part 1 — Flawed assumptions in the current flow
1. *"We must ask in order to understand."* One photo of the wall already contains style, palette, light, furniture, scale, and existing art. Asking about things the AI could *see* signals it isn't actually smart.
2. *"The user must describe their taste before seeing anything."* People can't name their style but recognize it instantly. Input-before-output is the core "form" trap.
3. *"Style must be named (Japandi)."* A label is a proxy that can be wrong and alienating ("that's not me"). We force our taxonomy on the user. Style should be shown and tuned visually, never named.
4. *"94% match" — a single correct answer exists.* Taste is a preference space, not a classification problem with one ground truth. A percentage feels patronizing and implies false certainty.
5. *"The effect (art on the wall) belongs at step 6."* The wow moment is deferred ~2 minutes. It should be at second 5. Wow first, refine later.
6. *"The flow is linear (1→8)."* Real design is non-linear — you jump between what / where / how big. A wizard fights how taste actually forms.
7. *"The wall photo is an optional step."* If the photo unlocks everything (inference + preview), it isn't a step — it's the front door that delivers instant magic.
8. *"One best recommendation is the goal" ("curated, not crowded").* One answer is a *verdict* you accept or reject. But you understand taste through *contrast*. Midjourney shows 4, not 1. "One best" is form-thinking (extract enough to compute the single right answer).
9. *"Decisions are made by answering."* Alternative: by **manipulation/reaction** (drag, swap, "more like this", veto, pin). Direct manipulation beats answering questions.
10. *"The AI should minimize mistakes."* A model that sometimes shows a deliberately *divergent* option learns your boundaries faster (active learning). A safe guess teaches slower than "here are two extremes."
11. *"The recommendation comes at the end of understanding."* It should be the **first move**; the process is *correcting* it.
12. *"The AI is a neutral extractor that asks then obeys."* A great designer has a *point of view* — proposes, defends, sometimes disagrees ("trust me"). Ours is servile. A category product has taste and agency.
13. *"The AI leads, the user follows."* Maybe the reverse: the user explores and plays, the AI curates in the background (Perplexity does the work, but you drive). Agency builds confidence.
14. *"Confidence is a number the AI reports."* Confidence should be something the user *feels* seeing the piece on their wall — not a percentage the AI announces.
15. *"The output is one product (a framed print) at the end."* The real job is "a wall that feels right" — sometimes one piece, a pair, a gallery wall, evolving over time. The unit is a **wall composition**, not "a poster."
16. *"It's a session with an end (purchase)."* Walls are lived with; taste and seasons change. Maybe it's a persistent, learning relationship with your space, not a one-shot funnel.
17. *"The experience is single-player."* Wall decisions at home are often shared (partner, family). The model could be collaborative/async (Figma's insight).
18. *"The value is the recommendation."* Maybe the value is the **seeing** — the power to see any art on *your* wall, in your light, at true scale. If that's magical enough, the user becomes their own confident designer.
19. *"It must feel like AI."* The best tools make the AI invisible — you feel like a brilliant designer, not an "AI user."

## Part 2 — Five fundamentally different models
Each has a different *core mechanic*, not cosmetics. They aren't mutually exclusive — the winner probably fuses them — but they're worth separating as hypotheses.

**A — "The living wall" (your wall is the canvas, not a form).** You enter *inside a view of your wall* (photo or template room). The AI makes the first move — art appears on it, at scale, in your light. From then on there are **no questions and no steps**. You live in the wall view and *manipulate*: swipe to swap the piece (a curated deck that converges), pinch to resize, drag to reposition, tap "more like this / not this." The AI learns from swaps and dwell-time — never asks. The wall is a persistent document you return to. *Category shift:* from "answer questions to get a recommendation" to "play on your real wall; the AI curates the deck you flip through." *5 years later:* "Latenca made choosing art feel like *arranging*, like moving furniture — not shopping."

**B — "Two directions" (diverge → converge; taste through contrast).** The AI never asks; it *proposes*. It opens with two deliberately different complete arrangements on your wall (e.g. "quiet & warm" vs "bold & graphic") — unlabeled, just shown. You pick the one that pulls you (or "somewhere between", or "neither, go weirder"). Each choice spawns two divergent children. In 3–4 forks you converge on a wall you love, having only made gut this-or-that reactions to *your room*. The controlled error is built in: one of the two is always a stretch, to map your boundaries fast. *Category shift:* taste emerges from a branching tournament of full visualizations, not from describing attributes. *5 years later:* "Latenca didn't ask your taste. It showed two walls and watched which you reached for — and after five picks it knew better than you did."

**C — "A partner with a point of view" (a peer, not a wizard).** The AI becomes an opinionated co-designer with taste. It makes a bold first move and *defends it* ("I went large and calm — your room has a lot going on, so the wall should breathe"). You push back naturally ("too safe", "warmer", "I have a green couch you can't see"). It argues, adjusts, sometimes gently disagrees ("I'd resist smaller — here's why, but your call"). A dialogue of proposals and reactions, not Q→A. The product is the *relationship*. *Category shift:* from extraction to genuine collaboration; the AI has agency and taste (Cursor for interiors). *5 years later:* "Latenca gave everyone an interior designer with a personality — one who argues with you, not just takes orders."

**D — "Wow-first" (result before input; magic then refine).** Zero questions to start. You give ONE thing — a photo of your wall (or pick a room like yours) — and *immediately* see a finished, beautiful designed wall in your space. Full stop. That's the entire first screen: transformation. Only after the wow do refinements appear, and only as reactions to what's on screen ("love it / warmer / different vibe") — each optional. Many buy from the first or second view. *Category shift:* time-to-magic collapses to ~5 seconds; photo inference replaces the questionnaire entirely; refinement is optional polish, not a required funnel (Perplexity: answer-first). *5 years later:* "Latenca showed you your new wall before you asked anything. Everyone else was still running quizzes."

**E — "Ambient" (a living, evolving space you own).** Not a session with an end. Latenca becomes a persistent model of your space and taste. Your wall is a *place you own* in the app; it proposes ideas over time (seasonal, new artists, "this pairs with what you have"), you react occasionally, it learns continuously, and buying is just "yes, make that real" when a proposal lands. *Category shift:* from transaction/funnel to an ongoing relationship and living space; the taste model compounds ("Discover Weekly" for your walls). *5 years later:* "Latenca didn't sell you a print. It became your home's designer for years."

## Part 3 — My recommendation
**The one core bet everything rests on:** *inference from a wall photo* + *learning from reactions, not questions*. That's the common denominator of A, B, and D — and it's the thing "that doesn't exist yet."

Recommended fusion for a v1 of the new category:
- **Entry = Model D** (photo → instant "wow" on your wall; zero questions).
- **Exploration = Model B** (if the first shot isn't perfect: two divergent directions, not a return to a form).
- **Control = Model A** (you live in the wall view; swap/scale/position by direct manipulation).
- **Voice = Model C** (the AI has a light point of view and explains *why* — but invisibly, not as a chatbot).
- **Model E** is phase 2 (retention/LTV), not the start.

What I would NOT carry over: naming the style, the "match %", linear 8 steps, asking about things visible in the photo, "one best" as the only path.

## Cheapest test before building any screens
1. Take 5 real wall photos (friends / apartments online).
2. By hand, for each, create: (a) one "wow" shot [tests Model D] and (b) two divergent directions [tests Model B].
3. Show 5 people: does the "wow" land with zero questions? Do "two directions" hit their taste faster than our current 8-step flow?
This decides whether photo-inference is good enough to bet on — before we build screens.

## Questions I'd love your view on
1. Is "photo inference + learn from reactions" actually the right core bet, or is there a stronger primitive?
2. Which of the 5 models (or fusion) has the best odds of being category-defining vs. merely nice?
3. What's the biggest risk in the Wow-first entry — and how would you de-risk a bad first shot without adding questions back?
4. Is the "confidence %" worth keeping in any form, or does it always read as gimmick?
5. Is there a sixth model we're not seeing — a mechanic none of the four exemplars used?
