# Architectural Lock Registry

Authoritative status of every major decision. See `REVIEW_WORKFLOW.md` for how this is used. The registry moves **only** through a `DECISIONS.md` entry — never silently.

Legend: **LOCKED** = change needs an explicit architectural decision · **ACTIVE** = evolving this milestone · **BACKLOG** = must not modify current architecture.

## 🔒 LOCKED (architecture — do not change without a decision)
| Item | Where it lives | Locked because |
|---|---|---|
| **Single-session product** (~90% use once; value must land in one 10–15 min session; no dependence on long-term personalization) | `ai/exploration/RETHINK-the-primitive-v4-single-session.md`, `docs/PRODUCT-BLUEPRINT-single-session.md` | Defines the whole optimization target |
| **Photo-first** (a wall photo is the entry and the taste seed; ~80% inferred from it) | PRODUCT-BLUEPRINT | Removes the questionnaire; enables the wow + the close |
| **Opinion-first** (AI leads with a bold, complete design; understanding emerges from reactions; no interrogation, no unsolicited explanation) | `ai/exploration/RETHINK-the-primitive-v5-opinion-first.md`, `ai/AI_SYSTEM.md` | The core interaction stance |
| **React-don't-specify** (user reacts to complete proposals; taste is recognized, not described) | RETHINK-primitive series | The primitive |
| **Sequential interaction** (one bold proposal at a time; NOT spatial navigation) | `ai/exploration/RETHINK-sequential-vs-spatial.md` | Forced by "taste is recognized, not described" + single-session |
| **Closing overview** ("the range I explored" collapsing to the chosen wall, at the landing) | RETHINK-sequential-vs-spatial | The one borrowed spatial benefit (no-regret) |
| **Design Intelligence is the moat — as a direction** (evaluate the room-*after* not the object; diagnose → thesis → intervention → compose → products) | `ai/DESIGN_INTELLIGENCE.md` | The thing that makes one AI exceptional vs average |
| **Surprising-yet-inevitable** as the quality/delight target | DESIGN_INTELLIGENCE, RETHINK-v5 | Reconciles delight + confidence |

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
| "Taste Critic **alone** is the whole moat" | Hypothesis | Correction #4: moat is plural (diagnosis discipline, curated supply, render fidelity, the pilot dataset, taste critic) |
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
| AR real-room preview | PRODUCT-BLUEPRINT | Beyond v1 |

---
*To change any row: add a `DECISIONS.md` entry (what moved, from→to, why), ideally via a PR. Promoting BACKLOG→ACTIVE/LOCKED or unlocking a LOCKED item is itself an architectural decision.*
