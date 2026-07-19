# DECISIONS

This document contains every accepted product decision. It is part of the Product Bible.

## How to use this file

- **One entry per decision.** Big / expensive / hard-to-reverse decisions get: Decision, Context, Reason, Alternatives (optional), Implications. Small decisions can be a single line.
- **Status is light.** Default = the decision is active. Add `Superseded by D-0XX — <one line>` when a decision is replaced. `REVIEW` means the founder wants to revisit it.
- **Never delete a decision.** History is preserved by marking it superseded, so the reasoning stays visible later.

---

# D-001
## Title
Latency is an AI Wall Designer.
### Status
LOCKED — see D-012 and the "product framing to reconcile" open question in PROJECT_STATUS (may be softened/superseded pending founder decision).
### Reason
The core product is helping users make confident wall decoration decisions rather than operating as a traditional ecommerce catalog.

---

# D-002
## Title
Trust before sales.
### Status
LOCKED
### Reason
Long-term customer trust is more valuable than maximizing short-term revenue.

---

# D-003
## Title
Recommendations before catalog.
### Status
LOCKED
### Reason
Users struggle with decisions, not with finding more products.

---

# D-004
## Title
AI behaves like a designer.
### Status
LOCKED
### Reason
The assistant should advise, explain and educate instead of selling.

---

# D-005
## Title
Mobile-first product.
### Status
LOCKED
### Reason
Most users will discover and purchase using their phones.

---

# D-006
## Title
Wall projects are first-class objects.
### Status
LOCKED
### Reason
The primary outcome is a complete wall composition, not a single artwork.

---

# D-007
## Title
Support both browsing and AI.
### Status
LOCKED
### Reason
Some users prefer traditional shopping while others want AI guidance.

---

# D-008
## Title
Community projects become inspiration.
### Status
REVIEW
### Reason
Public wall compositions may become an important discovery mechanism, but validation is required.

---

