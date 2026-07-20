# Architectural Lock Registry

Authoritative status of every major decision. See `REVIEW_WORKFLOW.md` for how this is used. The registry moves **only** through a `DECISIONS.md` entry — never silently.

Legend: **LOCKED** = change needs an explicit architectural decision · **ACTIVE** = evolving this milestone · **BACKLOG** = must not modify current architecture.

## 🔒 LOCKED (architecture — do not change without a decision)
| Item | Where it lives | Locked because |
|---|---|---|
| **Single-session product** (~90% use once; value must land in one 10–15 min session; no dependence on long-term personalization) | `ai/exploration/RETHINK-the-primitive-v4-single-session.md`, `docs/PRODUCT-BLUEPRINT-single-session.md` | Defines the whole optimization target |
| **Neutral/sample-wall-first, Mixtiles-style** (D-021) — compose from the catalog on a clean or sample-room wall; customer room photo is **optional & best-effort**, not the core. *(Supersedes the earlier "photo-first".)* | `docs/DECISIONS.md` D-021 | ~80% won't upload; room compositing is unreliable and breaks trust when it fails |
| **Opinion-first** (AI leads with a bold, complete design; understanding emerges from reactions; no interrogation, no unsolicited explanation) | `ai/exploration/RETHINK-the-primitive-v5-opinion-first.md`, `ai/AI_SYSTEM.md` | The core interaction stance |
| **React-don't-specify** (user reacts to complete proposals; taste is recognized, not described) | RETHINK-primitive series | The primitive |
| **Sequential interaction** (one bold proposal at a time; NOT spatial navigation) | `ai/exploration/RETHINK-sequential-vs-spatial.md` | Forced by "taste is recognized, not described" + single-session |
| **Closing overview** ("the range I explored" collapsing to the chosen wall, at the landing) | RETHINK-sequential-vs-spatial | The one borrowed spatial benefit (no-regret) |
| **Latenca = an intelligent FRONT orchestrating external AI; models are rented behind a swap-able vendor-abstraction layer** (D-020) — we do NOT build our own model | `docs/DECISIONS.md` D-020 | Solo team; keeps us able to plug in a better backend later |
| **Design Intelligence = our orchestration + curation + guided-experience logic** (the conductor: evaluate the room-*after* not the object; diagnose → thesis → intervention → compose → products) — NOT a trained model | `ai/DESIGN_INTELLIGENCE.md` | Makes the guided experience feel coherent & "intelligent" |
| **Surprising-yet-inevitable** as the quality/delight target | DESIGN_INTELLIGENCE, RETHINK-v5 | Reconciles delight + confidence |
| **Shop is the floor, designer is the front door — never a gate** (D-022); a session may end without a purchase | `docs/DECISIONS.md` D-022 | Reframes D-001/D-012; keeps D-002 (trust before sales) intact |
| **MVP boundary = Krok 1 (shop spine) + Krok 2 (advisor)** (D-030); the advisor is the MVP's only AI moment | `docs/DECISIONS.md` D-030, `docs/VISION.md` | Resolves "lean vs platform"; one external-AI dependency keeps it solo-buildable |
| **One Designer Flow; project type is a parameter** (D-023) — MVP = 2 types (empty wall / add-replace); input material + context are project-state fields | `docs/DECISIONS.md` D-023 | Prevents multiplying flows (the funded-team trap) |
| **Pool-level learning; no cross-session taste profile per customer** (D-024) — the KB is the advisory memory | `docs/DECISIONS.md` D-024 | Keeps the learning effect without breaking single-session or privacy |
| **Moat is a target mechanism, not a current asset** (D-025): Curated Catalog × Designer System × Outcome Data × Distribution | `docs/DECISIONS.md` D-025 | Prevents turning strategic aspiration into a false claim of advantage |
| **No visible confidence percentage** (D-026) — internal `readiness`, qualitative user-facing state naming the missing input | `docs/DECISIONS.md` D-026 | A percentage would be the "fake AI" we ruled out |
| **Distribution is part of the product** (D-027) — content and landing pages per design problem; no automatic publishing of customer data | `docs/DECISIONS.md` D-027 | The weakest factor in D-025 and business risk #1 |
| **Design outcome ≠ commercial outcome** (D-029) — acceptance measures the advisor, purchase measures the business | `docs/DECISIONS.md` D-029 | Purchase is too noisy to measure recommendation quality |

