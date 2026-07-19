# Latenca — Operational Design Intelligence (5 artifacts)

Turns the framework into a system a human designer can use tomorrow and we can later automate. **No UI, no prompts, no model architecture — the judgment itself.**

## Corrections honored (read first)
1. **`Resolution × Revelation` is a working hypothesis for the objective, NOT a proven/validated function.** It is used here only as a *reviewer question*, never as a computed score. Artifact 5 is designed to test it.
2. **No artificial numerical precision.** No weights, no 0–100 sub-scores. Everything is pass/fail, floor/no-floor, present/strong/absent, or rank-order — until the human study earns numbers.
3. **"Conviction beats hedging, *after* correctness is secured."** Boldness is only evaluated after Stage A (valid) and Stage B (competent) pass. A bold-but-incompetent design is rejected, not rewarded.
4. **The Taste Critic is one moat component, not the whole moat.** The moat is plural: the *diagnosis→thesis discipline*, *curated/sellable supply*, *render fidelity*, the *proprietary human-evaluation dataset* this study produces, and the Taste Critic. Do not over-index on the critic.
5. **Separate "can design" from "can sell."** The system reasons toward the *ideal* intervention (which may include mirror / shelf / moulding / lighting / empty). What we can currently *sell* is a subset (framed prints / posters via POD). Every artifact carries this split explicitly; the gap is strategic signal, not something to hide by silently degrading the design.

---

# Artifact 1 — Room Diagnosis Schema
The structured brief produced from one room photo. Each field: **observed · why it matters · possible values · confidence · influences.** `confidence ∈ {high, medium, low, unknown}`; **low/unknown fields are resolved by the in-session reaction loop, never by asking the user.**

### A. Architecture & surface
- **wall_surface** — *observed:* paint / brick / wallpaper / panelling / texture. *why:* competes with art, affects contrast & mounting. *values:* smooth-neutral / textured / patterned / feature-material. *conf:* high. *influences:* whether art must be simple/bold to read; frame choice.
- **architectural_features_on_wall** — *observed:* window, door, radiator, fireplace, moulding, switches, vents, corner. *why:* obstacles + pre-existing focal points. *values:* list w/ positions. *conf:* high. *influences:* usable zone, archetype (defer/counterbalance), placement gates.
- **ceiling_height** — *observed:* low / standard / high. *why:* vertical scale headroom. *values:* low / standard / high. *conf:* medium. *influences:* vertical vs horizontal archetype; stacking.

### B. Proportion & geometry
- **wall_dimensions_est** — *observed:* width×height in m, estimated via furniture/known-object reference. *why:* master scale constraint. *values:* metric range + reference used. *conf:* medium (high w/ depth sensor). *influences:* piece size, single-vs-multi, everything downstream.
- **wall_aspect** — *observed:* wide / square / tall / narrow-slot. *why:* dictates composition shape. *values:* those. *conf:* high. *influences:* horizontal/gallery vs vertical/stacked vs single.
- **usable_zone** — *observed:* area not blocked by furniture/features/obstacles. *why:* where art can actually live. *values:* region. *conf:* medium. *influences:* max size, placement, whether an idea is even feasible.
- **viewer_distance** — *observed:* primary viewing distance (sofa/bed to wall). *why:* scale & detail legibility. *values:* near / mid / far. *conf:* medium. *influences:* size, contrast, detail density.

### C. Furniture & objects
- **anchor_furniture** — *observed:* sofa / bed / console / sideboard / none. *why:* composition base + width reference + "above what". *values:* type + width. *conf:* high. *influences:* proportion rule, centering, height.
- **furniture_weight_position** — *observed:* visual weight heavy-left / centred / right / balanced. *why:* the imbalance the wall may counter. *values:* those. *conf:* medium. *influences:* symmetry vs asymmetry; side of emphasis.
- **existing_objects** — *observed:* existing art, TV, shelves, plants, lamps. *why:* focal competition/conflict. *values:* list. *conf:* high. *influences:* defer vs dominate; whether to edit.

### D. Visual weight & focal structure
- **room_weight_distribution** — *observed:* where the eye is pulled overall. *why:* the tension to resolve. *values:* left/right/centre/diffuse. *conf:* low–medium. *influences:* balance strategy.
- **existing_focal_hierarchy** — *observed:* is there already a dominant focal point? competing ones? *why:* the wall becomes / defers to / resolves the focal point. *values:* none / one-dominant / competing. *conf:* medium. *influences:* archetype; whether the wall's job is to *lead* or *quiet down*.

