# Latenca — the Design Intelligence Framework

> The interaction is locked. This is the product now: *how the AI arrives at "here's what I'd do."* This is the moat.

## The one idea that separates exceptional from average
Two AIs, same room, same catalogue, same reactions. The average one produces a forgettable wall because it optimizes the wrong thing in the wrong shape:
- **Wrong thing:** it scores the *object* — "how well does this artwork match this room?" (compatibility/retrieval). A designer scores the *effect on the whole room and the person after* — "what does this wall do to the space?"
- **Wrong shape:** it optimizes an **additive** objective (maximize expected likability across many dimensions). An additive objective is *maximized at the mean* — the safe center — which is exactly why AI regresses to generic. A designer optimizes a **peaked, multiplicative** objective that rewards *one bold, coherent bet* and punishes hedging.

Fix both and you have Latenca's intelligence: **evaluate the room-after, not the object; and reward the resolved-bold, not the safe-average.**

---

## 1. What the AI optimizes for (the objective function)
Not match. Not likability. The objective is over the **room-as-a-system, after the intervention**, and it's the product of two terms:

**Objective = Resolution × Revelation**

- **Resolution** — how completely the wall makes the *whole room* feel intentional and at rest, resolved toward the room's *purpose* (rest / gather / focus). Every room has a tension (something unfinished, unbalanced, a blank wall pulling at you); resolution is how much that tension is discharged. This is the *inevitability* term.
- **Revelation** — how far the solution is from what the person (or a compatibility-recommender) would have reached themselves. This is the *"I'd never have thought of that"* term.

They multiply because either alone fails: resolution without revelation = safe and boring (recommender); revelation without resolution = novel and wrong (Midjourney chaos). **Their product *is* "surprising-yet-inevitable"** — our delight target now has a mathematical shape. The AI optimizes for the room feeling *inevitable* in a way the user *couldn't have authored.*

## 2. How it scores a wall (0–100) — and why it's NOT a weighted average
A flat weighted sum of composition+balance+harmony+… is itself the regression-to-mean trap: averaging many decent dimensions yields safe mush. Great design is **peak excellence on a few dimensions with deliberate sacrifice on others**, not evenness. So scoring is **three tiers, non-linear:**

