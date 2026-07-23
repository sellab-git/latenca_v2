# Component inventory — reuse these, don't reinvent

**HARD RULE.** Before styling or building ANY UI element in the mockups, **grep this file (and the target HTML) for an existing component and reuse its exact classes/markup.** Do NOT author a fresh `.myThing{…}` with your own padding/shape/font/colour. Inventing a new element for something that already exists is the single most repeated mistake on this project — every "why does this look different?" has been a reinvented component.

**Process every time:**
1. Name the thing you need (a placeholder / a button / a chip / a card / a trust line…).
2. Find it below (or grep the HTML for a sibling that already does it).
3. Reuse the SAME markup + classes. Only add a tiny variant class if a state is genuinely missing.
4. If it truly doesn't exist yet, add it here as a new shared component — then use it everywhere.

Tokens live in each file's `:root` (colours, `--fs-*`, `--w-*`, `--sp-*`, `--r-*`, `--btn-*`, `--icon/--iconbtn`, `--z-*`, `--mainpad`). Never hardcode px/hex that a token covers.

---

## Reusable components (mockups)

| Need | Component | Classes / markup | Notes |
|---|---|---|---|
| **Empty-slot placeholder** ("+ Add a piece") | `.ph` | `<span class="ph"><svg>+</svg><span>Add a piece</span></span>` inside a dashed box | ONE component — used on the wall (`.slot.empty`) AND the pick overlay (`.sp-art.empty`). Icon 22px, Inter, `--fs-xs`, semibold, muted. **Do not make a second placeholder.** |
| **Wall piece** | `.slot` | `<button class="slot">` (`.empty` variant) | Real `<button>`; white edge + `--art-shadow-lg`. |
| **Dock icon button** (layout/zoom/count/show-sizes) | `.wl-btn` | `<button class="wl-btn">` + `.wl-btn.on` for toggle | Lives in the `.walllevel` dock. Numbers = `.wl-n`, labels = `.wl-lb`. |
| **Advisor quick-chip** | `#quick button` | rendered by the `CHIPS` registry + `refreshQuick()` | Context-scoped (wall/piece/pick). Add a chip = one registry entry (D11). Never hand-render chips elsewhere. |
| **Buttons** | `.btn` / `.addcart` / `.pill` / `.mat` / `.seg button` | heights are tokens `--btn-sm:36 / --btn-md:40 / --btn-lg:48` | Primary CTA = `.addcart` (ink). Don't invent button heights. |
| **Icon button (light surface)** | `.icobtn` / `.pact` / `.dclose` | 40×40, `--r-ui`, muted → accent-ink on hover | |
| **Filter bar** (pills + orientation seg + sort + All filters) | `.filterzone`→`.filters` | `.pill` · `.count` · `.allf` · `.seg button` · `.drop` | Copied 1:1 from `01-home`. Reuse verbatim; don't restyle. |
| **Catalog card** | `.tile` | `img` + `.tgrad` + `.fav` + `.acts .tbtn` + `.info` | The one gallery card. Same on home, explore, detail. |
| **Cart line item** | `.citem` | `img.th` + `.ci`(`.ct`/`.cc`/`.cp`) | Itemised wall (D3). Totals = `.csub` + `.crow`. |
| **Trust line** | `.certline` | shield svg + text | Under-CTA variant = `.certline.trustdock` (centred, smaller). |
| **Slide-in drawer** | `.drawer` + `.scrim` | `.dhead` / `.dbody` / `.dfoot` | Cart, size guide, material/frame compare. `openDrawer()/closeDrawers()`. |
| **Config controls** | `.mat` (material) · `.optrow button` (size/mat) · `.frm` (frame swatch) · `.unit` (cm/in) | | Live in the config sheet `#cfgSheet`. |
| **Chat message / typing** | `.msg` (`.msg.me` for user) · `.typing` | `say('ai'\|'me', html)` | `#msgs` is `role="log" aria-live="polite"`. |
| **Section label** | `.blabel` | uppercase, `--faint` | |
| **Expand/collapse toggle** | `+` icon rotating 45°→× | `transform:rotate(45deg)` | NOT a chevron (project rule). |
| **Detail overlay** | `#spotlight` (`role="dialog"`) | hero `#spStage.sp-art` · picks `#spPicks .sp-th` · catalog `#spCat` | Panel `#col` reparents in. Layer model: chrome(800) > product(500/600) > wall(1) — see `layer-model.md`. |

---

## Where the design system lives
- **Tokens + shell**: `prototypes/mockups/shared/app.css` (`:root`, `.side`, `.topbar`, `.app` grid).
- **Chrome injection**: `prototypes/mockups/shared/shell.js` (sidebar, topbar, tabbar, search dropdown).
- **Layer/z-index model**: `docs/layer-model.md`.
- **Per-file `<style>`**: page-specific components (the wall/detail live in `05-wall.html`).

If a component isn't here, it's either in `app.css` (shared chrome) or the page's own `<style>` — grep before inventing.