### E. Palette & material
- **dominant_palette** — *observed:* neutral / warm / cool / specific hues. *why:* harmony vs contrast. *values:* named. *conf:* high. *influences:* piece palette, accent vs blend.
- **material_palette** — *observed:* wood tone, metals, textiles. *why:* frame & material echo. *values:* named. *conf:* medium. *influences:* frame choice, "built-in" feel.
- **room_contrast_level** — *observed:* high / low overall contrast. *why:* whether bold or quiet reads. *values:* high/low. *conf:* medium. *influences:* boldness ceiling.

### F. Light
- **natural_light** — *observed:* direction + intensity. *why:* glare, colour rendering, best-time read. *values:* strong/soft + direction. *conf:* medium. *influences:* matte vs glossy, palette, placement away from glare.
- **light_temperature** — *observed:* warm / cool / mixed. *why:* how colours read. *values:* those. *conf:* low–medium. *influences:* palette warmth.

### G. Purpose & mood
- **room_type** — *observed:* living / bed / dining / office / hall. *why:* the room's job. *values:* those. *conf:* high. *influences:* mood target, formality, energy.
- **mood_target** — *observed:* inferred use → rest / energy / welcome / focus / intimacy. *why:* the emotional target design resolves toward. *values:* those. *conf:* **low (infer boldly, correct via reactions).** *influences:* everything in Stage C.
- **formality** — *observed:* casual / formal. *why:* symmetry & restraint. *values:* those. *conf:* low–medium. *influences:* symmetric vs dynamic.

### H. Complexity & rest
- **visual_complexity_budget** — *observed:* how much more the room can take (busy → little; sparse → lots). *why:* prevents over-adding; may *require* restraint. *values:* low / medium / high. *conf:* medium. *influences:* calm-vs-complex archetype; mandatory-restraint trigger.
- **rest_need** — *observed:* does the room need a quiet/breathing wall? *why:* gate for the empty/restraint archetype. *values:* yes/no. *conf:* low–medium. *influences:* whether "add nothing / add little" must be a candidate.

### I. Physical & commercial constraints
- **mountable_constraints** — *observed:* obstacles, max feasible size, surface issues. *why:* feasibility gate. *values:* limits. *conf:* high. *influences:* Stage A gates.
- **sellability_map** — *observed:* which parts of the ideal intervention we can currently produce (framed prints yes; mirror/shelf/moulding/lighting **not yet**). *why:* design-vs-sell split. *values:* sellable / designable-not-sellable. *conf:* high. *influences:* realization + the strategic gap flag (never silently degrade the design).

### Synthesis (the bridge to thesis)
- **room_problem** — one sentence naming what's unresolved, + the 2–3 fields driving it, + overall confidence. This is the input to the Thesis Library.

---

# Artifact 2 — Design Thesis Library (organized by *problem*, not style)
Each thesis: **diagnosis · intent (one sentence) · archetypes · contraindications · bold when · fails when · trace.** (Full entries below; abbreviated for density but complete.)

**Group 1 — Emptiness / under-anchoring**
- **T1 Blank oversized wall.** *diag:* large empty wall, no anchor. *intent:* "Give the wall one confident centre of gravity." *arch:* single oversized statement piece. *contra:* wall too small; competing focal feature. *bold:* go much larger than expected. *fails:* piece too small → floats. *trace:* "2.6 m empty wall over a low sofa → one ~140 cm piece, centred, to anchor the whole zone."
- **T2 Furniture dwarfed by wall.** *diag:* art/furniture look lonely under a tall/wide wall. *intent:* "Extend the furniture's presence up the wall." *arch:* vertical stack / tall single / gallery rising from furniture. *contra:* low ceiling. *bold:* fill the vertical void decisively. *fails:* timid single small piece. *trace:* "Sideboard on a 3 m wall → a tall triptych rising two-thirds up to marry furniture and wall."
- **T3 Cold / impersonal room.** *diag:* correct but soulless. *intent:* "Introduce one piece of human warmth." *arch:* single evocative work / warm-toned statement. *contra:* already busy. *bold:* choose emotion over decoration. *fails:* generic 'nice' print. *trace:* "Grey minimal room → one warm, human, textural piece to break the chill."

