import json, collections

P = r"C:\AI biznes\18. Latenca\docs\mixtiles-positions.json"
OUT = r"C:\AI biznes\18. Latenca\prototypes\mockups\shared\wall-layouts.js"
d = json.load(open(P, encoding="utf-8"))

def sig(w):
    return tuple(sorted((round(f["box"][0]),round(f["box"][1]),round(f["box"][2]),round(f["box"][3]),f["orient"]) for f in w["frames"]))

# We only offer P/L/S (real aspects ~0.71 / 1.0 / 1.4). A Mixtiles "banner" slot (wide-thin
# title band, ~3.0) has no equivalent in our catalogue → rework it into a centred LANDSCAPE
# (aspect 1.4) in the same band, keeping the layout. (Tall-thin <0.6 → centred PORTRAIT 0.714.)
LO, HI = 0.6, 1.55
def debanner(slots, A):
    out=[]; reworked=0
    for l,t,w,h,o in slots:
        ar=(w/h)*A
        if ar>HI:                       # wide banner → centred landscape 1.4
            cx=l+w/2; nw=1.4*h/A; out.append([round(cx-nw/2,1),round(t,1),round(nw,1),round(h,1),'L']); reworked+=1
        elif ar<LO:                     # tall-thin → centred portrait 0.714
            cy=t+h/2; nh=w*A/0.714; out.append([round(l,1),round(cy-nh/2,1),round(w,1),round(nh,1),'P']); reworked+=1
        else:
            out.append([round(l,1),round(t,1),round(w,1),round(h,1),o])
    return out, reworked

# dedup identical arrangements, keep first, collect aliases
seen = {}
order = []
for name, w in d["walls"].items():
    s = sig(w)
    if s in seen:
        seen[s]["aliases"].append(name)
    else:
        oc = w.get("overallCm", {})
        aspect = round(oc.get("w",1)/oc.get("h",1), 3) if oc else w.get("wallPxAspect",1)
        raw = [[f["box"][0],f["box"][1],f["box"][2],f["box"][3],f["orient"]] for f in w["frames"]]
        slots, rk = debanner(raw, aspect)
        seen[s] = {"name":name, "aliases":[], "aspect":aspect, "slots":slots, "reworked":rk}
        order.append(s)

# group by frame count
by_count = collections.defaultdict(list)
for s in order:
    e = seen[s]
    by_count[len(e["slots"])].append(e)

# emit JS
lines = []
lines.append("/* Auto-generated from docs/mixtiles-positions.json — real gallery-wall arrangements.")
lines.append("   Keyed by frame count. Each preset: {name, aspect (w/h), slots:[[l,t,w,h,orient],...]} in % of the wall.")
lines.append("   orient: P portrait | L landscape | S square. Positions/orientations are exact (from Mixtiles editor DOM);")
lines.append("   physical sizes are NOT copied — we map slots to our own 9 Gelato sizes via the crop rules (D-050). */")
lines.append("const WALL_LAYOUTS = {")
for c in sorted(by_count):
    lines.append(f"  {c}: [")
    for e in by_count[c]:
        notes=[]
        if e["aliases"]: notes.append("+ "+", ".join(e["aliases"]))
        if e["reworked"]: notes.append(f"banner→landscape ×{e['reworked']}")
        alias = ("  // "+" · ".join(notes)) if notes else ""
        slots = ",".join("["+",".join(str(x) if not isinstance(x,str) else f'\"{x}\"' for x in sl)+"]" for sl in e["slots"])
        lines.append(f'    {{ name:"{e["name"]}", aspect:{e["aspect"]}, slots:[{slots}] }},{alias}')
    lines.append("  ],")
lines.append("};")
lines.append("if (typeof module!=='undefined') module.exports = WALL_LAYOUTS;")
open(OUT,"w",encoding="utf-8").write("\n".join(lines)+"\n")

total = sum(len(v) for v in by_count.values())
print(f"distinct layouts written: {total}")
print("by count:", {c:len(by_count[c]) for c in sorted(by_count)})
print("\nbanner→landscape reworks:")
for c in sorted(by_count):
    for idx,e in enumerate(by_count[c]):
        if e["reworked"]: print(f"  {c} pieces · layout {idx+1} ({e['name']}): {e['reworked']} slot(s)")
print("file:", OUT)
