# DESIGN PRINCIPLES

The single source of truth for Latenca's design. **This replaces the old `UX_UI.md`.**
Per-screen specs live alongside this file as `SCREEN_XX_*.md`.

**Workflow:** the founder (Product Designer / UX Lead) writes screen specs → Stitch
(UI/visual designer) generates UI from them → Claude (frontend engineer) implements in
code → founder reviews. Keep Stitch and the coded tokens in sync (see "Design system").

## What Latenca is (and isn't)
Latenca is an **AI Wall Designer** — it guides people from uncertainty to confidence when
choosing and arranging wall art. It is **not** an ecommerce print marketplace. It should
feel like a calm interior designer — closer to a guided conversation than a shop.

## UX principles
1. **Reduce cognitive load** — never show more options than necessary (max ~3 primary per screen).
2. **Guide, don't overwhelm** — progressive disclosure; guidance over long lists.
3. **Confidence first** — every screen should reduce uncertainty.
4. **Mobile-first** — designed for one-handed phone use.
5. **Beautiful by default** — visual quality is product quality.
6. **AI present everywhere but never shouting** — a calm designer, not a chatbot.

## Visual direction
Calm. Editorial. Warm. Trustworthy. References: Apple, Aesop, Airbnb.
Photography dominates; the UI disappears. Lots of breathing room; very little visual
noise. Never look like a print marketplace.

## Design tokens
**Palette (warm natural neutrals):**
- Ink / near-black (primary actions, text): `#1A1A1D` / `#0F0F10`
- Muted text: `#6B6B6D`
- Background (warm cream): `#F6F3EF`
- Panel / surface: `#EFEAE4`
- Accent — warm oak (sparingly): `#A67C52`
- Accent — sage (sparingly; confidence / success): `#6FA28A`

Primary buttons = solid dark ink, light text. Accents used sparingly, never as large fills.

**Typography:** Playfair Display (headlines — large, elegant serif) · Inter (body & labels).
**Shape:** cards ~16px radius; primary buttons are full pills; soft subtle shadows, no harsh borders.
**Icons:** outline, 2px stroke, rounded.
**Layout:** 8pt grid, generous spacing; cards are the primary element (one idea per card).
**Imagery:** real, warm interior photography; immersive, editorial — not product-on-white.

## States (don't skip)
- **Empty states** educate and motivate — never blank.
- **Errors** explain what happened, why, and how to fix it.
- **Accessibility:** dynamic text, high contrast, screen readers, large tap targets.
- **Dark mode:** designed from the start; light and dark get equal care.

## Design system — kept in two places, in sync
- **Stitch** (visual generation): project `Latenca_v1` (id `14371462573108088597`),
  design system "Latenca — Calm Editorial" (asset `3417471652753919553`).
- **Code** (implementation): `web/src/app/globals.css` (`@theme` tokens) + `web/src/messages` (copy).

When either changes, update the other so Stitch output and the app never drift.