**Group 2 — Imbalance**
- **T4 Off-centre architectural element.** *diag:* a door/window pulls the wall off-axis. *intent:* "Rebalance around the off-centre element." *arch:* asymmetric composition / offset single. *contra:* symmetrical formal room. *bold:* lean into the asymmetry, don't fight it. *fails:* forced centring that looks wrong. *trace:* "Window hard-left → weight the art right to settle the wall."
- **T5 One-sided furniture weight.** *diag:* heavy furniture one side. *intent:* "Counterweight the heavy side." *arch:* offset single / asymmetric pair. *contra:* balanced room. *bold:* strong single counterweight vs timid spread. *fails:* even spread that ignores the imbalance. *trace:* "Heavy left bookcase → a bold piece right as a counterweight."
- **T6 Vertical void.** *diag:* low furniture, tall empty wall above. *intent:* "Occupy the vertical." *arch:* stacked / tall vertical. *contra:* low ceiling. *bold:* commit to real height. *fails:* one small piece stranded high. *trace:* "Low bench, 3 m ceiling → a tall vertical to own the height."
- **T7 Marooned piece on a wide wall.** *diag:* wide wall, single small work adrift. *intent:* "Make the wall read as one intended field." *arch:* horizontal single / gallery band. *contra:* narrow wall. *bold:* horizontal scale or a deliberate wide set. *fails:* under-scaled single. *trace:* "4 m wall → a wide horizontal, not a lonely square."

**Group 3 — Competition / too busy**
- **T8 Busy room, needs calm.** *diag:* patterns/objects everywhere at eye level. *intent:* "Give the eye one calm place to rest." *arch:* single low-contrast / restrained. *contra:* sparse room. *bold:* restraint amid chaos is the bold move. *fails:* adding more complexity. *trace:* "Patterned sofa + rug + shelves → one calm large low-contrast piece."
- **T9 Competing focal points.** *diag:* TV + window + fireplace fight. *intent:* "Subordinate the wall so one focus wins." *arch:* quiet single / defer. *contra:* no existing focus. *bold:* deliberately *not* competing. *fails:* a loud piece that adds a 4th focus. *trace:* "TV + fireplace → a quiet piece that yields to the fireplace."
- **T10 Cluttered wall/shelves.** *diag:* accumulation, no order. *intent:* "Edit, then anchor." *arch:* subtraction + one anchor. *contra:* intentional collection. *bold:* remove more than you add. *fails:* piling a new piece on top. *trace:* "Crowded shelves → clear two-thirds, anchor with one work."

**Group 4 — Ignored asset**
- **T11 Ignored architectural feature.** *diag:* fireplace/arch/moulding unused. *intent:* "Make the feature the hero; support it." *arch:* pieces that frame/defer to it. *contra:* no feature. *bold:* let the architecture lead, art plays second. *fails:* art that upstages the feature. *trace:* "Beautiful mantel → a piece scaled to crown, not compete."
- **T12 Great view/window.** *diag:* the window is the art. *intent:* "Defer to the view; frame the moment." *arch:* restrained flanking / empty. *contra:* no view. *bold:* the courage to add almost nothing. *fails:* blocking/competing with the view. *trace:* "Garden window → keep the wall quiet, let the view star."
- **T13 Strong existing hero piece.** *diag:* a great sofa/object already leads. *intent:* "Support the existing hero, don't rival it." *arch:* quiet complements. *contra:* nothing notable. *bold:* restraint in service of what's there. *fails:* a second competing hero. *trace:* "Sculptural chair → a subdued piece that lets it lead."

**Group 5 — Proportion mismatch**
- **T14 Narrow slot between features.** *diag:* tight vertical strip. *intent:* "Honour the slot with a vertical gesture." *arch:* single tall narrow. *contra:* wide wall. *bold:* embrace the narrowness. *fails:* cramming a wide piece. *trace:* "40 cm strip between doors → one tall narrow work."
- **T15 Long low band (above sideboard).** *diag:* wide short wall. *intent:* "Answer the horizontal with a horizontal." *arch:* wide single / horizontal row. *contra:* tall wall. *bold:* full-width commitment. *fails:* a centred square leaving dead ends. *trace:* "2.4 m over a credenza → a wide horizontal spanning it."
- **T16 Small room feels smaller.** *diag:* cramped, low light. *intent:* "Add depth and light." *arch:* mirror (design) / luminous piece (sellable). *contra:* large bright room. *bold:* mirror over art. *fails:* a dark heavy piece. *trace:* "Small dim nook → a mirror to double light [design]; if not sellable, a luminous high-key print [sell]."

