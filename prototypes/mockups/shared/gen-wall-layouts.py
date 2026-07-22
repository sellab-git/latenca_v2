# -*- coding: utf-8 -*-
# =============================================================================
#  LATENCA — WALL-LAYOUT DESIGN KIT
#  Author gallery-wall layouts in our OWN cm grid. Proportions are correct by
#  construction — we never copy Mixtiles pixels, we only borrow their IDEAS.
#
#  We sell 3 sizes per orientation; on the wall every piece shows at its middle
#  (50 cm) tier, whose real cm share a 50 cm module:
#     square  50x50   portrait 50x70   landscape 70x50
#  Expressed in 10 cm UNITS (u):  S = 5x5   P = 5x7   L = 7x5
#  Because every piece's on-wall size comes from this module (not from pixels),
#  a square and a portrait ALWAYS share the 50 cm width and differ only in height.
#
#  HOW TO DESIGN A NEW LAYOUT  (edit SECTION 2):
#    rows("SP", "L")        -> row 1 = square+portrait, row 2 = one landscape
#    grid(3, 2, "S")        -> 3 columns x 2 rows of squares
#    A "spec" is a string of orient chars (S/P/L) = one horizontal row,
#    left->right. rows() stacks the rows, centres each one, and vertically
#    centres each piece inside its row band. Output proportions are exact.
#    For a shifted (brick) row pass a tuple: ("SPS", dx_in_units).
#
#  Run:  python "gen-wall-layouts.py"   ->  writes wall-layouts.js
# =============================================================================

import collections

# ---- SECTION 1: THE ENGINE (reusable — you rarely touch this) ---------------
# All 9 Gelato sizes, in 10 cm UNITS. tier 0=small 1=mid 2=large.
#   Portrait  30x40  50x70  70x100     Landscape 40x30  70x50  100x70
#   Square    30x30  50x50  70x70
# A "token" = orient letter + tier digit: P0 P1 P2 / L0 L1 L2 / S0 S1 S2.
# Because every module lives in the same 10 cm unit, ANY mix renders cm-true:
# a small square next to a large portrait shows their true relative sizes.
DIM = {
    "P": {0: (3, 4), 1: (5, 7), 2: (7, 10)},
    "L": {0: (4, 3), 1: (7, 5), 2: (10, 7)},
    "S": {0: (3, 3), 1: (5, 5), 2: (7, 7)},
}
GAP = 0.55                                          # ~5.5 cm between frames

def _parse1(tok):
    """'P2' -> ('P',2). Bare letter -> tier 1."""
    return tok[0], (int(tok[1]) if len(tok) > 1 and tok[1].isdigit() else 1)

def _split(s):
    """'P2S0S0' -> ['P2','S0','S0']."""
    out, i = [], 0
    while i < len(s):
        if i + 1 < len(s) and s[i + 1].isdigit():
            out.append(s[i:i + 2]); i += 2
        else:
            out.append(s[i]); i += 1
    return out

def _cell(cell):
    """A cell is one token 'S0' OR a vertical stack ['S0','S0']. Returns (parsed_tokens, width, height)."""
    toks = [cell] if isinstance(cell, str) else list(cell)
    parsed = [_parse1(t) for t in toks]
    w = max(DIM[o][t][0] for o, t in parsed)
    h = sum(DIM[o][t][1] for o, t in parsed) + GAP * (len(parsed) - 1)
    return parsed, w, h

def _row(spec, gap):
    """One horizontal row of cells. spec = 'P2S0' (flat) or a list of cells where a cell may be a
    vertical stack, e.g. ['P2', ['S0','S0']] = big portrait + a column of two small squares.
    Returns (rel_pieces, width, band_height)."""
    cells = _split(spec) if isinstance(spec, str) else list(spec)
    info = [_cell(c) for c in cells]
    band_h = max(h for _, _, h in info)
    x, pieces = 0.0, []
    for parsed, w, h in info:
        y = (band_h - h) / 2.0                       # centre the cell block within the row band
        for o, t in parsed:
            pw, ph = DIM[o][t]
            pieces.append([x + (w - pw) / 2.0, y, pw, ph, o, t])   # centre each piece in its cell width
            y += ph + gap
        x += w + gap
    return pieces, (x - gap), band_h

def rows(*specs, gap=GAP, vgap=None):
    """Stack rows top->bottom, centre each horizontally. Returns (slots%, aspect)."""
    vgap = gap if vgap is None else vgap
    laid, y, widths = [], 0.0, []
    for spec in specs:
        pcs, rw, bh = _row(spec, gap)
        laid.append((pcs, y, rw)); widths.append(rw); y += bh + vgap
    total_h = y - vgap
    total_w = max(widths)
    slots = []
    for pcs, ry, rw in laid:
        offx = (total_w - rw) / 2.0
        for x, yo, w, h, o, t in pcs:
            slots.append([round((x + offx) / total_w * 100, 1),
                          round((ry + yo) / total_h * 100, 1),
                          round(w / total_w * 100, 1),
                          round(h / total_h * 100, 1), o, t])
    return slots, round(total_w / total_h, 3)

def grid(cols, rows_n, token="S1", gap=GAP):
    """Uniform cols x rows grid of one orient+tier token (e.g. 'S1', 'P2')."""
    return rows(*([token * cols] * rows_n), gap=gap)

