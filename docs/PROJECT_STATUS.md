# PROJECT_STATUS

> Jedyne źródło prawdy o **bieżącym stanie** projektu — „gdzie jesteśmy teraz". Nadpisywane swobodnie.
> Czytaj to jako pierwsze każdą sesję.

Ostatnia aktualizacja: 2026-07-19

---

## Czym jest ten projekt (folder 18)

**Połączenie dwóch wcześniejszych projektów Latenca w jeden kierunek:**
- z **15. Latenca** (prototyp): dojrzały design system + rzemiosło (model danych, cennik, mobile step-flow, customizacja na szynach)
- z **17. Latenca** (`sellab-git/latenca`): koncept AI-doradcy + strategia + governance + Biblia dokumentów

Reguła: **17 rządzi strategią, 15 rządzi rzemiosłem.** Pełne uzgodnienie w [SPEC.md](SPEC.md), decyzja połączenia = D-017 w [DECISIONS.md](DECISIONS.md).

**Źródła (15 i 17) pozostają NIETKNIĘTE** — tu tylko czytamy/kopiujemy do 18.

---

## Bieżąca faza

**Faza 0 — szkielet i wiedza (w toku).** Zebranie całej wiedzy obu światów w jednym miejscu, scalony SPEC, governance. Bez rysowania ekranów.

Plan fazowy (każda kończy się akceptacją Artura):
- **Faza 0** — szkielet + scalony SPEC + wpięcie badań + log decyzji ← TERAZ
- **Faza 1** — design system z 15 zaadaptowany **mobile-first** (tokeny zostają, układ nowy); decyzja o akcencie
- **Faza 2** — mapa ekranów i przepływów (na papierze), rozstrzygnięcie „jak wygląda ściana na mobile"
- **Faza 3** — budowa **mockupów HTML mobile-first**, ekran po ekranie
- **Faza 4** — (później) przejście na Next.js + backend, dopiero po zamknięciu flow

---

## Zasady stałe (zablokowane 2026-07-19)
- **Tylko mockupy HTML** teraz — Next.js to Faza 4.
- **Mobile-first od 390px** — nie portujemy desktopowych układów z 15.
- **Dotykamy tylko folderu 18.**
- **Builder z 15 = próba, projektujemy od zera** pod doradcę i flow zakupu.
- **Artyści = atrybucja (a) teraz; marketplace (b) docelowo** (szew w modelu danych już teraz).

---

## Aktywne zadania (Faza 0)
- [ ] Struktura folderu + kopie źródeł do `reference/` (governance z 17, prototyp z 15, mockupy z 17) — *czeka na Bash*
- [x] Scalony `SPEC.md` (strategia 17 + rzemiosło 15 + mobile-first + moje koszty)
- [x] `PROJECT_STATUS.md` (ten plik), `README.md`
- [ ] Wpięcie badań: `COSTS.md` (realne Gelato) + `MARKET.md` (mapa rynku) — *czeka na Bash*
- [ ] `DECISIONS.md`: dopisać **D-017** (połączenie 15+17) — *czeka na Bash*
- [ ] `git init` (świeże repo, bez powiązania ze starymi) — *czeka na Bash*

---

## Aktywne hipotezy (z 17 + moje badania, zbieżne)
- Wąskie gardło = **dystrybucja/ruch**, nie katalog ani konwersja.
- **Zestawy/ściany = jedyna ekonomia, która się spina** (kolejny druk w paczce ~€0,29; pojedynczy druk na płatnym ruchu jest stratny). 🔬 COSTS.md.
- **USA ≈ 2× marża Europy.** 🔬 COSTS.md.
- **Kuracja to fosa** (sztuka AI jest towarem; gust i spójne zestawy — nie).

## Ryzyka
- **CAC ~$55–120 vs ~$40 zysku/zamówienie** → pojedyncza sprzedaż na zimnym ruchu = strata. Dlatego zestawy + rynek USA.
- **Over-building** — budowanie infrastruktury przed walidacją popytu (🔬 #1 zabójca). Dlatego mockupy HTML, nie apka; jedna ścieżka w v1, nie wszystko naraz.
- Sztuka AI: platformy tłumią masowe AI-decor; brak ochrony prawnej → marketing na realnych zdjęciach pokoi; fosa = kuracja.

---

## Następne kroki
1. Dokończyć Fazę 0 (kopie + D-017 + git — gdy Bash wróci).
2. Faza 1: design system mobile-first + decyzja o akcencie.
3. Faza 2: mapa ekranów, rozstrzygnięcie ekranu „ściany".

## Otwarte pytania
Patrz [SPEC.md](SPEC.md) sekcja 11. Najważniejsze: **dystrybucja** (do kogo docierasz taniej niż reklamą?), akcent wizualny, ekran „ściany" na mobile, zestaw warstw customizacji.