**Group 6 — Mood / job mismatch**
- **T17 Un-restful bedroom.** *diag:* bedroom lacks calm. *intent:* "Lower the room's volume." *arch:* single soft horizontal above bed. *contra:* energetic room wanted. *bold:* quiet + large. *fails:* busy/high-contrast over the bed. *trace:* "Bed wall → one wide, soft, low-contrast piece for rest."
- **T18 Low-energy workspace.** *diag:* flat, uninspiring desk wall. *intent:* "Inject focused energy." *arch:* graphic / structured / bold single. *contra:* rest space. *bold:* real graphic punch. *fails:* bland decoration. *trace:* "Home office → one structured, energising piece in sight-line."
- **T19 No-impression entry/hall.** *diag:* first-impression wall is blank. *intent:* "Make a confident first statement." *arch:* bold single / tight gallery. *contra:* tiny hall. *bold:* set the tone loudly. *fails:* a timid small piece. *trace:* "Entry → one arresting piece as the home's opening line."
- **T20 Cold dining.** *diag:* dining lacks intimacy. *intent:* "Warm and gather the room." *arch:* warm single / pair at seated eye-level. *contra:* formal restraint wanted. *bold:* warmth + intimacy of scale/height. *fails:* cold or too-high hanging. *trace:* "Dining wall → warm piece hung to seated eye-level."

**Group 7 — Character / identity**
- **T21 Generic room, no view.** *diag:* nothing says who lives here. *intent:* "Give the room one point of view." *arch:* a single characterful, opinionated work. *contra:* client wants neutral. *bold:* a definite aesthetic stance. *fails:* safe 'goes-with-anything'. *trace:* "Show-home feel → one opinionated piece to claim identity."
- **T22 Collector with nothing shown.** *diag:* person has taste, wall is bare. *intent:* "Let the wall perform their taste." *arch:* curated gallery wall. *contra:* minimalist. *bold:* a confident, dense, well-ordered set. *fails:* random scatter. *trace:* "Eclectic owner → a structured salon gallery."
- **T23 Over-decorated ('trying too hard').** *diag:* too many competing statements. *intent:* "Reduce to one clear voice." *arch:* subtraction + single anchor. *contra:* deliberately maximalist. *bold:* remove most of it. *fails:* adding another statement. *trace:* "Five competing pieces → keep one, remove four."

**Group 8 — Light / colour**
- **T24 Dark wall/room.** *diag:* low light, heavy feel. *intent:* "Lift the wall." *arch:* mirror [design] / high-key luminous print [sell]. *contra:* bright room. *bold:* reflective/luminous over dark. *fails:* a dark, absorbing piece. *trace:* "North-facing dim wall → a luminous high-key work."
- **T25 Monochrome room, needs an accent.** *diag:* all-neutral, slightly flat. *intent:* "Introduce one deliberate accent." *arch:* single accent-colour piece. *contra:* client wants pure neutral. *bold:* one confident colour note. *fails:* a timid tonal match that disappears. *trace:* "Greige room → one considered accent to give it a pulse."
- **T26 Busy palette, needs unifying.** *diag:* many competing colours. *intent:* "Bridge the palette with one work." *arch:* single piece carrying the room's colours. *contra:* already unified. *bold:* a piece that ties disparate hues. *fails:* adding a clashing new hue. *trace:* "Clashing cushions → one piece that reconciles the colours."

*(All 26 are the working set; the human study will prune, merge, and add.)*

---

