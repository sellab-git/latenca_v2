# Audit — "Design my wall" (05-wall.html) + product/detail view

Date: 2026-07-23. Scope: the two states of `prototypes/mockups/05-wall.html` — THE WALL (pan/zoom canvas + floating advisor/buy panel) and the PRODUCT/DETAIL view (scrollable overlay with artwork + picks + catalog). Sources: code read + live browser probe (Playwright) + an independent adversarial static review.

This doc has two jobs:
1. **Open decisions** that need Artur/ChatGPT input before I build them (below, top).
2. **Full findings + status** — what I am fixing autonomously vs what is blocked on a decision.

---

## A. DECISIONS — RESOLVED 2026-07-23 (ChatGPT review)

**Architectural principle (overrides everything below):** shipping, availability, catalog filtering and recommendation ranking are **shared services/modules used across Home · Product · Wall · Cart** — never local to `05-wall`.

- **D1 — Shipping:** live **Gelato** quote for the customer's country/postal code (no flat rate; would be arbitrary for global POD). Prototype: country picker → `Shipping calculated for [country]` → shown amount → total = items + shipping. MVP: `getShippingQuote(cart, destination)` → Gelato is source of truth → amount passed to Stripe as shipping. States: loading / quote / unavailable. No "free shipping over $X" until per-market economics are known.
- **D2 — Tax:** **Stripe Checkout + Stripe Tax** (`automatic_tax`), computed from the customer's address at checkout. Prices are **tax-exclusive**; PDP shows `Taxes calculated at checkout`. Remove `incl. VAT` and `ships to Poland`.
- **D3 — Cart:** **itemise** the wall (each piece: artwork · size · material · frame · price) then Subtotal / Shipping / Tax-at-checkout / Total — still one arrangement, one order, but a visible line spec. **Remove the empty "Pairs well with"** cross-sell for now (revive later from the shared catalog engine).
- **D4 — Trust:** one light line **under the CTA**: `Secure checkout · Made to order · Support if anything arrives damaged`. No extra accordion, no payment-logo wall, **no certificate/ratings unless real**. Future Trustpilot = brand-level (header/Home), never per-artwork.
- **D5 — Limit:** **max 12** (control + advisor copy + counter + layout presets + cart validation must all agree). Copy fixed to 12.
- **D6 — Catalog:** **one shared Catalog Engine** (data · tags · filters · sort · card components · a11y rules); Home/Product/search/recs embed it, differing only in default filter / count / layout / heading. Do NOT invent a second taxonomy for the wall. ⚠️ **Finding (Claude, verified):** the Home catalog filters are **a MOCK** — `syncAll()` only updates pills/chips/panel, the count is faked (`n=4120`/heuristic in `01-home.html`), and the grid is **not** re-filtered. So there is **no real engine to extract yet**; the shared engine must be **built** (real tagged dataset + filter/sort logic) as an MVP task. Until then the wall's detail filters stay non-functional rather than duplicating a mock.
- **D7 — Latenca Picks:** deterministic ranking from the shared catalog data (`category + palette + orientation + mood − current artwork`), **not** an LLM/embeddings. Needs the tagged dataset (blocked with D6).
- **D8 — Availability (new):** resolved at **variant × destination** through Gelato, not at artwork level. Unavailable config → hide/disable the variant + offer an alternative; never remove the artwork. Shared service for configurator/cart/recs.
- **D9 — Zero results (new):** never a dead end. Prevent where possible (show counts, disable would-be-zero options); on filter-zero → explain + `Remove last filter`/`Clear all` + closest matches (flagged as broader); on search-zero → suggestions + related + advisor CTA; on no-Gelato-variant → nearest available size/material; on weak advisor match → be honest + offer one high-impact change.

**Prototype-now vs MVP-backend:** buildable in the static prototype = D2 copy, D4 trust line, D3 itemised cart, D5 consistency, and mocked D1 country/shipping + D9 recovery UI. Requires the Next.js MVP (real services) = live Gelato quotes (D1), Stripe Tax (D2), the shared Catalog Engine + tagged dataset (D6/D7), Gelato availability (D8).

---

<details><summary>Original open-decision context (pre-resolution)</summary>

These are product/commerce choices, not code. I will NOT guess them. Each has context + my recommendation.