## 🟡 ACTIVE (evolving now — improve freely this milestone)
| Item | Where | Note |
|---|---|---|
| Research package / pilot (Studies A/B/C) | `experiments/pilot/`, `ai/RESEARCH_PACKAGE.md` | Being executed; expected to change |
| Room Diagnosis Schema (fields, confidence) | `ai/DESIGN_INTELLIGENCE-operational.md` | Refined by the pilot |
| Thesis Library (26 patterns) | DESIGN_INTELLIGENCE-operational | Prune / merge / add after Study A |
| Evaluation rubric (Stages A–D) | DESIGN_INTELLIGENCE-operational | Deliberately **unweighted** until data earns numbers |
| Candidate Generation Protocol | DESIGN_INTELLIGENCE-operational | Tunable |
| Product-blueprint details (cycle counts, timings) | docs/PRODUCT-BLUEPRINT | Directional numbers, not law |
| Prototypes / mockups / UX copy | `prototypes/` | Cosmetic layer |
| Catalogue & pricing | (private / TBD) | Not fixed |

## ⚪ NOT LOCKED — explicitly held as HYPOTHESES (do not treat as settled; corrections on record)
| Item | Status | Why not locked |
|---|---|---|
| `Resolution × Revelation` as *the* objective function | Hypothesis | Correction #1: used only as a reviewer question; the pilot tests it |
| "Taste Critic **alone** is the whole moat" | Superseded by D-025 | Correction #4: moat is plural. D-025 now settles the framing: `Curated Catalog × Designer System × Outcome Data × Distribution`, and states Latenca has **no moat yet** |
| **Pinterest as the long-term main channel** | Hypothesis | D-027 locks distribution-as-product but locks Pinterest only as the **first channel to test**; organic reach is neither free nor easy — D-028 tests it |
| Any numeric scoring weights | Not yet | Correction #2: no numbers until the study earns them |
| Bold-resolved > safe **for buyers** | Hypothesis | Study B tests it; business-critical falsifier if false |

## 🔵 BACKLOG (do not modify current architecture)
| Idea | Source | Gate to promote |
|---|---|---|
| Spatial "pro mode" for the ~5% (experts/hosts) | RETHINK-sequential-vs-spatial | Separate product decision |
| Persistent taste model / ambient ("Model E") | RETHINK-primitive-v3 | Only if the single-session constraint is revisited |
| Point-at-inspiration input | RETHINK-primitive-v2 | Companion input, post-core |
| Multiplayer / shared design | RETHINK-primitive-v2 | Post-core |
| Mirror / shelf / moulding / lighting as **sellable** (close the design-vs-sell gap) | DESIGN_INTELLIGENCE-operational | Supply expansion decision |
| Room-aware compositing (upload wall → analyze → composite art in perspective/light) | D-021 | Hard to do reliably; best-effort v2 only |
| AR real-room preview | PRODUCT-BLUEPRINT | Beyond v1 |
| **"Whole room" project type** (multi-wall coherence) | D-023 | After the MVP proves the single-wall promise |
| **Content personalization** ("use this image but change the flowers") via external image AI | D-030 | Only when a real content-editing feature exists — not before |
| **Open generation** (prompt-to-image for the customer) | D-030 | Not our role; we are not a generator |
| **Per-style / per-set landing pages** (merchandising layer) | D-027 | After per-problem pages are shown to work |
| **Automatic learning loop on outcome data** | D-024, D-029 | Needs volume — until then we only log |

---
*To change any row: add a `DECISIONS.md` entry (what moved, from→to, why), ideally via a PR. Promoting BACKLOG→ACTIVE/LOCKED or unlocking a LOCKED item is itself an architectural decision.*