# Artifact 3 — Candidate Generation Protocol (one room → genuinely different proposals)
Goal: **meaningfully different professional proposals, not cosmetic variations.**
1. **Generate 3–5 *theses* (not 3–5 pieces).** Diversity is enforced at the *thesis* level: each candidate must solve a *different diagnosed problem* OR take a *materially different stance* on the same problem (e.g. "anchor boldly" vs "let it breathe" vs "defer to the feature").
2. **Diversity rules (hard):** no two candidates may share the same *archetype + scale-band + mood*; the set must span the range from *expected* to *bold*; at least one candidate must be a move a compatibility-recommender would **not** produce (a tail move).
3. **Mandatory restraint candidate:** whenever `visual_complexity_budget = low`, or an architectural asset is being ignored, or the room is at capacity, the set **must** include a restrained/empty thesis ("add little / add nothing / edit"). The system must be *able to propose less.*
4. **The safe-centre is a baseline to beat, not a default:** generate one *expected* proposal explicitly, but it is shown **only if** the bold candidates fail Stage A/B/C. Never default to it.
5. **Grounding (hard):** every proposal must cite the Room-Diagnosis field(s) it responds to, and its scale/placement/palette must be derived from the measured brief. A proposal that ignores the brief is invalid by construction.
6. **Catalogue constrains realization, not the thesis:** form the thesis and composition **first** (the creative act). Then map to sellable products. If the ideal composition can't be realized from the catalogue, **flag the design-vs-sell gap** and either (a) realize the *nearest sellable* composition that still serves the thesis, or (b) mark it designable-not-sellable. The catalogue must never be the starting point or narrow the creative thesis.

---

# Artifact 4 — Evaluation Rubric (hierarchical, gate-first, no weights yet)
Each criterion: **observable evidence** + **explicit rejection condition.** Stages are ordered; failing an earlier stage stops evaluation.

### Stage A — Physical validity gates (objective, pass/fail)
- **Scale** — *evidence:* piece(s) span ≈ half-to-two-thirds of the anchor width. *reject if:* far under-scaled or overflows the usable zone.
- **Placement/height** — *evidence:* centred in the standard eye-level band relative to furniture. *reject if:* collides with furniture/ceiling/obstacles or floats.
- **Obstacle respect** — *evidence:* clears switches/vents/window/door-swing/radiator. *reject if:* overlaps any.
- **Palette relationship** — *evidence:* harmonises or *intentionally* contrasts. *reject if:* accidental discord with no rationale.
- **Realisable** — *evidence:* buildable + sellable, or explicitly flagged designable-not-sellable. *reject if:* not buildable.

### Stage B — Professional quality floor (each must clear a floor)
- **Single focal hierarchy** — *evidence:* one dominant element. *reject if:* competing equal centres.
- **Resolved visual weight** — *evidence:* weight answers the room's existing weight. *reject if:* lopsided with no counter.
- **Proportion & rhythm** — *evidence:* consistent spacing/alignment. *reject if:* arbitrary gaps/misalignment.
- **Coherence with room** — *evidence:* palette/material harmony or intentional contrast. *reject if:* incoherent with the room.
- **Restraint** — *evidence:* every element earns its place. *reject if:* anything is superfluous.
> Stage B = "a competent designer would not be embarrassed." Competence is the *floor*, not the win.

### Stage C — Authored resolution (qualitative: absent / present / strong — NO weights)
- **Legible thesis** — *evidence:* a reviewer can state the one idea in a sentence. *reject/downgrade if:* no single idea.
- **Solves the diagnosed problem** — *evidence:* it addresses the room's actual problem (from the brief), not generic prettification. *reject if:* pretty but solves nothing.
- **Resolution (hypothesis)** — *evidence:* the *whole room* feels more intentional/at-rest after. *reject if:* only the object is nice, room unchanged.
- **Revelation (hypothesis)** — *evidence:* non-obvious; beyond a compatibility pick. *downgrade if:* it's the expected move.
- **Coherence of intent** — *evidence:* every element serves the one idea. *reject if:* assembled from unrelated parts.
- **Conviction (after correctness)** — *evidence:* a committed bold bet, given A+B already pass. *downgrade if:* hedged/safe.
> `Resolution` and `Revelation` are **hypotheses under test** (Artifact 5), used as reviewer questions, not computed.

### Stage D — User-reaction update (in-session fit, not wall-quality)
- **Reaction interpretation** — *evidence:* infer which dimension the user responded to; update the read. *rule:* early "not this" → larger jump; "more" → push that direction + resolve next uncertainty.
- **Stop/convergence** — *evidence:* explicit love, or rejections cease with only tiny tweaks left, or repeated return to one. *rule:* offer the close at the peak; on fatigue, force a final two-way contrast.

---

