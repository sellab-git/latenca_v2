# Latenca

Single source of truth for Latenca — an AI **wall designer**: from one photo of your wall to a wall you love, in one session. This repo holds the product thinking, design intelligence, and experiments. Pre-launch; documents are **living**.

## Structure
```
/docs         — product bible & operating docs
   VISION.md                             (START HERE — strategic overview: what & why)
   REVIEW-designer-layer.md              (review of the "digital interior designer" hypotheses)
   PRODUCT_BIBLE.md · DECISIONS.md · ROADMAP.md · PROJECT_STATUS.md
   WORKFLOW.md · SCREEN_MAP.md · PRODUCT_ARCHITECTURE.md
   PRODUCT-BLUEPRINT-single-session.md   (the single-session product spec)
/knowledge    — external / market / user knowledge
   WALL_DESIGN_KNOWLEDGE.md · USER_RESEARCH.md · BENCHMARK.md · BUSINESS.md · market-map.html
/ai           — the intelligence (the moat)
   AI_SYSTEM.md
   DESIGN_INTELLIGENCE.md             (the framework / evaluation function)
   DESIGN_INTELLIGENCE-operational.md (schema, thesis library, rubric, generation)
   RESEARCH_PACKAGE.md                (the 3-study validation plan)
   /exploration                       (RETHINK-*: the reasoning trail that led here)
/experiments/pilot   — the executable validation pilot
   RESEARCH-pilot-master-checklist.md · RESEARCH-pilot-decision-report-template.md
   /StudyA  (expert design evaluation)   /StudyB  (homeowner purchase)   /StudyC  (wizard-of-oz)
/prototypes   — mockups, design system, review screenshots
/reference    — source material (project 15 prototype HTML, project 17 mockups/specs)
/Analizy      — competitor benchmarks (Fy! · Mixtiles · Ideogram · Displate)
               patterns only — we never copy code, text, graphics, branding or licensed IP
/private      — commercially sensitive (NOT public: real costs/pricing)   [gitignored]
```

## How we work (decision review, like code review)
```
Claude drafts → commit → GitHub → ChatGPT reviews → accept → merge
```
Instead of "what do you think?", the loop becomes **"review commit <hash>"** / **"review PR #<n>"**.
- **Claude** works on the local repo and commits meaningful changes.
- **ChatGPT** reviews the current version in the repo (not summaries) and flags: consistent / breaks an earlier assumption / contradicts `AI_SYSTEM` / experiment doesn't falsify the hypothesis / this commit changes the moat.
- **Artur** decides accept / revise / pivot.

Full rules: **`docs/REVIEW_WORKFLOW.md`** (roles, 5 review types, severity 🟢🟡🔴, escalation). Whole-system reviews: **`docs/PRODUCT_AUDIT.md`**. Every doc/decision is **LOCKED / ACTIVE / BACKLOG / HYPOTHESIS** — authoritative registry in **`docs/LOCKS.md`**; status moves only through a `docs/DECISIONS.md` entry.

## Reading order (for a new reviewer)
1. **`docs/VISION.md`** (what & why, the phased ladder, the MVP boundary) → 2. `docs/REVIEW-designer-layer.md` (latest open questions) → 3. `docs/DECISIONS.md` + `docs/LOCKS.md` (what is settled) → 4. `docs/PRODUCT_BIBLE.md` (full spec) → 5. `docs/PRODUCT-BLUEPRINT-single-session.md` → 6. `ai/DESIGN_INTELLIGENCE.md` + `-operational.md` → 7. `ai/RESEARCH_PACKAGE.md` → 8. `experiments/pilot/`.
Context: `Analizy/` (competitor benchmarks). Background: `ai/exploration/` (how the thinking got here).

## ⚠️ Publishing rules (this repo IS public)
Published with a fresh, squashed history so nothing sensitive from earlier history reached GitHub. Standing rules:
- `/private/` stays gitignored and untracked (real costs/pricing).
- **No API keys / tokens, ever** (the Gelato key has never been committed — keep it that way).
- Check `knowledge/BUSINESS.md` and `knowledge/BENCHMARK.md` before adding confidential numbers.
- **Settled (2026-07-20):** the real Gelato unit costs in `docs/PRODUCT_BIBLE.md` stay public. They are already in the pushed history, and Gelato's pricing is semi-public anyway — anyone can open an account and see it. `private/` still holds the full cost/margin scenarios; don't re-raise this.
- Anything added here is public the moment it is pushed — assume no take-backs.

## Status
Working direction: a **curated shop with one AI moment** — the shop is the floor, the designer is the front door and never a gate (see `VISION.md` §6 and `REVIEW-designer-layer.md` §D). MVP = shop spine (Krok 1) + advisor (Krok 2); content personalization, open generation, room-photo compositing and the creator marketplace are later rungs. Locked constraints: D-020 (we orchestrate external AI, no own model) and D-021 (neutral wall, room photo optional). **Primary business risk remains distribution / CAC, not product.**

---
*Working docs in English (product UI is English). Numbers marked verified vs assumed.*
