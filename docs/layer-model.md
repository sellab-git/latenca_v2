# Layer model — the "Design my wall" canvas (05-wall.html)

**Read this before touching any z-index, `position`, overlay, or panel on the wall page.**
The repeated bugs (panel over the top bar, invisible search dropdown, wall showing through) were all
the same root mistake: not respecting this stack. Artur defined it plainly — keep it exactly.

## The three planes (bottom → top)

| # | Plane | Elements | z-index | Rule |
|---|-------|----------|---------|------|
| 1 | **WALL** (lowest) | `#wallView` (the canvas our compositions hang on) | **1** | never on top of anything |
| 2 | **PRODUCT** (middle) | `.spotlight` (open piece + catalog), `.col` (the buy/advisor panel) | **500 / 600** | sits *between* — above the wall, below the chrome |
| 3 | **CHROME** (top) | `.side` (left menu), `.topbar` (top bar) **and the topbar's `.sdrop` search dropdown** | **800** | **NEVER covered by anything** |

**Invariant: `CHROME (800) > PRODUCT (600 ≥ 500) > WALL (1)`. Always. No exceptions.**

- The buy panel `.col` scrolls *under* the top bar — because chrome (800) > panel (600).
- The search dropdown is nested inside `.topbar`, so it inherits the chrome plane and renders above the open product.
- The wall is a full-screen `position:fixed` canvas behind everything; the chrome is opaque and covers it at the edges.

## Why it kept breaking — the gotchas

1. **`z-index` does nothing on a `static` box.** The top bar was `position:static` in one override → its z-index was
   ignored → it dropped below the product. Chrome must stay **positioned** (`sticky`/`relative`) *and* carry its z-index.
2. **The generic token ladder is modal-oriented and does NOT match this page.** `--z-scrim:500 / --z-panel:600` are
   "modal" tiers that sit *above* `--z-header:200`. In a normal page that's right; on this canvas page the chrome is a
   fixed *frame* that must top everything, so chrome is raised to **800** (above the product band). Don't "fix" this by
   lowering it back to `--z-header`.
3. **`.main` is transparent in the canvas model** (so graphics slide under the chrome). Any gap in an overlay therefore
   shows the wall through it. The `.pdp{margin-top:12px}` gap is why `.spotlight` bleeds up `top:-12px` to reach the top
   bar, and bleeds left `left:-(--mainpad)` to reach the menu. An overlay must cover edge-to-edge or the wall leaks.
4. **Nested `position:absolute;z-index` bubbles to the nearest *positioned-with-z* ancestor.** `.col`/`.spotlight` live
   inside `.pdp`/`.stagewrap`, but those don't create stacking contexts, so their z-index competes directly in `.app`'s
   context against the chrome. That's why raising the chrome above 600 is enough.

## Checklist before adding/º moving any overlay on this page

- [ ] Which plane is it — WALL, PRODUCT, or CHROME? Pick its band and stay inside it.
- [ ] Is the box **positioned**? z-index is inert on `static`.
- [ ] Does it cover its whole area, or will the transparent `.main` leak the wall at an edge?
- [ ] Verify with a hit-test (`document.elementFromPoint`), not by eye — Playwright, on a fresh `?cb=` URL.

## How to verify (Playwright)

```js
// panel must go UNDER the top bar on scroll:
sc.scrollTop = 30; sc.dispatchEvent(new Event('scroll'));
document.elementFromPoint(panelCenterX, topbarBottom-4).closest('#topbar')   // → truthy = correct

// search dropdown must render ABOVE the open product:
document.elementsFromPoint(dropX, dropY)   // .sdrop must appear BEFORE .spotlight in the list
```
