# Study A — Results Structure

IDs: Rooms R1–R6 · Proposals R{n}-P01..P08 · Reviewers E1–E5 · Classes INVALID/GENERIC/UNRESOLVED/BOLD/EXCEPTIONAL.
Fill after unblinding. **Do not invent success numbers beyond those in the research package.**

## Table 1 — Proposal-level (one row per proposal)
| Proposal | Room | Seeded class | E1 | E2 | E3 | E4 | E5 | Modal class | Class agree % | Mean rank | Median rank | Rank variance | % valid (Stage A) | % competent (Stage B) | Thesis legible % | % proud-to-sign | Sellability | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1-P01 | R1 | | | | | | | | | | | | | | | | | |
| … | | | | | | | | | | | | | | | | | | |

## Table 2 — Room-level (one row per room)
| Room | Problem type | Seeded class spread | Modal-class spread (reviewed) | Stage A agreement | Stage B agreement | Class agreement | Top-ranked proposal (modal) | Does top = a BOLD/EXCEPTIONAL? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R1 | blank-oversized | | | | | | | | |
| … | | | | | | | | | |

## Table 3 — Reviewer-level (one row per reviewer)
| Reviewer | Rooms scored | % Stage A "valid" | % Stage B "competent" | Class distribution given (INV/GEN/UNR/BOLD/EXC) | Avg confidence | Mean |rank vs group| (consistency) | Notes / tendencies |
|---|---|---|---|---|---|---|---|
| E1 | | | | | | | |

## Table 4 — Class confusion matrix (seeded × modal reviewed)
| Seeded ↓ / Reviewed → | INVALID | GENERIC | UNRESOLVED | BOLD | EXCEPTIONAL |
|---|---|---|---|---|---|
| INVALID | | | | | |
| GENERIC | | | | | |
| UNRESOLVED | | | | | |
| BOLD | | | | | |
| (EXCEPTIONAL is emergent — no seed row; count where it was assigned) | | | | | |

---

## How to calculate & interpret (definitions)
- **Stage A agreement** = share of proposals where all (or all-but-one) reviewers gave the same valid/invalid verdict. *Interpret:* should be **near-unanimous**. If not → physical-validity gates are miscalibrated (fix the gate definitions).
- **Stage B agreement** = same, for competent/not-competent. *Interpret:* expect a **strong majority**. Lower than A is acceptable.
- **Class agreement** = share of reviewers assigning the modal class per proposal. *Interpret:* expect high for INVALID/GENERIC, **lower toward BOLD/EXCEPTIONAL** — top-end disagreement is informative, not failure.
- **Rank consistency** = per proposal, spread of ranks across reviewers (variance) and per reviewer, mean absolute deviation from the group median rank. *Interpret:* low spread = reviewers see the same quality order.
- **Class confusion** = read Table 4. Strong diagonal = reviewers recover the seeded classes. Diffuse matrix = classes not distinguishable.
- **Thesis readability** = % of proposals for which a majority of reviewers wrote a legible one-sentence thesis. *Interpret:* BOLD/EXCEPTIONAL should have high readability; GENERIC low (no single idea).
- **Sign-off rate** = % proud-to-sign, by class. *Interpret:* should rise sharply from GENERIC → BOLD → EXCEPTIONAL.

## Framework success / failure (only the accepted thresholds)
**Success (all qualitative, per the research package):**
- Stage A near-unanimous.
- Stage B strong-majority.
- Reviewers rank **BOLD/EXCEPTIONAL above GENERIC consistently across rooms**, and the rubric's class assignments track reviewer consensus **better than a style-match baseline**.
- Proposals high on "solves the diagnosed problem + legible thesis + resolved room" are the ones reviewers independently rank top.

**Failure / falsification:**
- Stage A not near-unanimous.
- Confusion matrix diffuse (classes not recovered above chance).
- "Solves diagnosed problem" does **not** correlate with high rank.
- No agreement on EXCEPTIONAL even after the disagreement session.

*(Do not add numeric cut-offs beyond these.)*
