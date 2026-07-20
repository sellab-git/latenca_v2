import os, re, io, html
from collections import defaultdict

ROOT = r"C:\AI biznes\18. Latenca"
MOCK = os.path.join(ROOT, "prototypes", "mockups")
REF  = os.path.join(ROOT, "reference", "prototype-html-15")
ARCH = os.path.join(REF, "archiwum-wersji")
OUT  = os.path.join(ROOT, "prototypes", "index.html")

def htmls(d):
    return sorted(f for f in os.listdir(d) if f.lower().endswith(".html")) if os.path.isdir(d) else []

current = [f for f in htmls(MOCK)]
finals  = [f for f in htmls(REF)]

# our own frozen versions, grouped per screen (the record that stops us
# losing work the way product v56-v59 was lost)
ours = defaultdict(list)
for f in htmls(os.path.join(MOCK, "versions")):
    m = re.match(r"(.+?)-v(\d+)\.html$", f)
    key, n = (m.group(1), int(m.group(2))) if m else (os.path.splitext(f)[0], 0)
    ours[key].append((n, f))
for k in ours:
    ours[k].sort()

# group the archive by screen, sorted by version number
groups = defaultdict(list)
for f in htmls(ARCH):
    m = re.match(r"(.+?)-v(\d+)(?:-.*)?\.html$", f)
    if m:
        groups[m.group(1)].append((int(m.group(2)), f))
    else:
        groups[os.path.splitext(f)[0]].append((0, f))
for k in groups:
    groups[k].sort()

def links(files, base):
    return "\n".join(
        '<a class="f" href="{}/{}">{}</a>'.format(base, html.escape(f), html.escape(os.path.splitext(f)[0]))
        for f in files)

ourrows = []
for screen in sorted(ours):
    items = ours[screen]
    chips = "\n".join(
        '<a class="v" href="mockups/versions/{f}" title="{f}">{label}</a>'
        .format(f=html.escape(f), label=("v%d" % n if n else "—"))
        for n, f in items)
    ourrows.append(
        '<section class="grp"><h3>{}<span class="n">{} wersji</span></h3><div class="vs">{}</div></section>'
        .format(html.escape(screen), len(items), chips))

rows = []
for screen in sorted(groups, key=lambda s: -len(groups[s])):
    items = groups[screen]
    chips = "\n".join(
        '<a class="v" href="archiwum-wersji-link/{f}" title="{f}">{label}</a>'.replace(
            "archiwum-wersji-link", "../reference/prototype-html-15/archiwum-wersji"
        ).format(f=html.escape(f), label=("v%d" % n if n else "final"))
        for n, f in items)
    rows.append(
        '<section class="grp"><h3>{}<span class="n">{} wersji</span></h3><div class="vs">{}</div></section>'
        .format(html.escape(screen), len(items), chips))

doc = """<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Latenca — podgląd wszystkich makiet</title>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400..600&family=Inter:wght@400..700&display=swap" rel="stylesheet">
<style>
  :root{--bg:#F6F3ED;--panel:#FBF9F5;--ink:#1A1917;--muted:#6E695F;--faint:#8C8578;--line:#E7E2D8;
        --accent:#7C6CF0;--accent-soft:#ECE6FA;--accent-ink:#5F4DE0;--r:6px;
        --serif:'Lora',Georgia,serif;--sans:'Inter',-apple-system,Segoe UI,Roboto,sans-serif}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:14px;line-height:1.5}
  .wrap{max-width:1100px;margin:0 auto;padding:40px clamp(16px,4vw,32px) 80px}
  h1{font-family:var(--serif);font-size:32px;font-weight:600;margin:0 0 6px}
  .sub{color:var(--muted);margin:0 0 32px;max-width:70ch}
  h2{font-family:var(--serif);font-size:20px;font-weight:600;margin:36px 0 4px}
  .hint{color:var(--faint);font-size:13px;margin:0 0 14px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
  .f{display:block;background:var(--panel);border:1px solid var(--line);border-radius:var(--r);
     padding:13px 15px;text-decoration:none;color:var(--ink);font-weight:500;transition:.15s}
  .f:hover{border-color:var(--accent);background:#fff}
  .grp{border-top:1px solid var(--line);padding:16px 0 4px}
  .grp h3{font-size:14px;font-weight:600;margin:0 0 10px;display:flex;align-items:baseline;gap:10px}
  .n{color:var(--faint);font-weight:400;font-size:12px}
  .vs{display:flex;flex-wrap:wrap;gap:5px}
  .v{display:inline-block;background:var(--panel);border:1px solid var(--line);border-radius:999px;
     padding:4px 11px;font-size:12px;color:var(--muted);text-decoration:none}
  .v:hover{border-color:var(--accent);color:var(--accent-ink);background:var(--accent-soft)}
  .note{background:var(--accent-soft);color:var(--accent-ink);border-radius:var(--r);
        padding:12px 15px;font-size:13px;margin:0 0 28px}
</style></head><body><div class="wrap">
<h1>Latenca — wszystkie makiety</h1>
<p class="sub">Jedno miejsce na wszystko, co powstało: bieżące makiety z tego repo, finalne prototypy z projektu 15
oraz pełna historia wersji. Zanim zaczniesz projektować panel od zera, sprawdź tutaj — najprawdopodobniej już istnieje.</p>
<p class="note">Uruchom serwer w katalogu głównym repo, żeby linki działały:
<code>python -m http.server 8099</code> → <code>http://localhost:8099/prototypes/index.html</code></p>

<h2>Bieżące makiety</h2>
<p class="hint">Aktywna praca w tym repo (latenca_v2).</p>
<div class="grid">__CURRENT__</div>

<h2>Nasze wersje</h2>
<p class="hint">__OURSN__ zamrożonych migawek z tego repo — widać, jak każdy ekran dochodził do obecnej postaci.
Otwórz starszą obok bieżącej, żeby zobaczyć, co dokładnie się zmieniło.</p>
__OURROWS__

<h2>Finalne prototypy z projektu 15</h2>
<p class="hint">Zamknięty design system — punkt wyjścia do każdego nowego ekranu.</p>
<div class="grid">__FINALS__</div>

<h2>Historia wersji</h2>
<p class="hint">__ARCHN__ plików. Widać, jak każdy ekran dochodził do finalnej postaci.</p>
__ROWS__
</div></body></html>"""

doc = (doc.replace("__CURRENT__", links(current, "mockups"))
          .replace("__FINALS__", links(finals, "../reference/prototype-html-15"))
          .replace("__OURSN__", str(sum(len(v) for v in ours.values())))
          .replace("__OURROWS__", "\n".join(ourrows))
          .replace("__ARCHN__", str(sum(len(v) for v in groups.values())))
          .replace("__ROWS__", "\n".join(rows)))

io.open(OUT, "w", encoding="utf-8").write(doc)
print("napisane:", OUT)
print("biezace:", len(current), "| finalne:", len(finals), "| archiwum:", sum(len(v) for v in groups.values()))
