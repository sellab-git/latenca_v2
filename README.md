# Latenca

Single source of truth for Latenca — an AI **wall designer**: from one photo of your wall to a wall you love, in one session. This repo holds the product thinking, design intelligence, and experiments. Pre-launch; documents are **living**.

## Structure
```
/docs         — product bible & operating docs
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

Full rules: **`docs/REVIEW_WORKFLOW.md`** (roles, review output format, what the reviewer checks). Every doc/decision is **LOCKED / ACTIVE / BACKLOG** — authoritative registry in **`docs/LOCKS.md`**; the registry moves only through a `docs/DECISIONS.md` entry.

## Reading order (for a new reviewer)
1. `docs/PRODUCT_BIBLE.md` → 2. `docs/PRODUCT-BLUEPRINT-single-session.md` → 3. `ai/DESIGN_INTELLIGENCE.md` → 4. `ai/DESIGN_INTELLIGENCE-operational.md` → 5. `ai/RESEARCH_PACKAGE.md` → 6. `experiments/pilot/`. Background: `ai/exploration/` (how the model got here).

## ⚠️ Pre-push checklist (before this repo becomes public)
Intended to go **public without sensitive files**. Before creating/pushing the public remote:
- [ ] `/private/` is excluded (gitignored) and untracked.
- [ ] **Publish with a FRESH history** (single squashed commit of the current tree) so nothing sensitive from old history (e.g. `COSTS.md`) reaches GitHub.
- [ ] Review `knowledge/BUSINESS.md` and `knowledge/BENCHMARK.md` for confidential numbers before exposing.
- [ ] No API keys / tokens anywhere (the Gelato key has never been committed — keep it that way).
- [ ] Confirm public exposure is intended for each folder.

## Status
The product-experience architecture is locked (photo → bold opinion → react → land → buy, single session). Current focus: **validating the Design Intelligence** via `/experiments/pilot/`, then building. Nothing here is pushed yet.

---
*Working docs in English (product UI is English). Numbers marked verified vs assumed.*