# D-009
## Title
Development workflow is a 3-layer, tool-agnostic model.
### Status
Accepted (2026-07-18)
### Decision
The repo is the single source of truth, structured in three layers: **Bible** (durable truth), **PROJECT_STATUS.md** (current state, one file), **chats** (thinking — only conclusions land in the repo). Roles: founder = Editor-in-Chief; ChatGPT = external sparring partner (no repo access, no implementation); Claude = maintains repo + implements + proposes, never changes accepted decisions without approval. Full detail in `WORKFLOW.md`.
### Reason
Earlier proposals (a proposal-workflow with automated cross-model review) were over-engineered for a solo founder pre-MVP. This model gives ~90% of the value with nothing to build or maintain.
### Alternatives
Proposal Workflow + automated Product Review between models (rejected: ChatGPT can't read the repo, cross-vendor auto-review is a brittle meta-product); separate ADR files (deferred: one `DECISIONS.md` is enough until it grows).
### Implications
No orchestration, API, or webhooks. The only manual step is the founder recording a decision.

---

# D-010
## Title
Build the product directly — no separate up-front market-validation test.
### Status
Accepted (2026-07-18) — founder decision
### Decision
Proceed to build v1 rather than first running a market/discovery test (e.g. an Etsy demand test).
### Context
Research showed the real business risk is discovery / traffic, and suggested a cheap validation-first test. The founder chose to build the product and validate through building.
### Implications
Discovery/traffic must be addressed early in the build (Pinterest anchor, content-as-factory), not deferred.

---

# D-011
## Title
Catalog is source-agnostic; v1 art comes from public-domain (CC0) + AI-generated (hybrid).
### Status
Accepted (2026-07-18)
### Decision
The catalog data model is source-agnostic (every product tagged with a `source` and a `collection`). v1 is filled from **museum public-domain / CC0 APIs** (Art Institute of Chicago, Met, etc.) and **AI-generated** art. A **creator marketplace is deferred to phase 2**.
### Context
Legal research (with license quotes): free stock sites (Unsplash/Pexels/Pixabay) **prohibit selling their images as prints** — unusable. Museum CC0 art is legal to sell, free, and print-resolution. AI-generated art is legal to sell but needs upscaling and has no copyright moat.
### Reason
Fills a legal, print-ready catalog immediately, with no artist cold-start and no licensing risk.
### Alternatives
Creator marketplace first (rejected: chicken-and-egg — creators won't upload to a shop with no buyers); free stock APIs (rejected: illegal to sell as prints).
### Implications
Data model needs `source` + `collection` from day one. Public-domain requires curation filters (resolution ≥3000px, sane aspect ratio, paintings-only to avoid paper-edge scans). If AI: marketing leads with real-room photos (platforms suppress bulk AI decor imagery).

---

# D-012
## Title
The AI Wall Designer is one purchase path within a curated shop — build the shop first.
### Status
Accepted (2026-07-18) — working plan; reframes D-001 (see PROJECT_STATUS open question)
### Decision
The product is a curated wall-art shop with three entry paths (AI Designer / Browse / Get Inspired). Build the shop spine first (catalog → product page → cart → checkout); the AI Wall Designer flow is v2, built on top.
### Reason
The AI designer recommends and sells products, so it needs a working shop underneath it. It is the heart of the vision but the most expensive and least-validated thing to build — so it is not the first build.
### Implications
v1 build order = skeleton + design system → catalog → cart/checkout → (v2) AI Designer.
### Revision (2026-07-18)
The AI-guided journey is the **hero experience**, not merely one path deferred to v2. Per the `SCREEN_01_HOME` brief, the home is "the beginning of an AI-guided design experience… closer to ChatGPT than to Etsy," not a shop landing. The catalog/cart remain the substrate underneath, but the flagship we build and show is the AI journey (mobile-first). A conventional shop/browse still exists as a secondary path.

---

# D-013
## Title
v1 tech stack + repo structure: Next.js app in `web/`, source-agnostic catalog.
### Status
Accepted (2026-07-18)
### Decision
The product is built as a Next.js 16 (React 19, Tailwind 4, TypeScript) app in the `web/` subfolder of this repo; the Bible/docs stay at the repo root. The catalog is source-agnostic (each product has `source` + `collection`), seeded for v1 with the public-domain museum artworks. Planned services, added when needed: Supabase (data), Stripe + Apple/Google Pay (payments), Gelato (print fulfillment).
### Reason
Matches the standard stack across the founder's projects; a subfolder keeps app and docs cleanly separated in one repo; the source-agnostic catalog lets public-domain, AI-generated, and creator art coexist without a rewrite.
### Implications
Prices kept in minor units via a central `formatPrice()` (no hardcoded currency). Museum images use a plain `<img>` — their Cloudflare CDN blocks the Next image optimizer's server-side fetch — to be swapped for `next/image` once art moves to our own CDN.

---

# D-014
## Title
Product UI language is English; code is i18n-ready.
### Status
Accepted (2026-07-18)
### Decision
All product UI text is English (global market). The system is built translation-ready: UI strings live in `web/src/messages/en.ts` (never hardcoded in components), and locale/currency formatting goes through `web/src/lib/locale.ts` (`DEFAULT_LOCALE`, `formatCurrency`). Adding a language later = a sibling messages file + a locale switch, with no component changes.
### Implications
Never hardcode UI copy, currency symbols, or locale in components.

---

# D-015
## Title
Brand name is "Latenca" (not "Latency").
### Status
Accepted (2026-07-18)
### Reason
Confirmed by founder. Some mockups render the wordmark as "LATENCY"; the correct brand is "Latenca" (matches the domain and repo). Use "LATENCA" everywhere.

---

# D-016
## Title
Spec-driven UX/UI workflow: `/design` specs → Stitch → code.
### Status
Accepted (2026-07-18)
### Decision
UX/UI is developed from written **product/screen specs**, not ad-hoc prompts. Source of truth = `/design/` (`DESIGN_PRINCIPLES.md` + one `SCREEN_XX_*.md` per screen). Roles: founder = Product Designer / UX Lead / Creative Director (writes specs, reviews); Stitch = UI/visual designer (generates UI from specs, operated by Claude); Claude = frontend engineer (implements in code). `UX_UI.md` is folded into `design/DESIGN_PRINCIPLES.md`.
### Reason
Specs are the durable artifact both Stitch and code work from; swapping images doesn't scale. A shared design system (Stitch project `Latenca_v1` ↔ coded `@theme` tokens) prevents design↔code drift.
### Implications
Reviews critique substance (hierarchy, CTA strength, AI visibility), not "nice". Keep Stitch and code tokens in sync.

---

# D-017
## Title
Merge projects 15 + 17 into a new project (folder `18. Latenca`); 17 governs strategy, 15 governs craft.
## Status
Accepted (2026-07-19) — founder decision
## Decision
A new project is created in `C:\AI biznes\18. Latenca` that merges the two prior Latenca efforts. Project **17** (this repo, `sellab-git/latenca`) contributes the STRATEGY: the AI-advisor concept, the wall/set as the core object, the source-agnostic catalog seeded from museum public-domain (CC0) + operator-curated AI, and the governance/Bible + decision log. Project **15** (`sellab-git/latenca_v1`, the mature static prototype) contributes the CRAFT: the design system, the data model (artwork ≠ product ≠ order), the gross-up pricing formula, the mobile step-flow thinking, and the "customization on rails" concept. **Conflict rule: where 15 and 17 disagree, 17's strategy wins; 15 supplies execution.** Full reconciliation in `SPEC.md`.
## Context
Two projects grew independently and reached the same hard conclusions (discovery is the bottleneck; CAC ~$55–120 vs ~$40 profit; curation is the moat; sets/walls are the only economics that work). 15 is polished UI but framed as a marketplace/catalog; 17 is the concept + a real but bare Next.js app whose from-scratch UI was weak. Neither alone is the product.
## Reason
15 has the design quality and reusable machinery; 17 has the concept, governance, and strategic decisions. Merging keeps both strengths instead of rebuilding either.
## Implications
- **Sources are frozen:** nothing in `15. Latenca` or `17. Latenca` is modified — only read/copied into `18`.
- **Advisor + wall = ONE product:** the AI advisor is the guided layer on a mobile step-flow that produces a wall; browse is the alternative path; both land in the wall/set. Not two products stitched.
- **Catalog v1 = museum CC0 + operator-curated AI** (per D-011). Creator marketplace deferred to phase 2; artist exists now only as **attribution** (browse-by-author), but the data-model seam (ARTIST as first-class entity, moderation gate) is built early.
- **The 15 "wall builder" is a discarded attempt** — the wall experience is redesigned from scratch under the advisor/purchase flow, mobile-first (no drag canvas).
- **Medium = HTML mockups, mobile-first (390px up), now.** Next.js + backend = a later phase, only after the flow and design are locked (revises 15's and 17's build-first framing to design-first-in-mockups).
- Fresh git repo, unconnected to the old remotes; a new GitHub repo only on explicit approval (name TBD — `latenca` is taken).

---

# Decision Template

## ID
D-XXX
## Title
...
## Status
Accepted | REVIEW | Superseded by D-XXX
## Date
YYYY-MM-DD
## Decision
What was decided.
## Context
Why this decision exists (the situation, any benchmark/research).
## Reason
Why this option over the others.
## Alternatives
What else was considered and why it was rejected. (optional)
## Implications
What this changes for product / architecture / UX.

---

# D-018
## Title
Repo `sellab-git/latenca_v2` is the single source of truth; adopt the review workflow + Architectural Lock Levels.
### Status
LOCKED
### Reason
Public repo (private/ excluded) so reviews run against current files, not chat summaries. Roles: Claude = author/editor, ChatGPT = senior reviewer, Artur = decider. Every doc/decision is LOCKED / ACTIVE / BACKLOG per `docs/LOCKS.md`; the registry moves only through a DECISIONS entry. See `docs/REVIEW_WORKFLOW.md`.
### Implications
LOCKED items change only via an explicit decision (+ ideally a PR). Promoting BACKLOG→ACTIVE/LOCKED or unlocking is itself a decision. R×R objective and "Taste Critic = whole moat" remain HYPOTHESES (not locked), per earlier corrections.
