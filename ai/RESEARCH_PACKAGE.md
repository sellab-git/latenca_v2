# Latenca — Design Intelligence Pilot (executable research package)

Three connected studies answering three different questions. Runnable as-is; no further product theory required. **Core correction built in: experts judge *design quality only*; homeowners test *purchase intent*; experts never predict customer behaviour.**

- **Study A** — can the framework identify design quality?
- **Study B** — does that quality create desire + purchase confidence (bold vs safe)?
- **Study C** — can Latenca reach a confidently purchasable wall in one 10–15 min session?

**Sequence:** A first (produces expert-labelled proposals) → B reuses A's proposals with homeowners → C runs in parallel/after on participants' own rooms.
**Decision gates:** A fails → intelligence premise shaky (fix rubric/reconsider). A passes, B fails → "bold" doesn't sell; pivot toward safe-but-personal. A+B pass, C fails → single-session timeline/interaction needs rework. All three pass → green-light to build.
**Do not update the Product Bible yet.** This package is standalone.

---

## 0. Shared Materials Kit (used across A & B)
- **Rooms:** 6 real, homeowner-typical room photos (not staged magazine rooms), each a different problem group from the Thesis Library — e.g. R1 blank-oversized wall · R2 off-centre window imbalance · R3 busy-needs-calm · R4 ignored fireplace · R5 dark/small · R6 generic-no-identity.
- **Catalogue:** one fixed set of ~40–60 real, buyable pieces (with sizes + frame options), so every proposal is realisable and comparable. Design-vs-sell: Study A may include *designable-not-sellable* moves (mirror/shelf/moulding/empty) **tagged**; Studies B & C use **sellable only** (purchase must be real).
- **Proposal card (standard format):** room photo with the design rendered on it (consistent mock-up quality so render polish never confounds) + physical spec (pieces, sizes, frames) + a **hidden metadata sheet** (proposer id, intended class, one-sentence thesis, diagnosed problem, sellable/flag).
- **Render-quality control:** all cards produced to the same visual standard by one operator, so reviewers judge *design*, not production gloss.

---

# STUDY A — Expert Design Evaluation
**Purpose:** does the framework reliably distinguish *invalid / competent-generic / interesting-unresolved / bold-resolved / exceptional*?

