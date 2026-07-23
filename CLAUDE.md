# Latenca — project instructions

Curated AI-wall-art shop with an AI advisor. Static HTML mockups (project-15 design system) in `prototypes/mockups/`, heading to a Next.js MVP. UI/copy = **English**, prices **USD**, global market.

## RULE #1 — reuse components, never reinvent  ⛔ (the single most repeated mistake here)

Before styling or building ANY UI element in the mockups:
1. Open **`docs/components.md`** — the inventory of existing components. Is there already one for this? (placeholder `.ph`, dock button `.wl-btn`, buttons `.btn`/`.pill`/`.mat`, card `.tile`, drawer `.drawer`, trust line `.certline`, filter bar `.filterzone`, config `.optrow`/`.frm`, chips via the `CHIPS` registry…)
2. `grep` the target file for a sibling that already does it and **reuse its exact classes/markup**. Broaden a selector into a shared component rather than authoring a parallel one.
3. Only author a NEW class if it genuinely doesn't exist — then add it to `docs/components.md`.

Every "why does this look different?" from Artur has been a reinvented component (latest: an invented `.sp-pickhero` instead of the shared `.ph`). Do not author a fresh `.myThing{…}` with your own padding/shape/font/colour when a component exists. Use `:root` tokens (`--fs-*`, `--w-*`, `--sp-*`, `--r-*`, `--btn-*`, `--icon/--iconbtn`, `--z-*`, `--mainpad`) — never hardcode px/hex a token covers.

## Key docs (read the relevant one before working)
- **`docs/components.md`** — reusable component inventory (RULE #1).
- **`docs/layer-model.md`** — the 3-layer z-index model (chrome > product > wall). Read before touching any z-index/overlay.
- **`docs/audit-wall.md`** — wall+detail audit + all product decisions (D1–D11: shipping/tax/cart/trust/catalog engine/unified slot flow/context chips) + the mockup↔real-code boundary.
- **`docs/PROJECT_STATUS.md`** — current state / resume point.
- **`docs/wall-spec.md`**, **`docs/DECISIONS.md`** — frozen wall rules + decision log.

## Conventions
- **Freeze a snapshot** `prototypes/mockups/versions/05-wall-vN.html` + a `versions/labels.json` entry at each meaningful mockup change.
- **Verify in the browser** (Playwright) before claiming done — measure/hit-test, don't assert.
- Auto-push this repo (Artur's standing rule); `private/` (costs/keys) is never pushed.
- Competitor screenshots shared in chat are NOT committed — the repo holds only our derived numbers.
