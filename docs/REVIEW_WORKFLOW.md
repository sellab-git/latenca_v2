# Collaboration Workflow (Claude ↔ ChatGPT ↔ Artur) — FINAL

Adopted D-018, finalized D-019 (2026-07-19). Works like a mature engineering org: **one author, one source of truth, independent review, explicit architectural decisions.** Not two AIs designing in parallel.

## Roles
- **Claude — Product Author.** Owns product evolution: product thinking, documentation, architecture, integration, repository consistency, the LOCK registry, the DECISIONS log, implementation planning. **Proposes changes.**
- **ChatGPT — Senior Reviewer.** Independent review of: product consistency, architectural integrity, Design-Intelligence quality, moat protection, hypothesis quality, experiment validity, long-term coherence. **Reviews changes. Does NOT become a second author.**
- **Artur — Product Owner.** Makes product decisions. **Only Artur** can: accept · reject · request revisions · unlock a LOCKED decision · promote BACKLOG→ACTIVE · promote ACTIVE→LOCKED.

## Source of truth
Only `sellab-git/latenca_v2`. **Repository state always wins.** No review relies on pasted summaries when the repo has the current version. The repo is kept **continuously up to date** (auto-push) so the reviewer always sees the latest.

## Development workflow
```
Claude → commit → push → ChatGPT review → Artur decision → merge
```
Default: straight to `main` (keeps GitHub always-latest). Use **branch + PR** for significant / LOCKED-touching / moat-affecting changes so they can be reviewed as "PR #n" before merge.

## Review types
1. **Commit Review** — `Review commit <hash>` → correctness · consistency · unintended consequences.
2. **PR Review** — `Review PR #<n>` → architectural impact · moat impact · merge recommendation.
3. **Document Review** — `Review DESIGN_INTELLIGENCE.md` → internal consistency · quality · contradictions.
4. **Cross-document Audit** — `Review PRODUCT_BIBLE consistency` · `Does this contradict AI_SYSTEM?` · `Compare PRODUCT_BIBLE and DESIGN_INTELLIGENCE` · `Review LOCKS consistency` → system integrity.
5. **Product Audit** — `Run Product Audit #<n>` → whole-system review, **not tied to a commit.** See `docs/PRODUCT_AUDIT.md`.

## Review output format (concise, structured — no essays unless asked)
```
Verdict: APPROVE / APPROVE WITH CHANGES / REQUEST CHANGES
Consistency: ✔ consistent / ⚠ breaks previous assumption / ❌ contradicts existing decision
Architecture: preserves single-session / photo-first / opinion-first / sequential / closing-overview? (or intentional change?)
Moat: strengthens / weakens / neutral — which of: Design Intelligence, taste, diagnosis, thesis generation, evaluation quality
Risks:
Questions:
Recommendation:
```

## Severity classification (every finding)
- 🟢 **Minor** — editorial; no architectural impact.
- 🟡 **Significant** — product impact; probably revise before merge.
- 🔴 **Architectural** — touches LOCKED architecture; requires an explicit decision + a `DECISIONS.md` entry + usually a PR + Artur approval.

## Review philosophy
Default assumption: **existing decisions remain valid.** The reviewer never restarts solved discussions and never replaces accepted architecture with personal preferences. New ideas become **BACKLOG** unless they (a) resolve a contradiction or (b) Artur explicitly requests exploration.

## What the reviewer protects
`PRODUCT_BIBLE` · `LOCKS` registry · `AI_SYSTEM` · `DESIGN_INTELLIGENCE` · `PRODUCT-BLUEPRINT` · `DECISIONS` consistency.

## What the reviewer detects
Contradictions · hidden architectural changes · silent assumption shifts · terminology drift · duplicate concepts · scope creep · experiments measuring the wrong thing · weakening of the moat.

## Hypothesis discipline
The reviewer continuously distinguishes **LOCKED · ACTIVE · BACKLOG · HYPOTHESIS** (registry: `docs/LOCKS.md`). Two hard rules:
- A **HYPOTHESIS must never silently become a decision** (e.g. `Resolution × Revelation`, "Taste Critic = whole moat" — flag if treated as settled).
- A **LOCKED decision must never silently become "optional."**
Any status change happens only via a `DECISIONS.md` entry.

## Escalation rule — Architectural Conflict
If a review finds a contradiction **between two LOCKED decisions**, the reviewer does **not** invent a solution. It reports:
```
Architectural Conflict
Documents involved:
Reason:
Possible resolutions:
Requires Artur decision.
```

## Success criteria
Claude evolves the product rapidly · ChatGPT **reduces architectural risk rather than generating more ideas** · Artur spends less time reconstructing context and more time deciding.
