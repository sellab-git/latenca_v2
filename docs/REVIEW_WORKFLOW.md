# Review Workflow (Claude ↔ ChatGPT ↔ Artur)

Adopted 2026-07-19. This governs how changes are made and reviewed. It works like senior engineering code review, not two AIs designing in parallel.

## Roles
- **Claude — Author/Editor.** Writes, integrates, documents, evolves the product. Owns the repo and the `docs/LOCKS.md` registry.
- **ChatGPT — Senior Reviewer.** Product / Architecture / Decision / Design-Intelligence reviewer. Reviews changes; does **not** rewrite the project or introduce new frameworks unrequested.
- **Artur — Decider.** Accepts / revises / pivots. Only Artur (via an explicit decision) changes a LOCKED item.

## Source of truth
`sellab-git/latenca_v2` (public) is the **only** source of truth. Repository state always wins over any pasted summary. Reviews are against the current repo, not chat history.

## Review philosophy
Review changes, don't rewrite. **Existing decisions remain valid unless the current change explicitly replaces them.** New ideas are BACKLOG candidates unless required to resolve a contradiction. No restarting closed discussions.

## Making a change (author flow)
- **Trivial / ACTIVE-doc edits** → straight to `main`, commit with a clear message.
- **Significant change** (touches a LOCKED item, changes the moat, or an architectural decision) → **branch + PR** (`gh pr create`) so it can be reviewed as "PR #n" before merge.
- Any change to a **LOCKED** item must add an entry to `docs/DECISIONS.md` stating what changed and why.

## Review request types (Artur → ChatGPT)
`Review commit <hash>` · `Review PR #<n>` · `Review <FILE>.md` · `Review PRODUCT_BIBLE consistency` · `Does this contradict AI_SYSTEM?` · `Does this change the moat?` · `Is this experiment actually falsifying the hypothesis?`

## Review output format (ChatGPT) — concise, structured, no essays unless asked
```
Verdict: APPROVE / APPROVE WITH CHANGES / REQUEST CHANGES
Consistency: ✔ consistent / ⚠ breaks previous assumption / ❌ contradicts existing decision
Architecture: <preserves single-session / photo-first / opinion-first / sequential / closing-overview? or intentional change?>
Moat: <strengthens / weakens / neutral — which of: Design Intelligence, taste, diagnosis, thesis generation, evaluation quality>
Risks:
Questions:
Recommendation:
```

## What the reviewer actively checks
1. **Consistency** with PRODUCT_BIBLE · AI_SYSTEM · DESIGN_INTELLIGENCE · DECISIONS · PRODUCT-BLUEPRINT.
2. **Architectural integrity** — preserves single-session · photo-first · opinion-first · sequential · closing overview. If not: is the change *intentionally* architectural (LOCKED → needs a decision)?
3. **Moat** — does it strengthen or weaken Design Intelligence / taste / diagnosis / thesis generation / evaluation quality?
4. **Experimental validity** — does a research change actually test the intended hypothesis, or accidentally measure something else?
5. **Scope creep** — flag unnecessary complexity, a second system, duplicated concepts, or unmotivated terminology changes.

## What the reviewer will NOT do
Redesign accepted architecture · introduce alternative frameworks unrequested · replace decisions with preferences · restart closed discussions.

## Architectural Lock Levels (the deterministic layer)
Every document/decision is **LOCKED**, **ACTIVE**, or **BACKLOG** — the authoritative registry is **`docs/LOCKS.md`**.
- **LOCKED** — changing requires an explicit architectural decision (+ a `DECISIONS.md` entry). A reviewer treats a LOCKED-violating change as REQUEST CHANGES unless it's flagged as an intentional architecture change.
- **ACTIVE** — currently evolving in this milestone; improve freely.
- **BACKLOG** — interesting ideas that must **not** modify current architecture.
This lets a reviewer instantly tell apart a **bug**, an **architectural change**, and a **future idea** — reducing design churn.

**Author refinement to the rule:** a change that *promotes* a BACKLOG idea into ACTIVE/LOCKED, or *unlocks* a LOCKED item, is itself an architectural decision — it requires a `DECISIONS.md` entry and (ideally) a PR. The registry moves only through decisions, never silently.