### D1. Shipping model & where the cost is shown  *(blocks the price/trust fixes)*
Today: "Free shipping over $60" is hardcoded in 3 places; the cheapest wall is $39; below the threshold the shipping cost is shown **nowhere**; the cart total = piece sum with **no shipping line**. Real fulfilment is Gelato (print-on-demand), whose shipping is quote-based per destination.
- **Question:** flat rate? free-over-$X (what X)? live Gelato quote? And do we show a shipping line in the panel + cart, plus a "spend $X more for free shipping" nudge?
- **My recommendation:** a simple flat shipping shown as its own line + a free-over-threshold nudge for the prototype; wire real Gelato quotes only in the Next.js build. Pick a threshold that sits above a 1-piece wall (e.g. free over $75) so the nudge actually fires.

### D2. Tax / market model  *(blocks the "incl. VAT" cleanup)*
Today: prices in **USD**, label says "incl. **VAT**" (EU concept), delivery hardcoded "ships to **Poland**", dates `en-US`. Three markets in one panel. Latenca is already decided **English-first / USD / global**.
- **Question:** confirm global USD, tax-not-shown (US-style) vs tax-inclusive. Remove "VAT" + "Poland" entirely?
- **My recommendation (will apply unless overridden):** global USD, drop "incl. VAT" and "ships to Poland", show tax as "calculated at checkout" or omit; keep one locale formatter. This matches the settled English-first decision, so I will proceed with the removal and leave the *replacement wording* for D1/this decision.

### D3. Cart itemisation & cross-sell
Today: a multi-piece wall collapses in the cart to "Your wall · N pieces" with one thumbnail + one total; pieces can differ in size/frame/material but none of that shows. The "Pairs well with" cross-sell section is **always empty** (never populated).
- **Question:** itemise each piece (thumb + size/material/frame + price per piece)? And what fills "Pairs well with" — same-artist works, same-collection, or drop it?
- **My recommendation:** itemise (buyers of "N different pieces" must verify what they pay for); fill cross-sell with same-artist / same-collection picks, or remove the heading until we have it.

### D4. Trust signals near the buy CTA
Today: rating/reviews, certificate of authenticity, secure-checkout, payment logos, returns all live **inside the collapsed "Options" sheet** — invisible at the moment of decision. Note: there is no real review system yet, so "rating/reviews" would be placeholder data.
- **Question:** which trust cues go next to "Add wall to cart", and do we have real data for them (reviews? COA? returns policy)? 
- **My recommendation:** a compact always-visible trust strip with the cues we can back truthfully (secure checkout, returns, COA if real); NO fake review counts.

### D5. Piece count ceiling — 6 or 12?
Today: the `+` control and layouts support **12**; the advisor copy says **"Six pieces is the most I arrange on one wall."** They contradict. Decision D4 in project notes = keep 12.
- **My recommendation (will apply):** make the copy say 12 (match the control). Flag only in case 6 was the real intent.

### D6. Catalog filtering — needs a category taxonomy  *(blocks "real filters")*
The detail-view catalog shows pills *Matching / Abstract / Botanical / Landscapes / Space*, an orientation toggle, and Sort. Right now they do nothing. Orientation + Sort I can wire from existing data. But **the artworks have no category tags** (only title/artist/orientation), so the theme pills can't filter anything real.
- **Question:** what is the category taxonomy, and should each artwork carry a category tag?
- **My recommendation:** define ~5 canonical categories, tag the art pool, then the pills become real. Until then I will (a) make the pills keyboard-accessible buttons and (b) wire orientation + sort, and clearly mark theme pills as not-yet-active rather than silently dead.

### D7. AI "picks" matching (Etap C)
The "Latenca picks" were always a stub ("palette-matched later"). Real palette/mood matching needs a matching signal per artwork (dominant colours / mood tags).
- **Question / recommendation:** defer until D6's taxonomy exists; then match on category + palette.

---

</details>

## B. What I am fixing autonomously (no decision needed)

Tracked here as I go (✅ done / ⏳ in progress):

