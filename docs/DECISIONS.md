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
**Superseded by D-032 (2026-07-20)** — the Stitch step was never used in practice and `/design/` does not exist in this repo. The *screen briefs* this decision introduced remain valuable and are still cited (see D-012's revision); only the tooling and folder layout are replaced.
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

---

# D-019
## Title
Finalize the collaboration workflow (adds Product Audits + severity levels + escalation rule).
### Status
LOCKED
### Reason
Mature-org model: one author (Claude), independent reviewer (ChatGPT, not a second author), decider (Artur). Extends D-018 with: 5 review types incl. periodic **Product Audit** (whole-system, not commit-tied; run by ChatGPT on a Claude-prepared baseline; triggered at milestones / ~2wk / ~10 commits / on-demand), severity 🟢🟡🔴, hypothesis discipline (HYPOTHESIS must never silently become a decision; LOCKED must never silently become optional), and the Architectural-Conflict escalation rule (reviewer reports, never invents). See `docs/REVIEW_WORKFLOW.md` + `docs/PRODUCT_AUDIT.md`.
### Implications
Audits report, they do not redesign — findings resolve explicitly into DECISIONS / LOCKS / BACKLOG / fix. Supersedes nothing; extends D-018.

---

# D-020
## Title
Latenca is an intelligent FRONT that orchestrates external AI — we do not build our own model.
### Status
LOCKED
### Reason
The team is one person + AI assistants. We orchestrate existing external models/generators (vision, image generation, LLM) kept **behind a vendor-abstraction layer** so any backend can be swapped for a better/newer one later ("wypiąć i wpiąć coś mądrzejszego"). The product IS the customer-facing experience: an "intelligent" designer/assistant that coherently guides the user through choosing and buying — one graphic, several, a composition, or a whole wall. Our "Design Intelligence" = the orchestration + curation + guided-experience logic (the conductor), NOT a trained model (the orchestra is rented).
### Implications
- **Moat is honestly relocated:** NOT a proprietary model. It is execution / experience quality / curation / brand / being genuinely good first. (Corrects the earlier "Design Intelligence as *the* moat" — the model is a commodity we rent.)
- **Vendor-abstraction is architectural:** every external model is a replaceable component behind our own interface (extends the Gelato/AI-model/CDN vendor-boundary principle).
- **Validation shifts:** we can run a REAL feasibility spike with existing tools now (does today's off-the-shelf stack produce good-enough guided output?), not only a human-faked Wizard-of-Oz.
- **Distribution/CAC remains the primary business risk** — unchanged by this decision.
- A trained "Taste Critic" as a moat drops from ambition to a far-future BACKLOG idea.

---

# D-021
## Title
Mixtiles-style: compose from the catalog on a neutral/sample wall. Customer room photo is optional & best-effort, not the core. Room-aware compositing drops from v1.
### Status
LOCKED
### Reason
~80% of customers won't upload a room photo, and photo-based compositing (perspective/scale/light on often-poor photos) is hard to do well — when it fails it looks bad and destroys trust, which is the whole product. So "Design my wall" = the assistant composes a great wall (single / pair / gallery) from available catalog art, dynamically sized and proportioned, shown on a clean or sample-room wall (the Mixtiles pattern), driven by a few light parameters (room type, vibe, wall size/shape, number of pieces). Simpler, reliable, solo-buildable on existing tools; no CV/perspective/relighting.
### Implications
- **Downgrades "photo-first" (was LOCKED):** default is a neutral/sample wall; optional "preview on your wall" becomes a best-effort v2 nice-to-have, not the foundation.
- **Room Diagnosis Schema shrinks** from photo analysis to a few light parameters.
- `ai/DESIGN_INTELLIGENCE.md` and `docs/PRODUCT-BLUEPRINT-single-session.md` need simplification to match (their photo-centric parts) — flagged, not yet rewritten.
- Differentiation narrows to composition-intelligence + curation + art selection; **distribution/CAC remains the primary risk** (unchanged).
- **Room-aware compositing → BACKLOG.**

---

# D-022
## Title
Product shape: the shop is the floor, the designer is the front door — never a gate.
### Status
LOCKED
### Decision
Latenca is a curated shop with one AI moment. The **shop is the floor** (catalog, product page, configurator, cart) — it always exists and every path lands in it. The **designer is the front door and the face of the brand** — the hero of the home page and the differentiator. **Decisive rule: the designer is never a gate** — it can always be skipped and bought around. In navigation this is one product, not two equals: the fast path (*Browse and buy*) and the guided path (*Design my wall*) end in the same catalog, PDP and checkout.
### Reason
The brand promise is confidence in the decision, but most people buying wall art are not running a "project" — turning a purchase into a mandatory consultation would kill conversion. The verified Modsy case (~250 human designers, whole rooms, a model that did not scale) shows the danger is *human cost per project*, not the advisory layer itself.
### Implications
Reframes D-001 and D-012 and closes the open product-framing question in PROJECT_STATUS. Every designer recommendation is built from products available in the Latenca catalog and leads to a **buyable composition**; we do not build a separate consulting service — paid or free — detached from the shop's offer. **A user may end a session without buying** (this preserves D-002 *trust before sales* and D-004 *AI behaves like a designer, not a salesperson*). The home must clearly say "you can buy directly, but Latenca is best at helping you choose" — not two competing CTAs of equal weight.

---

# D-023
## Title
One Designer Flow; project type is a parameter, not a separate path.
### Status
LOCKED
### Decision
We do not build separate flows per user situation. One flow with a shared skeleton (set the goal → collect minimum data → hypothesis → proposal → feedback → refine → product and purchase), in which the **project type is a parameter** chosen with a single tap at the start. **MVP = two types: (a) empty wall, (b) add / replace.** Input material (photo, dimensions, inspiration) and context (moving in, renovation) are **fields in the project state**, not separate paths. Data and reasoning differ by type; the engine is one.
### Reason
The eight "entry points" mixed three different layers — only project type branches the logic. Building many paths is the funded-team trap. We ask for the type rather than guessing, because a misread at step 1 poisons the whole session.
### Implications
"Whole room" → v2 (needs coherence across walls and pushes the product toward a full interior-design service). Entry points that do not end in a purchase with us ("hang the one I bought elsewhere", "just pick a size") are out of MVP.

---

# D-024
## Title
Learning happens at pool level, not per customer.
### Status
LOCKED
### Decision
In the MVP we **do not build cross-session preference memory or an aesthetic profile of an individual customer.** The system learns from the **whole pool of projects** in order to advise the next customer better. The product's advisory memory is the **knowledge base (KB)**, not a user profile: *"Latenca does not build a cross-session taste profile of an individual customer — the system keeps aggregate knowledge of what works."* Project state applies **within a session**. The KB is built immediately in layers **A (rules) / B (heuristics) / D (patterns)**; layers **E (case studies) and F (effectiveness)** require volume. **From day 1 we log decisions; we do not build an automatic learning loop** until there is volume.
### Reason
Consistent with the locked single-session constraint, with no privacy exposure, while keeping the learning effect. A loop trained on a few dozen projects learns noise and hardens accidents.
### Implications
This does **not** block operational data — orders, consent, or possibly saved projects later. The KB is a **day-1 quality condition** and the source of rationales: a rationale grounded in a KB rule is credible, one invented by the LLM on the fly is confabulation. Humans work **on the system** (KB, catalog, sampled quality audits), never **on an individual project** — the moment human cost grows with each session is the moment we repeat the Modsy mistake.

---

# D-025
## Title
The moat is a target mechanism, not a current asset.
### Status
LOCKED
### Decision
The target mechanism for building advantage: **Curated Catalog × Designer System × Outcome Data × Distribution**. The multiplicative form is deliberate — a missing factor zeroes the whole. **Latenca does not have a moat today:** Outcome Data and Distribution are practically 0, the Designer System is a design, and the catalog exists only partly.
### Reason
Design rules (145 cm centre height, 60–80% of furniture width) are public knowledge — the KB alone is not an advantage. What becomes unique is mapping rules onto **our** catalog, formats and real outcomes. Writing "the Latenca moat is…" would be a false claim of advantage.
### Implications
Distribution is an **unsolved problem, not an asset**, and remains business risk #1. No traffic → no projects → no data → the KB never specializes. Supersedes the earlier framing of "Design Intelligence as *the* moat" (already corrected by D-020).

---

# D-026
## Title
No visible confidence percentage.
### Status
LOCKED
### Decision
The MVP **does not show the user a percentage "confidence score"**. Internally we compute `readiness` from the completeness of key data (wall geometry, anchor context, project goal, aesthetic signal) **and from whether the recommendation is covered by the catalog and KB rules** — not merely a count of filled fields. The user sees a **qualitative state and the missing input**, e.g. *"I just need your wall width to size the art."*
### Reason
A percentage implies statistical precision the system does not have — that is exactly the "fake AI" we ruled out. The qualitative version is simultaneously honest and useful, because it tells the user what to do next.
### Implications
Applied to `prototypes/mockups/02-design-journey.html`: the 72% → 95% meter was replaced with readiness states (a quieter "still missing an input" variant and an accent "ready" variant).

---

# D-027
## Title
Distribution is part of the product.
### Status
LOCKED
### Decision
Distribution stops being "marketing for later" and becomes a product layer. The loop: *catalog + KB → project / editorial scenario → finished wall + rationale → channel → landing page for that specific problem → designer session → purchase → outcome log*. Rules: **in the first distribution test and in the MVP the main landing pages are built per design problem** — because that is how real search behaves ("art above a beige sofa"). Per-style and per-set pages remain permissible later as a **merchandising layer**, but are not the basis of the first test. Also: **no automatic publishing of customer data or photos** (material = editorial scenarios and neutral mockups; customer results only with explicit consent); **Pinterest is the first channel to TEST**, not an approved long-term main channel.
### Reason
Distribution is the weakest factor in D-025 and risk #1. Content pointing at a generic home page produces traffic, not conversion.
### Implications
Search metadata works for SEO and the channel at once. Pinterest organic reach is neither free nor easy — the channel stays a hypothesis.

---

# D-028
## Title
A manual distribution test runs in parallel with Krok 1 — this executes D-010.
### Status
LOCKED
### Decision
In parallel with building Krok 1 we run a **manual, editorial distribution test: 20–30 assets, zero automation.** The test answers three questions: do problem-framed wall-art posts earn attention · which problems generate saves/clicks/visits · does the user move from inspiration to intent to solve a wall. It **does not attempt to prove CAC or purchase conversion** — without a finished product that is not honestly measurable. A content-pack generator is built only if the channel works.
### Reason
**This executes D-010 rather than excepting it.** The Implications of D-010 require discovery/traffic to be addressed early during the build ("Pinterest anchor, content-as-factory, not deferred"). The test does not replace the build, does not block it, and is not a go/no-go gate.
### Implications
D-010 needs **no supersede and no unlocking**. Once the test starts it is recorded in `PROJECT_STATUS.md` (asset count, channel, status, what is measured). Automating a channel that does not yet work would be pure waste.

---

# D-029
## Title
Metrics: design outcome is separate from commercial outcome.
### Status
LOCKED
### Decision
Two measurement layers. **Design outcome** (advisor quality): accepted in session · accepted after iteration · elements swapped · direction rejected. **Commercial outcome** (business): add to cart · purchase · basket value · return. **Primary business signal = purchase. Primary observable signal of recommendation fit = acceptance in session.** A return is a negative signal but not proof of a design error. **"No later change" is rejected as unmeasurable.** Automatic learning on this data stays deferred until volume.
### Reason
Purchase depends on price, shipping, lead time, brand trust, PDP quality, checkout, availability and the finances of the customer. A good recommendation may go unbought; a weak one may be bought for other reasons — measuring advisor quality by purchase would train the system on a noisy signal.

---

# D-030
## Title
MVP boundary: shop spine (Krok 1) + advisor (Krok 2).
### Status
LOCKED
### Decision
The MVP is **Krok 1 (shop spine) + Krok 2 (advisor)**, per the ladder in `VISION.md`. Krok 1 = curated catalog + product page + simple configurator (size/format/finish/frame, live price — **no AI**) + neutral-wall preview + Gelato checkout. Krok 2 = the advisor front door, **the only AI moment in the MVP**, powered by external LLM/vision. Everything else is a later rung: **content personalization** ("use this image but change the flowers") → only when a real content-editing feature exists; **open generation**, **room-photo compositing**, **creator marketplace** → later.
### Reason
This was described in `VISION.md` but never recorded as a decision. It resolves the open "lean vs platform" question: neither a bare lean shop nor an ~8-month platform, but a differentiated MVP with one clear spine. Size, format, finish and frame are ordinary product parameters, not AI — so the MVP carries **only one external-AI dependency** (the advisor, which is orchestration), making it realistic for one person plus AI assistants.
### Implications
We are not a generator — open prompt-to-image is the Ideogram role, not ours (D-020 still governs: we orchestrate external models, we do not build our own). Benchmarks map onto the ladder: Displate and Mixtiles → Krok 1, Fy! → Krok 2, Ideogram → the deferred rung.

---

# D-031
## Title
Uploaded images are an analytical input, never a canvas. The working surface is a flat wall.
### Status
LOCKED
### Decision
**Anything a customer uploads is read, never painted on.** We extract signal from it and recommend from our own catalog; we never composite artwork onto a customer photograph.

**What may be uploaded is deliberately broad** — not only a photo of the wall, but **any image that reveals taste**: artwork they like, an inspiration shot, a fabric, a room they admire. The room photo turns out to be the *less* valuable upload: a room describes **constraints** (colour, size, what sits below), and those can be recovered with two or three questions. A liked artwork describes **taste**, which people cannot put into words — this is exactly the locked "taste is recognized, not described" principle. "Show me something you like" is also a far lower barrier than "photograph your home": less friction, less privacy exposure, and no implied promise to render their room.

**What we extract, and what each is for:**

| Extracted | Used for |
|---|---|
| Wall colour | Tinting the flat working surface — the "this is my wall" effect at zero render risk |
| Palette / dominant tones | Narrowing catalog selection (warm/cool, muted/bold) |
| Wall dimensions | The size answer + the dimension overlay |
| What already hangs there | Avoiding a clash with existing pieces |
| Style signals (furniture, materials) | Choosing which sample room to present in |
| Taste signal (from liked art / inspiration) | The direction of the recommendation itself |

**The working surface is a flat wall** — a plain plane, tinted with the customer's wall colour when we have it. Sample rooms are a *preview*, not the place where work happens. This mirrors what Fy! actually does: their `Flat` mode is editable (pieces move and resize) while the room render is a non-editable preview.

**Communication promise — binding.** We promise exactly what we deliver, and never more:

> *"Send a photo — I'll read the colours, the wall size and the style from it. I'll show the art on a clean wall in your colour so you can see it properly."*

The words "see it in your room" must never appear. Fy! promises *"SEE THE ART HANG IN YOUR SPACE"* and does not deliver it; that gap is what turns a feature into a bait-and-switch.
### Reason
Direct observation of Fy! across four tests (`docs/RESEARCH-wall-display.md`): the **analysis layer works** — palette extraction, wall dimensions, constraint validation, honest failure messages — while the **render layer fails** in three independent ways (missing scale, foreground depth, perspective). Mixtiles, the category leader, never asks for a room photo at all. Compositing succeeded only under near-studio conditions, which is what a curated sample room already provides. Reproducing the failing layer would mean building image work (segmentation, plane estimation) rather than orchestrating external AI — a different kind of undertaking from the one D-020 describes.
### Implications
- Reinforces **D-021**; the backlog item "room-aware compositing" keeps its three-part unlock condition (wall dimensions ✅ / scene depth ❌ / perspective ❌).
- **IP guardrail:** an uploaded image is used **only to read taste**, and recommendations come **from our own catalog**. We never reproduce, imitate or derive from an uploaded work. Basic moderation applies to uploads.
- **Cost:** uploads consume vision tokens (a high-resolution image can cost more than a whole text turn). The per-session image cap in `AI_COST_MODEL.md` applies to **all** uploads, whatever their type — not just room photos.
- The path **without** any upload must remain fully-featured, not a degraded fallback: ~80% of customers will not upload, and two or three questions recover most of the constraint signal.
- ✅ **Resolved (2026-07-20, founder decision): upload ships in the MVP.** The parts questions cannot replace — the wall-colour tint and the taste signal from a liked artwork — are the ones that make the advisor feel like it looked at something. The costs are already bounded: the per-session image cap in `AI_COST_MODEL.md`, and a promise narrow enough to keep (`we read it, we show the art on a clean wall in your colour`).

---

# D-032
## Title
How mockups are actually built: hand-coded HTML on project 15's real components, browser-verified, versioned in the repo.
### Status
LOCKED — supersedes D-016
### Decision
Screens are built as **hand-written HTML**, styled with **project 15's actual component classes and tokens** — not with invented components, and not generated by a visual tool. There is no Stitch step and no `/design/` folder in this repo.

**The method, in order:**
1. **Start from what exists.** If a good version of the screen already exists, **copy the file and edit it** — never re-author from scratch, which always drifts. `prototypes/index.html` lists everything available: current mockups, project 15's finished prototypes, and its 201-file version archive. Check there before designing any panel.
2. **Use 15's real components.** Tokens alone are not enough: borrowing `latenca.css` variables while inventing new component layouts produces something that reads as a different design system. Use the actual classes.
3. **Verify in a browser before showing anything.** Serve the repo and screenshot with Playwright at desktop and 390px. Do not build UI blind and do not claim it works without having looked at it.
4. **Freeze every meaningful version in the repo** at `prototypes/mockups/versions/`.

**Written screen briefs stay.** `reference/design-specs-17/` (`DESIGN_PRINCIPLES.md`, `SCREEN_01_HOME.md`) records the *intent* behind a screen and is still cited — D-012's revision draws its "closer to ChatGPT than to Etsy" framing from `SCREEN_01_HOME`. Briefs are read-only reference, not a build pipeline.
### Reason
D-016 described a process that practice quietly abandoned: Stitch was never used, and the `/design/` path it names as source of truth does not exist here. Leaving it Accepted meant a locked decision silently became optional — exactly what D-019 forbids. This entry records what is actually done, so the two stop diverging.

The two rules about copying and versioning are not stylistic preferences; both were learned expensively. Re-authoring an existing screen instead of copying it drifted repeatedly. And the product page v56–v59 was **permanently lost** because it lived only in a session scratchpad — v59 had to be reconstructed from v55 plus two surviving screenshots.
### Implications
- Reviews critique substance — hierarchy, CTA strength, whether the AI moment reads as intelligent — not "nice".
- A new screen begins by opening `prototypes/index.html`, not a blank file.
- Nothing that matters is left in a scratchpad. The scratchpad is for throwaway working files only.

---

# D-033
## Title
Perfect the flat wall first. Rooms and customer photos are not considered until we are happy with it.
### Status
LOCKED
### Decision
The **flat wall is the product's display surface**, and the work now is to make it excellent rather than to add alternatives beside it. Sample rooms stay in the prototype as a comparison toggle, but **receive no further investment** — no expansion of the room set, no per-room tuning. Showing artwork on a customer's own photo is not reconsidered until the flat surface is genuinely good.
### Reason
The flat plane is the **primary** surface at both category leaders, not a fallback: Mixtiles shows a single tile on a plain background and brings a room in only for multi-piece sets, and Fy!'s `Flat` mode is the editable working surface while its room render is a non-editable preview. Our MVP is a single piece (D-023) — exactly the case where the leader uses no room.

It also removes every failure mode catalogued in `RESEARCH-wall-display.md` — wrong scale, foreground depth, perspective — from the MVP entirely, rather than managing them. And it is cheap to perfect and expensive to fake: rooms would need six to nine photographs plus per-room placement, while the flat surface needs only craft.
### Implications
- **The bar on scale presentation rises sharply.** With no furniture for the eye to catch on, the promise of certainty rests entirely on the numbers and the artwork. The current dimension overlay is a starting point, not the finished thing.
- Identified work on the flat surface, most important first: **(1)** a true-scale reference outline (sofa or figure) so size can be judged without a room; **(2)** side-by-side size comparison instead of switch-and-guess; (3) a grid toggle, as Fy! has; (4) wall texture and light so the frame reads as hanging rather than pasted; (5) frames and materials — reuse the machinery already built in `03-product.html`, per D-032; (6) multi-piece layouts, since sets are the only economics that work.
- Does not reverse **D-021** or **D-031**; it sharpens their sequencing. Uploads remain an analytical input (D-031) — the wall colour read from a photo tints this flat surface.
- Supersedes the earlier working recommendation to keep both surfaces on an equal footing.

---

# D-034
## Title
The advisor and the product page are one screen in two states, not two screens.
### Status
LOCKED
### Decision
There is **one shell**: the artwork occupies the main area, and the right-hand column holds either the **conversation** or the **buy panel**. Whichever is not open collapses to a single line and stays reachable — the conversation never closes to buy, and the price is never hidden while talking. The entry point decides only which state opens first:

- **from the catalogue, search or a shared link** → buy state, with the conversation offered on one line
- **from "help me choose"** → conversation, with the price and configuration on one line

The stage does not show "the product". It shows **what is currently being discussed**, so a request like *"not this one — something warmer"* swaps the piece in place.
### Reason
Both screens had independently converged on the same layout, and the advisor mockup was re-inventing a poorer version of machinery the product page already had (frames, materials, sizes, room toggle, zoom). Building a third thing would have meant maintaining two answers to every question. Reusing the real page is also what D-032 requires.

The stronger reason is behavioural: a hard jump from advisor to product page ends the conversation exactly when the customer is closest to deciding. One screen removes the jump.

Keeping the chat **offered rather than open** on the catalogue entry protects two things at once — D-022, since a customer who already knows what they want must be able to buy without talking, and the cost model, since the product page is the highest-traffic page in the shop and a click is what keeps AI spend bound to intent.
### Implications
- **The chat is a new, much higher-traffic entry point to the AI than `AI_COST_MODEL.md` assumed.** The click gate bounds it, but the limits need recalculating against two entry points rather than one.
- **The conversation state must live *above* the product page in the component tree**, not inside it. Otherwise even a soft navigation unmounts it and the whole idea collapses. This is the one hard technical constraint of this decision.
- The address follows the stage (so bookmarks and shared links stay honest) but **adds no history entry** — six proposals must not mean six taps of Back. Back returns to the catalogue; the trail of seen pieces is the way back within the session. This is where the locked **closing overview** actually lands.
- **Size, material and frame survive an artwork swap.** They describe the wall, not the piece.
- Swaps are **sequential** — one proposal at a time, per the locked stance. Alternatives stay available but are not the primary move.
- The stage still holds **one** frame. Multi-piece walls remain the one genuine structural gap (D-033, item 6).
- Implemented in `prototypes/mockups/04-advisor.html`; `03-product.html` is left untouched as the reference. They converge into one file once the pattern is proven.

---

# D-035
## Title
The three sample rooms become the scale reference, and are calibrated to real centimetres.
### Status
LOCKED
### Decision
The flat wall stays the **workspace**; the three fixed sample rooms become the **size check**. Each room photo is measured **once** against a known object (a sofa at ~210 cm, a door at ~80 cm, a dresser at ~100 cm) to yield one number — pixels per centimetre on that wall plane. Every artwork at every size then renders at **arithmetically correct scale**, with no AI, no perspective estimation, and no per-customer variance.

Three rooms is the whole system. The set does not grow.
### Reason
Artur's observation: a fixed photograph can be calibrated once, whereas an abstract true-scale outline has to be interpreted by the viewer. A real room reads instantly and costs three measurements.

Inspection of the current prototype found the harder reason. Size multipliers are `0.78 / 1 / 1.26` where the true width ratios of 30×40, 50×70 and 70×100 are `0.6 / 1 / 1.4`, with a code comment explaining that the artwork is kept prominent at every size. **The room preview compresses scale — it shows small prints larger and large prints smaller than reality.** It flatters the artwork and misleads about the single thing a customer opens that view to learn.

The same check on `12. Printly` — which has a mature version of this machinery — found it does the same: artwork wrap scales `1 → 1.35 → 1.35`, with the size difference faked by shrinking the room background instead (`bg 1 → 1 → 0.775`), giving effective ratios of about `0.74 / 1 / 1.29`. Neither codebase contains any centimetre-to-pixel conversion. **This is an unsolved problem in both, not a solved one to copy.**
### Implications
- **Amends D-033**, which put rooms under a no-further-investment rule. That rule was aimed at compositing onto customer photos and at growing the room set — neither applies to three owned, calibrated photographs. Flat-wall-first is unchanged; rooms simply take a different job.
- **After calibration, 30 × 40 will look small.** That is the information the customer came for and it must not be compensated for.
- The calibration assumes the wall plane is roughly parallel to the camera. We own these three photographs, so this is a selection constraint, not a risk.
- `12. Printly` (`lib/mockup/calibration.ts`, `lib/frames/v3-metas.ts`, `components/blocks/MockupViewer.tsx`) is still worth copying when we reach real code — breakpoint matrix, orientation handling, graceful fallback, data-driven for new Gelato sizes. It uses **the same three room assets** (cupboard / dresser / office), so measurements transfer directly. **Copy the machinery; replace the hand-tuned numbers with computed ones.**
- Does not reverse D-031: customer photographs remain an analytical input and are never a canvas.