# Artifact 5 — Human Evaluation Test (the first study)
**Purpose:** does the framework reliably distinguish *invalid / competent-generic / interesting-unresolved / bold-resolved / exceptional* — using the same room photo + catalogue? Also: does "solves the diagnosed problem + legible thesis + room-after-resolved" predict expert top-picks, and do bold-resolved proposals convert to "would buy" better than safe ones?

**Participant roles**
- **Proposers:** 3–5 interior designers (mixed seniority) + 1 deliberate *baseline generator* (a naive style-match/compatibility pick, or a non-designer) to guarantee generic/invalid examples exist.
- **Reviewers:** 3–5 independent designers/curators who did **not** propose.
- **Facilitator:** neutral; runs blinding, randomisation, collation.

**Material**
- **Rooms:** 5–8 real room photos spanning different problem groups from Artifact 2 (not one room — test across problem types).
- **Proposals:** per room, 6–8 proposals, deliberately seeded to include each target class (ask some designers for a "safe" and a "bold" version; include the baseline generic; include ≥1 intentionally invalid to test Stage A). Aim to have all 5 classes present per room (seeded, not guaranteed).

**Blind-review method**
- Strip proposer identity, seniority, and all rationale. Randomise order. Reviewers see only room photo + proposal render + the catalogue. Reviewers do not know a proposal's intended class.

**Evaluation questions (map to the rubric)**
- Stage A: physically valid? (yes/no + reason)
- Stage B: professionally competent? (yes/no + which floor fails)
- Stage C: state its one idea in a sentence; does it solve *this* room's problem?; is it non-obvious?; does the whole room feel resolved?
- **Force-rank** all proposals for the room, best→worst.
- **Assign each to one of the 5 classes.**
- "Would you be proud to sign this?" (master test)
- "Would a typical homeowner confidently *buy* this?" (separate buy dimension)

**Disagreement handling**
- Measure inter-rater agreement per stage. **Pre-registered expectation:** near-unanimous on Stage A, strong on Stage B, *lower* on Stage C (taste) — and lower is informative, not a failure. Resolve disagreements by **discussion to surface the *why*** (this becomes the annotation guidance). Do **not** average disagreement away — catalogue it.

**Success thresholds (qualitative until data earns numbers)**
- **A:** reviewers near-unanimous on validity. *(else the physical rules are wrong.)*
- **B:** strong majority agreement on competence.
- **C:** reviewers rank *bold-resolved* and *exceptional* above *competent-generic* **consistently across rooms**, and the rubric's class assignments track reviewer consensus **better than a style-match baseline.**
- **Predictive core:** proposals scoring high on "solves the diagnosed problem + legible thesis + resolved room" are the ones reviewers independently rank top.

**What would falsify the framework**
- Experts cannot agree on "exceptional" even after discussion → the objective may be unlearnable.
- Rubric classes do not predict expert rankings → Stage C criteria don't track quality.
- "Solves-the-diagnosed-problem" proposals are **not** preferred over generic-pretty ones → the diagnose→thesis premise is wrong.
- **Business-critical:** bold-resolved proposals do **not** convert to "would buy" better than safe ones → the delight→confidence bet fails; revisit before building.

**Output usability**
- The labelled corpus (room, proposal, class, rank, one-sentence thesis, rationale, agreement level, sellable/flag) becomes: (a) the **Wizard-of-Oz playbook** (the human "AI" reuses the winning theses/archetypes/traces), and (b) the **seed annotation set + guidelines** for later training the Taste Critic — each proposal is an example with a quality label *and* a written rationale, i.e. the annotation schema itself.

---

## Status & next step
- **Accept the direction:** diagnosis → thesis → intervention → composition → products. ✔
- **Do NOT lock:** the scoring formula, the `Resolution × Revelation` objective, or "Taste Critic = the whole moat." All remain hypotheses pending the study.
- **Next action:** run Artifact 5 on real rooms. It both validates the framework and produces the first proprietary dataset.
- **Known tension (flagged, not resolved):** this framework *contradicts* current product rules — "ask before assuming", "explain every recommendation", "linear context gathering." Those need **formal revision only after** the operational model is validated. Do not rewrite them yet.
- **Docs to revise post-validation:** `WALL_DESIGN_KNOWLEDGE.md`, `AI_SYSTEM.md`, `DECISIONS.md`, `BACKLOG.md`, `PROJECT_STATUS.md`. (Left unchanged for now — pending study results.)