# ---- SECTION 2: THE CATALOG (design new layouts here) -----------------------
# Each entry: (frame_count, "Name", spec_call). Mixed orientations welcome.
# Names borrowed from the Mixtiles arrangements they were inspired by, so we
# keep the good ideas while owning the (correct) geometry.
CATALOG = [
    # === FULL MATRIX 3–12 ========================================================
    # Every count has: a clean grid/row option, a mixed-ORIENTATION option, and
    # (up to 9) a mixed-SIZE "hero" option. Sizes are baked & LOCKED (D1). All
    # proportions cm-true. Aspects kept ~0.55–2.2 so nothing letterboxes to a sliver.

    # --- 3 ---
    (3, "Triptych",           rows("P1P1P1")),                       # three portraits in a row
    (3, "Captured Affection", rows("S1P1", "L1")),                   # mixed orientation
    (3, "Hero & Stack",       rows(["P2", ["S0", "S0"]])),           # mixed size: big portrait + two stacked squares

    # --- 4 ---
    (4, "Timeless Quartet",   grid(2, 2, "S1")),
    (4, "The Perfect Four",   rows("L1P1", "P1L1")),                 # mixed orientation pinwheel
    (4, "Hero & Three",       rows("L2", "S0S0S0")),                 # mixed size: big landscape over three small

    # --- 5 ---
    (5, "The Joyful Five",    rows("S1S1S1", "S1S1")),               # 3 over 2
    (5, "Five Cross",         rows("S1", "S1S1S1", "S1")),           # plus / diamond
    (5, "Center Hero",        rows([["S0", "S0"], "P2", ["S0", "S0"]])),  # mixed size: tall hero, stacked pairs

    # --- 6 ---
    (6, "Six Grid",           grid(3, 2, "S1")),
    (6, "Beautiful Lines",    grid(3, 2, "P1")),                     # six portraits
    (6, "Feature Six",        rows("S0P2S0", "S0P2S0")),             # mixed size: two portrait heroes among four small

    # --- 7 ---
    (7, "The Sweet Seven",    rows("S1S1", "S1S1S1", "S1S1")),       # 2/3/2
    (7, "Seven Story",        rows("S1S1S1", "P1", "S1S1S1")),       # 3 / portrait / 3
    (7, "Hero Seven",         rows([["S0", "S0", "S0"], "L2", ["S0", "S0", "S0"]])),  # mixed size: wide hero flanked by two stacks of three

    # --- 8 ---
    (8, "Eight Grid",         grid(4, 2, "S1")),
    (8, "Eight Story",        rows("P1S1S1P1", "P1S1S1P1")),         # mixed orientation
    (8, "Hero Eight",         rows("S0S0S0S0", "L2", "S0S0S0")),     # mixed size: wide hero banded in small squares

    # --- 9 ---
    (9, "Nine Grid",          grid(3, 3, "S1")),
    (9, "Heartfelt Nine",     rows("S1S1S1S1", "P1", "S1S1S1S1")),   # 4 / portrait / 4
    (9, "Hero Nine",          rows("S0S0S0", "S0L2S0", "S0S0S0")),   # mixed size: landscape hub in a grid

    # --- 10 ---
    (10, "Ten Grid",          grid(5, 2, "S1")),
    (10, "Ten Moments",       rows("S1S1S1", "S1S1S1", "S1S1S1", "L1")),  # 3x3 + a base landscape

    # --- 11 ---
    (11, "Loving Life",       rows("S1S1S1S1", "S1L1S1", "S1S1S1S1")),    # landscape hub
    (11, "Eleven Grid",       rows("S1S1S1S1", "S1S1S1", "S1S1S1S1")),

    # --- 12 ---
    (12, "Twelve Grid",       grid(4, 3, "S1")),
    (12, "Twelve Lines",      grid(4, 3, "P1")),                     # twelve portraits
]

# ---- SECTION 3: EMIT --------------------------------------------------------
def emit(path):
    by_count = collections.defaultdict(list)
    for count, name, (slots, aspect) in CATALOG:
        assert len(slots) == count, f"{name}: {len(slots)} slots but declared {count}"
        by_count[count].append({"name": name, "aspect": aspect, "slots": slots})
    L = []
    L.append("/* Auto-generated by gen-wall-layouts.py — DESIGNED layouts in our own cm grid.")
    L.append("   Keyed by frame count. Each preset: {name, aspect (w/h), slots:[[l,t,w,h,orient],...]} in % of the wall.")
    L.append("   orient: P portrait | L landscape | S square. Proportions are cm-true by construction")
    L.append("   (module: S 5x5, P 5x7, L 7x5 units) — a square and a portrait always share the 50 cm width.")
    L.append("   Mixtiles (docs/mixtiles-positions.json) is kept only as an IDEA library; geometry is ours. */")
    L.append("const WALL_LAYOUTS = {")
    for c in sorted(by_count):
        L.append(f"  {c}: [")
        for e in by_count[c]:
            slots = ",".join("[" + ",".join(f'"{x}"' if isinstance(x, str) else str(x) for x in s) + "]" for s in e["slots"])
            L.append(f'    {{ name:"{e["name"]}", aspect:{e["aspect"]}, slots:[{slots}] }},')
        L.append("  ],")
    L.append("};")
    L.append("if (typeof module!=='undefined') module.exports = WALL_LAYOUTS;")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print("layouts written:", sum(len(v) for v in by_count.values()))
    print("by count:", {c: len(by_count[c]) for c in sorted(by_count)})

if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wall-layouts.js")
    emit(out)
    print("file:", out)