- [x] **Detail view = real modal** — `role="dialog"` + `aria-modal="true"` + dynamic `aria-label`, focus moved in on open (`#spBack`), **Esc closes**, focus returns to the piece on close. Verified live. *(Full Tab focus-trap still a follow-up.)* (P0 #3)
- [x] **Advisor chat announced to screen readers** — `aria-live="polite"` (`role="log"`) on `#msgs`, typing indicator `aria-hidden`. Verified. (P0 #5)
- [x] **"Six pieces" copy → real ceiling** — now uses `MAXPIECES` (12). (P1 #6 / D5)
- [x] **Removed placeholder string** "(In the real product…)". (P1 #9)
- [x] **`sizesFor()` uses its argument** (latent wrong-orientation bug fixed). (P2 #13)
- [x] **Catalog + pick images `loading="lazy"`** (hero/wall stay eager — above the fold). (P2 #14)
- [ ] **Filter pills** — deferred to Etap C, blocked on **D6** (no category taxonomy yet). (D6)
- [ ] **Remove "incl. VAT" + "ships to Poland"** — waits on D1/D2 replacement wording. (P0 #1/#2)

Verification: Playwright hit-tests confirmed the modal (role/aria-modal/aria-label, focus-in=`#spBack`, Esc closes, focus returns to the slot), `aria-live=polite`, no JS errors (only a favicon 404), and no regression to price/config/open-close (panel reparents to `#spotlight` and back to `.pdp` cleanly).

- [x] **Dead-code removal** — stripped ~111 lines of CSS/JS inherited from the single-product page (image `.stage*`/room classes, `.thumbs`, the `.buy`/`.pmeta`/`.priceblock` panel, `.fmt`, `.digital`, `.whyband` tokens (kept `.why` — live in chat), `.gtabs`, `.crumb`, `.summ`, `.follow`, the crossfade, and the whole `.lightbox` block; JS `sizeAR()`, `SHAPES_FOR`/`allowedShapes`, lightbox handlers). Each verified unreferenced (grep across the file + shell.js + app.css, incl. template strings) by a background review; applied one block at a time and Playwright-tested the full flow (fill, add/remove, layout, open piece, catalog, config sizes/materials/frames, drawers, cart, Esc) — **no JS errors, no visual change, live elements still styled**.

Still deferred to the pre-Next.js pass: promote magic numbers (`432px` panel width, `PAD`, zoom limits) to tokens, extract English strings for i18n. (Unused CSS will also be auto-purged by the Next.js build.)

Mobile (canvas model is desktop-only; missing `<nav class="tabbar">`; detail unhandled <821px) is a separate effort — not touched now.

---

## C. Full findings (reference)

### P0 — buyer-visible inconsistencies
1. Price/tax/delivery = three markets at once (USD + "VAT" + "ships to Poland" + en-US dates); "incl. VAT" is even overwritten to "this piece" once a piece is focused. → D1/D2.
2. Shipping cost shown nowhere; cart total has no shipping line. → D1.
3. Detail view is not a real modal: Esc doesn't close, focus not moved in, no `role="dialog"` (verified live). → fixing.
4. Catalog filters in the detail view are dead (pills are `<span>`, clicks do nothing; verified live). → partial fix + D6.
5. Advisor chat invisible to screen readers (no `aria-live`). → fixing.

### P1 — logic & content
6. "Six pieces is the most" but the real limit is 12. → fixing (D5).
7. Cart doesn't itemise a multi-piece wall; "Pairs well with" is permanently empty. → D3.
8. No trust signals next to the buy CTA (all buried in collapsed Options). → D4.
9. Placeholder/stub strings can reach a real buyer. → fixing.

### P2 — pre-port hygiene
10. ~40% dead CSS/JS inherited from the single-product page (stage/room/lightbox/old buy panel). → pre-port pass.
11. Magic numbers (panel width `432px` ×5, `PAD`, zoom limits) should be tokens. → pre-port pass.
12. Hardcoded English strings + `$` + `en-US` block i18n. → pre-port pass.
13. `sizesFor()` ignores its argument (latent bug). → fixing.
14. Images lack `loading="lazy"`/dimensions/skeleton. → fixing.

### Mobile (separate effort)
Canvas model gated to `min-width:821px`; no mobile tab bar (`#appTabbar` absent) → phone has no primary nav; detail/spotlight positioning unhandled below 821px.

### What already works well
Layer model (chrome > product > wall), wall↔detail panel parity, token system, orientation enforcement (D5 crop rule), config drawers (size/material/frame) + cart drawer, pieces are real `<button>`s, images have `alt`, nav arrows labelled, `prefers-reduced-motion` present, price sums correctly.