**Tier 0 — Gates (pass/fail; any violation → score 0, never shown).** The non-negotiables of competence:
- Scale/proportion correct (art ≈ 2/3 of the reference span; the #1 amateur failure is too-small).
- One clear focal hierarchy (no competing centers).
- Sight-lines / height / function respected (doesn't fight furniture, doors, switches; ~145–150 cm center).
- Palette relationship intentional (harmonize or deliberately contrast — never accidental discord).
- Physically real (buildable, buyable).

**Tier 1 — Craft (the competence score, thresholded — no dimension may be *bad*).** Composition, balance, proportion-to-room, harmony, and — weighted heavily because amateurs and AIs both under-value it — **restraint** (nothing unnecessary; the discipline to stop/subtract). Tier 1 gets you to *competent and pleasant*. A recommender maxes out here and stops → safe walls. **Competence is the price of entry, not the win.**

**Tier 2 — Authored (the greatness multiplier).** This is where the design has a point of view: **conviction** (commits to one idea, doesn't hedge), **tension** (a deliberate controlled imbalance/contrast — perfect balance is dead; *resolved* tension is alive), **surprise/originality** (the non-obvious move), **emotional resonance** (strongly *does* the room's intended feeling), and **coherence of intent** (every element serves ONE idea — reads as authored by one mind).

**The formula (the important part):**
`Score = Gates(0/1) × Competence(thresholded) × (1 + Authored)`
You must pass the gates; competence must clear a floor (no fatal weakness); then greatness is a **multiplier driven by the single boldest *coherent* bet.** Consequence: **a wall that's 70 on competence but 95 on one authored idea beats a wall that's 85-on-everything and bold on nothing.** That non-linearity — rewarding the peak, not the average — is the mathematical statement of "design is a coherent bet, not an average," and it is the single most important line in this document.

## 3. Where opinions come from (choosing the move)
A recommender only knows one move: "hand you an artwork." A designer first chooses the **kind of intervention**, by *diagnosing the room*:
1. **Diagnose the wall's problem.** Too empty/cold? Too busy, needs an anchor? Awkward proportion (too wide/tall/off-center)? Competing focal points? A feature being ignored? Bad light?
2. **Read the room's job & mood target** (rest / energy / welcome).
3. **Map problem → archetype** (each is a tool with indications *and* contraindications):
   - *One large statement piece* — an under-anchored wall; a calm room wanting a single confident note.
   - *Gallery wall* — a wide wall; a collector; a room that wants personality and can hold complexity.
   - *Asymmetry / off-center* — balances an existing off-center element; a room wanting dynamism over formality.
   - *Mirror* — a dark/small room needing light & depth; a wall facing something worth reflecting.
   - *Shelf / mixed media / objects* — a person who collects; a wall that should feel lived-in and layered.
   - *Empty / restraint* — an already-busy room; a wall whose job is to give the eye rest; let architecture or one feature speak. **The confidence to propose *nothing* is the mark of a master** — most AIs and amateurs literally can't.
4. **Pick the archetype that best resolves the diagnosed problem toward the mood target — then push it to its most confident version.** The specific artwork is chosen **last**, to serve the composition. *Think in interventions, not objects.*

## 4. How it thinks like a designer, not a recommender (the reasoning loop)
- **Recommender (bottom-up, object-first):** room features → similarity search over catalogue → rank by match. Mean-seeking, object-centric.
- **Designer (top-down, thesis-first):**
  1. See the **whole room as a system** — its story, tension, purpose, existing focal hierarchy.
  2. **Diagnose** what's unresolved.
  3. **Form a thesis** — one sentence of intent: *"This room is busy at eye level, so the wall's job is to be calm, large, and let it breathe."* The thesis is the point of view; everything serves it.
  4. **Choose the move** (archetype) that executes the thesis.
  5. **Compose** — scale, placement, balance, focal hierarchy, negative space — in service of the thesis.
  6. **Select the specific pieces last** — art is the material that realizes the composition.
  7. **Critique against the thesis** — cut anything not serving the one idea (restraint); ask *is it inevitable yet?* If not, push bolder or reframe.
The inversion — **author a thesis first and let it constrain everything** — is the entire difference. It's what makes output feel authored by one mind instead of assembled by a committee.

## 5. What makes an opinion bold (safe → interesting → great → inevitable)
- **Safe** = the statistically likely choice; minimizes objection and variance. The mean. Correct, forgettable. (AI's default.)
- **Interesting** = departs from the mean on one axis; a bet with a point of view that *might not* resolve.
- **Great** = a bold bet that *resolves* — the departure turns out *more right* than the safe choice. Surprise + resolution.
- **Inevitable** = great, but so resolved that in hindsight it seems obvious — the surprise disappears into rightness.
Mechanism: **boldness = distance from the safe center, in a *coherent* direction, that still resolves.** Quantify surprise as divergence from the expected/likely distribution; then keep only tail-moves that still pass gates and resolve the room. **This is precisely why ordinary AI can't be bold: it's trained to maximize likelihood, which means *living at the mean.* Latenca's value function must actively *reward resolved-tail moves* over the mode.** Bold ≠ random; bold = conviction where the mean-seeker won't go, that still lands.

## 6. Pre-ML knowledge — the master designer as a structured system (zero user data)
The "physics engine" that makes a competent, never-embarrassing designer before any learning. Four layers:
- **Perceptual/physical laws (near-deterministic):** scale ratios, hanging height (~145–150 cm center), group spacing (5–8 cm), filled-to-empty proportion, sight lines, viewing distance, how light of a given temperature/direction reads a piece.
- **Compositional principles (strong heuristics):** focal hierarchy (one dominant element), visual weight & balance, dynamic symmetry / thirds, rhythm & repetition, **negative space as an active element**, Gestalt grouping, **tension & resolution.**
- **Room-as-system knowledge:** every room has a purpose, a mood target, an existing focal hierarchy, a *visual-complexity budget* (busy rooms need calm walls; sparse rooms can hold complexity), and a light character. The wall's job is defined *relative to these.*
- **A move-library (clinical decision system):** each archetype mapped to the problems it solves and the ones it worsens (indications/contraindications).
- **Meta-principles (judgment):** solve the room not the wall; commit to one idea; restraint is the hardest skill; the room-after > the object; match the wall's energy to the room's job, then push one notch; the best move is sometimes less.
This layer guarantees Tier-0 and most of Tier-1 with no data — the AlphaGo "rules + handcrafted features."

## 7. How it avoids generic (regression to the mean)
Root causes of generic: additive objectives (max at the mean), scoring the object's likability, and hedging (many constraints → mush). Antidotes, all already built into the framework:
- **The thesis constraint** — every design traces to ONE intent; non-serving elements are cut. One mind's coherence is the opposite of committee-mush.
- **The multiplicative/peaked objective** — reward the peak authored bet, punish hedging; explicitly value deviation-that-resolves.
- **Restraint as a scored virtue** — force *subtraction*, defeating the generic urge to add.
- **Tail sampling + resolution filter** — generate from the bold tails (unexpected archetype/scale/emptiness), keep only what resolves; never sample the mode.
- **Radical grounding** — every move solves *this specific room's* diagnosed problem, so the output is bespoke by construction. (Generic = ignoring the room's specifics.)
- **A "would a master sign this?" critic** — penalizes the safe/obvious even when it scores fine on competence.

## 8. Rules vs. intuition (deterministic vs. learned)
- **Rules (deterministic, hand-coded, verifiable):** scale/proportion math, height, spacing, sight-lines, palette-clash & physical gates, archetype indications/contraindications, the compositional laws expressible as constraints. → The Tier-0 gates + much of Tier-1. *Knowable and teachable; encode it.* Guarantees never-embarrassing.
- **Intuition (learned aesthetic judgment):** Tier-2 — beauty, what *resolves*, what feels *inevitable*, when a bold bet pays, emotional resonance, taste. Unspecifiable; learned from a corpus of genuinely great design + refined by human aesthetic feedback (curators / taste-RLHF). → The learned **value network.**
Mirrors AlphaGo exactly: **rules define legal, competent play; the learned value network provides judgment.** Crucially, **the learned taste operates *inside* the rule-constraints** — it never trades competence for novelty; it finds greatness *within* the space of the competent. That's how you get bold *and* never embarrassing.

## 9. Principles to teach a junior (decision-making, not decoration)
1. **Design the room, not the wall.** Judge every choice by what it does to the whole space and the person in it.
2. **Diagnose before you prescribe.** The wall solves a problem; find the problem first.
3. **Have one idea.** If you can't state the thesis in a sentence, it isn't designed yet.
4. **Commit.** Conviction beats correctness. Don't average your options — choose.
5. **Scale is everything — and bigger is usually right.** Timidity in size is the most common failure.
6. **Restraint is the highest skill.** Subtract to the essential. The confidence to leave space empty is mastery.
7. **Tension, not just harmony.** Perfect balance is dead; introduce a controlled imbalance and resolve it.
8. **Earn the surprise.** Be non-obvious only in a way that ends up feeling obvious. Novelty without rightness is noise.
9. **Respect the room's job — then push one notch past expectation.**
10. **The test is inevitability.** You're done when it looks like it was always meant to be there.

## 10. The acid test — strip the UI; does the *reasoning* read as world-class?
Print the AI's internal trace — diagnosis, thesis, chosen move, composition logic, self-critique. Hand it to a top interior designer.
- If it reads *"matched the palette, popular size, highly-rated print"* → it's a recommender in costume. **Not ready.**
- If it reads *"the room is heavy and busy on the left and chaotic at eye level, so the wall's job is a single calm counterweight on the right — one oversized, low-contrast horizontal piece, hung low, to balance the sofa and let the room breathe"* → it's a designer. **Ready.**
**The readiness gate for the whole company:** the reasoning must stand alone as design thinking a master would be proud to sign. If, UI-stripped, the argument for each wall isn't one an exceptional designer would make, the product isn't ready — no interface can rescue that.

---

## The intelligence, as one system (the "evaluation function", à la AlphaGo)
- **Room Reader** — photo → structured brief (geometry, scale, light, palette, furniture, focal hierarchy, function) **+ the diagnosed problem.**
- **Rulebook / Design Prior** — deterministic competence + the archetype decision system (legal, never-embarrassing moves). *(≈ AlphaGo rules + features.)*
- **Thesis Former** — brief → one-sentence intent. *(the point of view)*
- **Move Generator (policy)** — thesis → candidate archetypes → candidate compositions, **sampled from the tails, grounded in the room.**
- **Taste Critic (value network) — THE MOAT** — scores each candidate by *Gates → Competence-floor → Authored-multiplier → Resolution×Revelation*; the learned aesthetic judgment that kills the safe and crowns the inevitable.
- **Restraint/Coherence Editor** — removes anything not serving the thesis; asks "inevitable yet?" and pushes or reframes. *(≈ lookahead: simulate the room-after.)*

The interaction was never the moat. **The moat is the Taste Critic** — a learned value function for *walls-in-rooms* that reliably prefers the resolved-bold over the safe-average — plus the *diagnosis→thesis* discipline that makes every output authored. Build that, and two AIs looking at the same room stop producing the same wall.
