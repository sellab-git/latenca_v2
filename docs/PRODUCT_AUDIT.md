# Product Audit

System-level review of the whole product, **not tied to a commit.** Catches what commit/PR review structurally cannot: design drift, accumulated contradictions, roadmap divergence, terminology creep, moat erosion, hidden assumptions. Part of the workflow (`REVIEW_WORKFLOW.md`, review type 5).

## Who runs it
- **ChatGPT performs the audit** (independent — the author has blind spots).
- **Claude prepares the baseline** so the audit is grounded, not a cold re-read (see below).
- **Artur decides** on the findings.

## When it runs (triggers — not vague "periodically")
- **Milestone boundaries** — before/after the pilot; before build starts.
- **Cadence** — every ~2 weeks of active work, OR every ~10 significant commits.
- **On demand** — whenever Artur senses drift.

## Baseline Claude prepares before each audit
1. **Diff since last audit** — what changed (commits/decisions), in one page.
2. **Current LOCKS state** — LOCKED / ACTIVE / BACKLOG / HYPOTHESES snapshot.
3. **Open hypotheses** — and whether any drifted toward "decision."
4. **Roadmap + pilot status** — where we claim to be.

## Audit checklist (every audit answers all)
- **Architecture integrity** — are all LOCKED items (single-session · photo-first · opinion-first · sequential · closing-overview · Design-Intelligence-as-moat · surprising-yet-inevitable) still honored across the repo? Any silent violation?
- **Terminology consistency** — same concept, same name everywhere? Any drift / duplicate concepts / second system forming?
- **Roadmap alignment** — does current work match `ROADMAP.md` / `PROJECT_STATUS.md`? Divergence?
- **Moat evolution** — is the moat (Design Intelligence / taste / diagnosis / thesis generation / evaluation quality) getting stronger, or being diluted?
- **Pilot readiness** — is `experiments/pilot/` still coherent and runnable? Do the studies still test the intended hypotheses?
- **Hypothesis ledger** — has any HYPOTHESIS silently become a decision? Has any LOCKED silently become optional?
- **Accumulated inconsistencies** — contradictions between docs that individually passed review.
- **Design drift** — has the product quietly moved away from its stated identity (a designer, not a shop/recommender)?
- **Hidden assumptions** — new assumptions introduced without being named.

## Output format
```
Product Audit #<n>  ·  date  ·  baseline: <commit range>
Overall health: 🟢 solid / 🟡 drift forming / 🔴 architectural issues
Findings (each):
  - [🟢/🟡/🔴] <finding> · docs involved · required action (DECISIONS entry / LOCKS update / BACKLOG / fix)
Architectural conflicts (if any): <use the escalation format>
Hypotheses status: <any drifting toward decision?>
Recommendation: proceed / fix-before-next-milestone / needs Artur decision on <X>
```

## Resolution rule
The audit **reports; it does not redesign.** Every finding must resolve **explicitly** into a `DECISIONS.md` entry, a `LOCKS.md` update, a `BACKLOG` item, or a fix commit — **never silently.** Findings that propose architecture changes go through the normal decision gate (Artur).

## Audit log
| # | Date | Baseline | Overall health | Key findings | Resolutions |
|---|---|---|---|---|---|
| _(first audit: recommended right before the pilot launches)_ | | | | | |
