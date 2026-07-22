# Wall configurator — frozen rules (v1)

The "Design my wall" flow. Decisions locked with Artur 2026-07-22. This is the
contract the mockup (`prototypes/mockups/05-wall.html`) and the layout engine
(`prototypes/mockups/shared/gen-wall-layouts.py`) must follow.

## Model
- A wall = N pieces, N = 1–12.
- Layouts are **curated presets**, authored in our own cm grid, cm-true by
  construction (proportions between pieces are always physically real).
- Mixtiles' 45 real arrangements are an **idea library** only
  (`docs/mixtiles-positions.json`); we do not copy their geometry.

## The 9 sizes (the only sizes we sell)
Portrait 30×40 / 50×70 / 70×100 · Landscape 40×30 / 70×50 / 100×70 · Square 30×30 / 50×50 / 70×70.
In the engine, 10 cm = 1 unit → tokens `P0/P1/P2`, `L0/L1/L2`, `S0/S1/S2`
(orientation letter + size tier 0=small 1=mid 2=large). Any mix renders cm-true.

## D5 — Orientation / crop rule (slot owns orientation)
Each layout slot has a fixed orientation. A source artwork may fill a slot ONLY if:
- **Portrait** artwork → Portrait **or** Square slot
- **Landscape** artwork → Landscape **or** Square slot
- **Square** artwork → Square slot only
(A square slot can crop any source; a P/L slot needs a source of that orientation.)
This MUST be enforced everywhere art enters a slot: initial fill, art swap,
**layout switch**, and count change. Current bug: it still mixes on layout switch — fix.

## D1 — Size behaviour (locked)
- **Curated / mixed compositions:** sizes are baked and LOCKED. No per-piece size change.
- **Uniform sets** (all pieces same orientation): the client may change the size of
  the WHOLE set at once (e.g. three portraits → 30×40 / 50×70 / 70×100). Never a single piece.

## D4 — Counts
1–12. The piece counter is capped to counts that have a defined layout; never fall
back across counts (no showing a 1-slot layout for a 7-piece wall). Adding/removing a
piece must preserve each surviving piece's orientation.

## D2 — Viewing (zoom, not a fixed scale)
- Default: the wall fits the stage sensibly — fewer pieces = bigger, more pieces =
  smaller, but never below a hard **minimum tile size** (no 10×10 px pieces).
- A **zoom control** (−/100%/+ with scroll) to enlarge a busy wall.
- A **"show all dimensions" toggle** (Mixtiles-style) that reveals every piece's cm at once.
- Proportions between pieces are always true. **No** room/ruler reference object for now.

## Parked (separate topic, do not build yet)
Frames, materials (paper / canvas / …), passe-partout / mats — how they change size on
the wall and how to display them. Frames are cosmetic-only until this is designed.

## Engine
`gen-wall-layouts.py` — author layouts as `rows(...)` / `grid(...)`; a row cell may be a
vertical **stack** (`["P2", ["S0","S0"]]`) for hero compositions (D3). Run it to emit
`shared/wall-layouts.js`. 27 layouts, every count 3–12 covered.
