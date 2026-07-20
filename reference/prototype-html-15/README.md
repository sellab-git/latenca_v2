# Latenca v1

Kurowana marka sztuki generowanej przez AI, sprzedawanej jako **fizyczne druki** (print-on-demand, Gelato) + pliki cyfrowe. Rynek docelowy: globalny (UI po angielsku, ceny w USD).

**Stan: faza przed-budową.** To repozytorium to zamrożony obraz projektu — działający prototyp UI (statyczny HTML) + spisana strategia i badania rynku. Nic jeszcze nie wystartowało; to nie jest kod produkcyjny, tylko podstawa do decyzji i przyszłej budowy w Next.js.

---

## Od czego zacząć czytanie

| Chcę... | Idź do |
|---|---|
| Zobaczyć, gdzie jesteśmy z myśleniem o biznesie | [`docs/00-status-strategiczny.md`](docs/00-status-strategiczny.md) ← **zacznij tu** |
| Zrozumieć rynek i konkurencję | [`docs/01-mapa-rynku.md`](docs/01-mapa-rynku.md) + [`docs/market-map.html`](docs/market-map.html) (klikalne) |
| Zobaczyć realne koszty i marże (dane z API Gelato) | [`docs/02-koszty-i-scenariusze.md`](docs/02-koszty-i-scenariusze.md) |
| Poznać pełną specyfikację produktu/designu | [`SPEC.md`](SPEC.md) |
| Zobaczyć, co trzeba dorobić przy prawdziwej budowie | [`NEXTJS-CHECKLIST.md`](NEXTJS-CHECKLIST.md) |

---

## Prototyp — jak obejrzeć

8 ekranów na wspólnym design-systemie (identyczna nawigacja + tokeny `:root` w każdym pliku). To **statyczny HTML** — otwórz plik w przeglądarce, albo odpal lokalny serwer, żeby działała nawigacja między stronami:

```bash
# z katalogu repo
python -m http.server 8099
# potem otwórz http://localhost:8099/Latenca-Home.html
```

| Ekran | Plik |
|---|---|
| Strona główna | `Latenca-Home.html` |
| Katalog (Explore) | `Latenca-Explore.html` |
| Kolekcje | `Latenca-Collections.html` / `Latenca-Collection.html` |
| Artyści | `Latenca-Artists.html` |
| Strona produktu | `Latenca-Product.html` |
| Koszyk / checkout | `Latenca-Cart.html` |
| Profil twórcy | `Latenca-Creator.html` |
| Builder ściany (eksperyment) | `Latenca-Builder.html` / `Latenca-Builder2.html` |

---

## Struktura repo

```
├── README.md                    ← ten plik
├── SPEC.md                      ← żywy dokument produktu/designu
├── NEXTJS-CHECKLIST.md          ← czego brakuje statycznemu prototypowi przy realnej budowie
├── Latenca-*.html               ← prototyp: 8 ekranów + warianty buildera
├── docs/
│   ├── 00-status-strategiczny.md   ← gdzie jesteśmy, co zdecydowane / wycofane / otwarte
│   ├── 01-mapa-rynku.md            ← konkurencja, modele biznesowe, prawo AI
│   ├── 02-koszty-i-scenariusze.md  ← realne koszty Gelato + scenariusze marży
│   └── market-map.html             ← klikalna mapa rynku
├── assets/                      ← grafiki pokojów użyte w prototypie
├── research/                    ← screeny referencyjne (Mixtiles, buildera)
└── archiwum-wersji/             ← archiwum wcześniejszych iteracji (historia)
```

---

## Najważniejsza otwarta decyzja

Nie „co sprzedajemy" ani „jak wygląda strona" (to mamy), tylko:

> **Do kogo umiesz dotrzeć taniej niż przez płatną reklamę?**

Prototyp jest gotowy i ładny — to najłatwiejsza część. Brakuje dystrybucji. Szczegóły w [`docs/00-status-strategiczny.md`](docs/00-status-strategiczny.md).

---

*Repozytorium prywatne. Dokumenty robocze po polsku; UI produktu po angielsku. Wszystkie liczby oznaczone jako zweryfikowane vs założone — patrz nagłówki dokumentów.*