### Materials
- 6 rooms × **8 proposals** ≈ 48 cards. Per room, seed the first four classes; let **"exceptional" emerge** (it can't be manufactured on demand):
  - 1 **invalid** (violates a Stage-A gate — e.g. far under-scaled, collides with the window).
  - 2–3 **competent-generic** (safe compatibility/style-match picks, no thesis).
  - 2 **interesting-unresolved** (a bold idea that doesn't quite resolve).
  - 2–3 **bold-resolved** (bold + resolves) — from which reviewers may flag *exceptional*.

### Proposer instructions
- Give each designer: the 6 photos + catalogue + Room Diagnosis Schema (Artifact 1) + Thesis Library (Artifact 2).
- Per assigned room produce: (a) one **"safe"** proposal (the expected, low-risk choice) and (b) one **"your best / boldest coherent"** proposal; optionally (c) a **"bold but unsure it resolves"** one.
- On the hidden sheet: one-sentence thesis + the diagnosed problem it solves + the archetype.
- Work **independently**; never see others' proposals. Render to the standard format.
- Facilitator constructs the **invalid** seeds and the **naive-baseline generic** seeds.

### Reviewer instructions
- 3–5 designers/curators who did **not** propose.
- **You are judging design quality ONLY. Do NOT predict whether a homeowner would buy** — that is a separate study.
- Justify each verdict with the rubric's observable evidence. Force-rank each room's 8. Assign a class to each. ~3–4 min/proposal.

### Blind-review process
1. Facilitator strips metadata, codes proposals (R1-P01…P08), randomises order per reviewer, normalises render quality.
2. Reviewers work **independently, no discussion**, time-boxed.
3. Submit forms + rankings + class labels.
4. Only after all submitted: unblind, compile, then run the disagreement session.

### Evaluation form (per proposal) — maps to Artifact 4
- **A. Physically valid?** Yes/No → if No, which gate (scale / placement / obstacle / palette / realisable) + note.
- **B. Professionally competent?** Yes/No → if No, which floor (focal / weight / proportion / coherence / restraint) + note.
- **C1. State its one idea in a sentence:** ______ (blank = no legible thesis).
- **C2. Solves THIS room's problem?** Clearly / Partly / No.
- **C3. Non-obvious (beyond a compatibility pick)?** Yes / Somewhat / No.
- **C4. Whole room feels resolved after?** Yes / Somewhat / No.
- **C5. Proud to sign this?** Yes / No.
- **Class:** invalid / competent-generic / interesting-unresolved / bold-resolved / exceptional.
- **Judgment confidence:** High / Med / Low.
- **Per room:** force-rank P01…P08 best→worst.

### Result tables
- **Proposal table:** room · code · intended-class(unblind) · each reviewer's class · modal class · class-agreement% · mean rank · rank-variance · %valid · %competent · %proud-to-sign · thesis-legibility%.
- **Confusion matrix:** intended class × modal reviewer class (do reviewers recover the seeded classes?).
- **Agreement:** raw agreement % per stage (A, B, class) — report simply; kappa optional, not required (no artificial precision).

### Disagreement log
For every proposal split by >1 class tier or wide rank spread: code · the split · each reviewer's stated reason (from C1–C5) · resolution-discussion conclusion (the distinction surfaced). **This log is the seed for annotation guidelines.**

### Falsification (Study A)
- Stage A not near-unanimous → physical-validity rules miscalibrated.
- Reviewers can't recover seeded classes above chance (diffuse confusion matrix) → classes aren't distinguishable → framework fails to identify quality.
- **C2 (solves diagnosed problem) does NOT correlate with high rank** → the diagnose→thesis premise doesn't drive quality.
- No agreement on "exceptional" even after discussion → exceptional may be idiosyncratic (some top-end disagreement is expected; *total* non-agreement is the falsifier).

---

# STUDY B — Homeowner Purchase Evaluation
**Purpose:** do expert-rated **bold-and-resolved** proposals create stronger desire / confidence / willingness-to-buy than **safe** ones — and is the expert winner also the customer winner?

### Participants
- **15–25 homeowners / people currently decorating** (target users, NOT designers). Screen: have a wall they'd consider; spread of age/taste/budget. (Directional/qualitative sample, not a powered RCT.)

### Materials
- The **same proposals from Study A**, filtered to **Stage-A-valid + sellable**. Per room present a subset spanning safe→bold: at least one expert *competent-generic/safe*, one expert *bold-resolved*, and the *exceptional* if one emerged (~3–5 per room).
- Each participant evaluates **2–3 rooms** (fatigue limit), assigned to span problem types; optionally include one room close to their own situation.
- **No labels, no "bold/safe" hints, no prices** during the desire phase.

### Procedure
1. **Rapid gut pass:** show each proposal ~5s; capture immediate **want (0–10)** per proposal — before any deliberation.
2. **Considered view:** show the room's proposals together; capture the measures below.
3. Randomise order. Reveal price only at the willingness-to-pay step.

### Measures (captured separately — the correction's list)
1. **First emotional preference** — after the gut pass: "which did you feel drawn to first?" + the 0–10 want scores.
2. **Final choice** — after considered view: "which would you choose for this room?"
3. **"This is the one" reaction** — for the final choice: *the one* / *best of these* / *none really*.
4. **Confidence to live with it** — 0–10 + "any regret risk?"
5. **Willingness to buy now** — yes / maybe / no.
6. **Acceptable price** — first ask *their* expectation (Van-Westendorp style: too-cheap / bargain / getting-expensive / too-expensive), **then** reveal actual price + capture reaction.
7. **Reasons for hesitation** — open: "what would stop you buying?"
8. **Bold vs safe** — reveal the safe/bold pair (still unlabelled) and ask which they prefer + why; record whether they gravitate safe or bold.
9. **Expert-winner = customer-winner?** — compare each participant's final choice to the expert modal top-rank for that room.

### Result table
- **Per proposal:** mean gut-want · %first-preference · %final-choice · %"the one" · mean live-with confidence · %buy-now · price bands · top hesitation themes.
- **Per room:** expert #1 == customer modal choice? (Yes/No/Partial).
- **Cross-cut:** expert *bold-resolved* vs expert *safe/generic* on want / confidence / buy-now (directional).

### Interpretation nuance (state up front)
Study B tests **static** proposals (no interaction). Inevitability may *require* the reveal+reaction dynamic, so static "the one" rates may be modest — that's expected, and is exactly what Study C isolates. B answers only: *all else equal, does bold-resolved design create more desire/confidence than safe design?*

### Falsification (Study B — business-critical)
- **Bold-resolved does NOT beat safe on *want* AND *buy-now*** → the delight→confidence bet fails; the "bold" thesis is wrong for real buyers. (Biggest falsifier.)
- Customers systematically prefer safe/generic → reconsider the core promise.
- "The one" essentially never fires on static cards → inevitability needs the session → raises the stakes of Study C (not fatal alone).
- Expert winner ≠ customer winner *and* customers prefer expert-low-ranked → expert quality doesn't transfer to desire.
- Willingness-to-pay far below a viable price → pricing/positioning problem independent of design.

---

# STUDY C — Wizard-of-Oz Single Session
**Purpose:** can a human designer, following *diagnosis → thesis → intervention → composition*, take a stranger from one room photo to a **confidently purchasable wall in 10–15 min**, behaving like the future AI?

### Participants
- **8–12 strangers** who are target users (have a room, might decorate). Each **sends a photo of their actual wall ≥24h in advance** (this enables the WoZ pre-render).

### The "AI" (WoZ team)
- **Designer (the brain):** diagnosis, thesis, intervention/proposal choices, drives the session, close.
- **Operator (hidden hands):** renders fast — mostly pre-made per anticipated theses + a few live edits — so walls appear quickly.
- **Framing:** run over screen-share; present as "our system." Enforce AI-like behaviour regardless of framing.

### Designer preparation (per participant, from the pre-sent photo)
- Run the **Room Diagnosis Schema** → write the `room_problem`.
- Pick **3–4 candidate theses** (Artifact 3 protocol: span safe→bold, ≥1 restrained option, ≥1 tail move, all grounded).
- **Pre-render** the first bold proposal + 3–4 alternates on the participant's actual photo (**sellable catalogue only**).
- Prepare the **bundled price** and the close.

### Session script (10–15 min)
1. **Open (0–1):** minimal. "Let's design your wall." **No questionnaire** (photo already in hand).
2. **Reveal (1–2):** show the first **bold, grounded** proposal on their actual wall. "Here's what I'd do." Silence; let them react.
3. **Design conversation (2–9):** **one complete proposal at a time.** Participant reacts **"more like this / not this"** (+ free reactions). Designer answers with the next, better/bolder proposal. Enforce: show-before-ask · complete opinions · **no explaining unless asked** · no style questionnaire · **max ~4–6 cycles.**
4. **Landing (9–11):** on convergence, present the winning wall large; optional brief **"here's the range I explored"** overview (closing spatial moment).
5. **Close (11–14):** "make it real" — bundled price, everything included, ships in ~X. Ask for the decision.
6. **Reassure/end (14–15).**

### Allowed interventions
- **Sellable only** (framed prints, sizes, frames, multi-piece sets, and *sparse/one-small-piece* as the restraint option). Designable-not-sellable (mirror/shelf/moulding) **not used in C** — the close must be a real purchase.

### Reaction capture
- Record the whole session (screen + audio).
- **Per cycle log:** proposal shown (thesis/archetype) · participant reaction (more/not-this + verbatim) · timestamp · designer's next move + why.
- Mark any **"that's the one"** moment (verbatim + timestamp). Record confidence + purchase decision at close.

### Stop rules
- Hard stop at **15 min**.
- **Land** when: explicit "that's the one"/love · OR two consecutive proposals rejected on *minor* tweaks only (converged) · OR participant returns to a prior proposal as favourite.
- **Fatigue:** after ~6 cycles with no love → force a final **two-way contrast** ("of everything, these two — which is more you?") → close on the winner or record **"no landing."**

### Success criteria
- Reached a **confidently purchasable wall** (would-buy-now, or actually buys in the real-purchase variant) within 15 min — target the **majority** of sessions.
- A meaningful share produce a genuine **"that's the one"** moment.
- **Live-with confidence ≥ ~7/10** on the landed wall.
- The emotional signature appears ("I'd never have thought of that" / "how did you get that").

### Failure criteria
- Most sessions **don't land** in 15 min → single-session promise too ambitious / method too slow.
- Lands but **purchase intent stays low** → design lands, doesn't convert (price/trust/seeing).
- Participants **need the questionnaire**, keep asking "why", or can't react without specifying → show-before-ask/opinion-first fails for real users.
- The **designer can't operate the method live** (can't form a good thesis + render fast enough) → automation will be harder than hoped.

### Post-session interview
- "How did that feel vs. how you normally shop for art?"
- "Was there a moment it clicked? When?"
- "Did you feel understood — by the questions, or by the designs?"
- "How confident are you living with this? Any regret?"
- "Would you actually pay [price]? Why / why not?"
- "Did you miss being asked questions / choosing from more options?"
- "Bold vs safe — did the bolder ones excite or scare you?"
- "What would have made you more confident to buy?"

### Real-purchase variant (strongest signal)
- Offer a **genuine** buy option at the end (real product, participant discount). Actual conversion is the best data; at minimum a binding-feeling "reserve." Handle refunds/ethics cleanly.

---

## Logistics
- **Lean & directional**, not a powered RCT (no artificial precision). Runnable in a few weeks: recruit 3–5 proposer designers + 3–5 reviewers (A), 15–25 homeowners (B), 8–12 strangers + a 2-person WoZ team (C), one facilitator throughout.
- **Reuse across studies:** same 6 rooms + catalogue + render standard tie A and B together; C uses participants' own rooms.
- **Outputs feed the build:** A's labelled corpus + disagreement log = annotation guidelines for the future Taste Critic; C's session logs + winning theses = the Wizard-of-Oz playbook. Nothing here depends on further theory.
