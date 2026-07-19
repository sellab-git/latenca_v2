# WORKFLOW — How this project is developed

> **One line:** The Bible says *what is true*. PROJECT_STATUS says *where we are*. Chats are *how we got there* — only the conclusions land in the repo.

This project is developed by a **solo founder** working with two AI models. The models are interchangeable **tools**. We are **not** building a system for the models to talk to each other. We are building a durable **product-development workflow**. The Git repository is the single source of truth.

---

## The three layers

### 1. Product Bible — durable truth ("what is true")
The small set of documents describing what is *currently true* about the product. No brainstorming, no chat history — only conclusions.

Bible files: `README`, `DECISIONS`, `AI_SYSTEM`, `UX_UI`, `USER_RESEARCH`, `PRODUCT_ARCHITECTURE`, `ROADMAP`, `BUSINESS`.

Keep the number of documents as small as possible. (`WALL_DESIGN_KNOWLEDGE` is a supporting reference note — future interior-design knowledge for the AI Designer — not core Bible.)

### 2. PROJECT_STATUS.md — current state ("where we are")
**One single file.** Current sprint, focus, active tasks, open questions, active hypotheses, risks, next steps. Overwritten freely. **There is never a second file describing project state.**

### 3. Chats — the thinking ("how we got there")
Conversations are a thinking *process*, not documentation. They stay in the chat. **Only conclusions enter the repo.**

---

## Roles

### Founder — Editor-in-Chief
Makes the decisions. Does **not** copy chat history between models. Does **not** sync the models — only syncs the repo (the Bible).

### ChatGPT — external sparring partner
For strategy, benchmarks, UX, AI behavior, and critique of ideas. **Not** part of the pipeline. Does **not** update the repo. Does **not** implement.

### Claude Code — works directly in the repo
Maintains the Bible, implements code, owns technical architecture, keeps the repo consistent. **May propose** better solutions. **Never changes an accepted decision without the founder's approval.**

---

## The operating loop (a typical piece of work)

1. **Start a ChatGPT session** → founder pastes `PROJECT_STATUS.md` (and any relevant Bible doc) so ChatGPT knows the current state.
2. ChatGPT helps reach a decision, or critiques an idea.
3. **Founder decides.**
4. Founder tells Claude the decision (or pastes ChatGPT's conclusion).
5. **Claude records it** in `DECISIONS.md`, updates `PROJECT_STATUS.md`, and implements / updates docs + code.
6. Claude reads `PROJECT_STATUS.md` **first** at the start of every session.
7. **End of a work session** → Claude updates `PROJECT_STATUS.md`, so the next session (any model) starts from the truth.

The founder never has to be a "relay." One decision = one short note. That is the only manual step, and it is the founder's real job.

---

## DECISIONS.md conventions

- One entry per decision. **Big / expensive / hard-to-reverse** decisions get: Decision, Context, Reason, Alternatives (optional), Implications. **Small** decisions can be one line.
- **Status is light.** Default = the decision is active. Use `Superseded by D-0XX — <one line>` when it is replaced.
- **Never delete a decision.** History is preserved by marking it superseded, so future-you sees the reasoning.

---

## The one rule that keeps everyone in sync

Every accepted decision lands in `DECISIONS.md` (with enough context to survive months later), and every session ends with `PROJECT_STATUS.md` updated. That discipline — not any tooling — is what keeps the founder, ChatGPT, and Claude from drifting.

## How it scales (years, not weeks)

When the project grows, you swap the *storage*, not the *model*: `DECISIONS.md` → separate ADR files; `PROJECT_STATUS.md` → an issue tracker (Linear / GitHub Issues); the Bible → a docs site. The shape stays identical.
