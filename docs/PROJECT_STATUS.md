# PROJECT_STATUS

> Jedyne źródło prawdy o **bieżącym stanie** projektu — „gdzie jesteśmy teraz". Nadpisywane swobodnie.
> Czytaj to jako pierwsze każdą sesję.

Ostatnia aktualizacja: 2026-07-21

---

## Czym jest ten projekt (folder 18)

**Tu odbywa się praca.** Repo: `sellab-git/latenca_v2`, publiczne, auto-push.

Linia rozwojowa projektów:
- **15. Latenca** — **baza UX/UI.** Skończony design system, 11 prototypów, 201 wersji archiwalnych. Każdy nowy ekran startuje stąd. Kopia w `reference/prototype-html-15/`
- **17. Latenca** — miejsce, gdzie pojawiły się **pomysły na zmianę systemu**: koncept doradcy, governance, briefy ekranów. Kopie w `reference/mockups-17/` i `reference/design-specs-17/`
- **18. Latenca** — **tutaj** ← praca bieżąca
- ~~19. Latenca~~ — **to był tylko test. Nic stamtąd nie bierzemy.**

Źródła (15 i 17) pozostają nietknięte — tylko czytamy i kopiujemy.

---

## Gdzie jesteśmy

**Kierunek produktu jest ustalony i zablokowany** (D-020 … D-033). Skończył się etap „co my w ogóle budujemy" — zaczyna się rzemiosło na jednej, wybranej powierzchni.

**Produkt w jednym zdaniu:** kurowany sklep z jednym momentem AI — sklep jest podłogą, doradca drzwiami frontowymi i **nigdy bramką** (D-022).

**MVP** = Krok 1 (kręgosłup sklepu) + Krok 2 (doradca) — D-030. Doradca to **jedyna** zależność od zewnętrznego AI; rozmiar, format, wykończenie i rama to zwykłe parametry produktu.

**Powierzchnia wyświetlania: płaska ściana** — i **tylko ona** dostaje teraz inwestycje (D-033). Pokoje zostają w prototypie jako przełącznik do porównania, ale bez rozbudowy. Zdjęcia klientów są **czytane, nigdy zamalowywane** (D-031).

---

## Zasady stałe

- **Tylko mockupy HTML** teraz — Next.js później
- **Mobile-first od 390px**; każdy ekran weryfikowany w przeglądarce na 390 i desktopie **zanim** zostanie pokazany (D-032)
- **Nie wymyślamy komponentów** — używamy prawdziwych klas z 15. Jeśli dobra wersja istnieje, **kopiujemy plik i edytujemy** (D-032)
- **Nic ważnego nie zostaje w scratchpadzie.** Wersje zamrażamy w `prototypes/mockups/versions/` — Product v56–v59 przepadł, bo tej zasady nie było
- 🔁 **Każdy commit zmieniający bieżącą makietę dodaje wersję do `versions/` + opis do `versions/labels.json`.** Nie na koniec sesji — **przy każdej zmianie.** Bez opisu „v1 v2 v3" nic nie mówi i nie da się wybrać, do której wrócić. *(2026-07-20: robiłem to nieregularnie i stan po kalibracji nie istniał jako plik — dało się go odzyskać z gita, ale tylko dlatego, że był w osobnym commicie.)*
- **Dotykamy tylko folderu 18**
- Artyści = atrybucja teraz, marketplace docelowo (szew w modelu danych już jest)

### Dwa warunki wiążące przy prawdziwym kodzie (Artur, 2026-07-20)

Nie są to życzenia — projektujemy pod nie **od pierwszej linijki**, bo obu nie da się dokleić później.

1. **Model musi być wymienialny w dowolnym momencie.** D-020 to zakłada, ale zapis jest łatwy do złamania przypadkiem. W praktyce: żadnych cech charakterystycznych dla jednego dostawcy na ścieżce głównej, prompty w jednym miejscu, format odpowiedzi nasz a nie ich, przełączenie dostawcy = zmiana konfiguracji, nie przepisywanie.
2. **Limity rozmów i kosztów mają być zaprojektowane, nie doklejone** — i pod stałą kontrolą. Szczegóły w `AI_COST_MODEL.md` §9–10.

⚠️ **Jedyny element, który nie może czekać: logowanie kosztu każdej sesji od pierwszej rozmowy.** Wszystkie limity w modelu kosztowym to dziś szacunki do dostrojenia na pierwszych 100 sesjach (§7). Bez logu od dnia zerowego nie będzie czym ich dostroić — a tego jednego nie da się odtworzyć wstecz.

---

## Kolejność prac (Artur, 2026-07-20) — obowiązuje

**1. System** (makiety, ogólny wygląd) → **2. Właściwy kod MVP** → **3. Dystrybucja**

⛔ **Dystrybucja jest zamknięta do czasu ukończenia MVP.** Nie wracać do niej, nie proponować testów, nie liczyć kanałów — nawet jeśli pozostaje ryzykiem nr 1. Kolejność jest świadoma.

⛔ **Skalowanie w pokojach: nie pogłębiać.** Kalibracja jest zrobiona i uczciwa — to wystarcza jako makieta. `12. Printly` ma znacznie więcej (ruch kamery zależny od rozmiaru, pełny system ram, formaty i materiały). **Analiza Printly i decyzja kopiować/zaadaptować/napisać od nowa należy do etapu prawdziwego kodu.**

---

## Aktywne zadania — etap 1: system (makiety)

**MVP = 3 ekrany (D-038):** Katalog-landing → Produkt+doradca → Koszyk. Nic więcej na ścieżce głównej.

**Cała aplikacja = „ściana"** (`CONCEPT-the-wall.md`): wspólny grunt‑ściany w `app.css`, grafiki „zawieszone" (cień), panele pływają. Szkielet z JEDNEGO źródła: `shared/shell.js` (markup, D-040) + `shared/app.css` (design‑system + cienie, D-041). Jeden system cieni (D-043).

Gotowe:
- **`01-home` = katalog‑landing** (v13). Doradca‑hero na górze (wariant C, D-042) + pełny Explore wciągnięty (D-038). Na „ścianie".
- **`04-advisor` = produkt + doradca** (v16). **MODEL D (D-046):** jeden trwały panel — doradca główną powierzchnią, tytuł+cena u góry, dok „Options + Add to cart" na dole, konfiguracja jako accordion nad rozmową. Zastąpił przełącznik trybów (D-034). Ugruntowane na Figma/Ideogram/Fy! + Rufus/NN-g.
- **`05-wall` = powierzchnia ŚCIANY** (v3) — **strona produktu JEST ścianą.** v2 = rebuild właściwą metodą (kopia `04-advisor` 1:1 + dostosowanie); dziedziczy cały panel model D + config sheet + drawery + kadry #fff/`--art-shadow-lg`. **v3 (D‑048): bez breadcrumba, bez ekranu‑bramki i „Zmień intencję"** (bramka łamała D‑022) — ściana otwiera się GOTOWA (1 praca; z katalogu = ta praca), 4 podejścia (Gotowa ściana/Od zdjęcia/Zaskocz/Dodaj pracę) = czipy doradcy przebudowujące tę samą ścianę w miejscu; obrazki = prawdziwy kurowany katalog z 04. Lewa scena 1→N slotów; panel +„Praca X z N"; dok +poziom ściany (układ ‹1/2›, liczba −N+); CTA „Dodaj ścianę do koszyka"=suma; per‑praca materiał/rozmiar/rama; N→N‑1 → zapas; zero przeciągania (D‑033). Playwright‑verified.
- **Breadcrumb usunięty z CAŁEGO projektu** (03/04/05) — D‑048. W aplikacji lokalizację pokazuje aktywna pozycja w lewym menu, nie okruszki.
- **Front‑end = ANGIELSKI** (D‑049). Cały UI po angielsku (rynek globalny, USD), kod i18n‑ready. `05-wall` przetłumaczony z PL→EN (napisy + parser czatu); reszta już była EN. Polski zostaje tylko w wewnętrznych docs/decyzjach.
- **Zamknięta lista rozmiarów Gelato** (D‑050): 9 rozmiarów, 3 na orientację (pion 30×40/50×70/70×100, poziom 40×30/70×50/100×70, kwadrat 30×30/50×50/70×70). Każda praca ma orientację; lista/etykieta/podgląd wynikają z niej.
- **Kształt ramki + reguły kadrowania** (D‑050 uzup.): ramka na ścianie ma REALNĄ proporcję wybranego rozmiaru (fit do aspect ratio, resize‑safe). Praca ma stałą orientację źródła + osobny „shape" do druku ograniczony regułą: **pion→pion|kwadrat, poziom→poziom|kwadrat, kwadrat→tylko kwadrat**. Selektor Shape w Options pokazuje tylko dozwolone; przełączenie na kwadrat docina obraz centralnie.
- **`05-wall` v4 — model placeholderów (D‑048 refinement):** niczego nie zakładamy. Slot = PUSTY (kreskowana ramka „Dodaj pracę") albo wypełniony. Wejście z menu = 1 pusty placeholder; z katalogu (`?art=`) = ta praca. Nowy slot (N→N+1) = pusty, doradca pyta „czym wypełnić?" → Zaskocz mnie / Dopasuj do reszty / Przeglądaj katalog (+ Przywróć poprzednią z zapasu). Cena/CTA liczą tylko wypełnione; CTA aktywne gdy ≥1 praca.
- **`03-product`** — stan sprzed doradcy, punkt odniesienia.

### ⚡ ZMIANA KIERUNKU (2026‑07‑21) — czytaj `docs/USER-INTENTS.md` (żywa mapa)
Artur zapytał o realny plan „Design my wall" → wyszła głęboka praca nad intencjami (178 scenariuszy → 5 podróży, recenzja ChatGPT, feasibility‑engine). **Reframe: jednostka = jedna praca; „ściana" = ZMIENNA liczba prac (1..N) kupowanych razem** (nie sztywna para); dwie drogi (gotowe układy + składanie), wzorzec Mixtiles; **strona produktu = ściana**; układy z biblioteki presetów; rozmiar należy do układu; panel dwupoziomowy. Modsy jako analogia — **zbanowane**.

### ⏭ WZNOWIENIE (2026‑07‑22, późna sesja) — `05-wall` = **v22**, wszystko wypushowane
**Układy:** decyzja A/B zdjęta — Artur chce też mieszane, więc powstał **kit do projektowania układów** (`shared/gen-wall-layouts.py`: tokeny `P/L/S`×rozmiar`0/1/2` = 9 rozmiarów Gelato jako moduły 10 cm; `rows()`/`grid()` + **stack** `["P2",["S0","S0"]]` na kompozycje „bohater"). Matryca 3–12 z **mieszanymi rozmiarami**, cm‑true z definicji. Mixtiles = tylko biblioteka pomysłów (`docs/mixtiles-positions.json` nietknięte).

**Zbudowany builder ściany + WIDOK SZCZEGÓŁÓW (główna robota sesji):**
- **Płótno 3‑warstwowe:** `#wallView` `position:fixed` pełny ekran (z1) MIĘDZY tłem‑ścianą a NAKŁADKAMI (menu/topbar/panel, z2, nieprzezroczyste); grafiki wjeżdżają POD nakładki. Akcje: **scroll = zoom** (+ przyciski −/100/+), **przeciągnij PUSTE płótno = pan**, **klik w pracę = szczegóły**.
- **D5 orientacja** pilnowana wszędzie (`reconcileToLayout()` + `swapArt`): pion→pion/kwadrat, poziom→poziom/kwadrat, kwadrat→kwadrat.
- **WIDOK SZCZEGÓŁÓW = pełny „model B" (Ideogram):** jedna przewijalna strona — góra: duża **surowa grafika** (bez ramki) + pasek **„Recently viewed"** (historia) po lewej, **panel po prawej** (reparentowany do przepływu, **odjeżdża przy scrollu**); pod foldem **katalog na PEŁNĄ SZEROKOŚĆ**. Tło `var(--bg)` wg motywu. Kolumny wyrównane (góra/dół). Powrót „× Back to wall" przywraca panel do nakładki.
- **Katalog = moduł 01-home 1:1** (Artur 3× „nie wymyślaj swojego UX"): dokopiowany brakujący CSS filtrów (`.pill/.filters/.seg/.allf/.drop/.count`); render = filterzone (pigułki + count + All filters + orientacja + Sort) + masonry `.tile` (fav/share/more/info) + Load more.

**STUBY do dokończenia:** filtry (pigułki/orientacja/sort/„All filters") są WIZUALNE, nie zawężają; brak wysuwanego panelu „All filters" (drawer — Artur: i tak pewnie usuniemy); brak dopasowania picków po palecie/nastroju (katalog filtruje tylko po orientacji). Snapshoty: `prototypes/mockups/versions/05-wall-vNN.html` + `labels.json` (do v22).

Następne (po reakcji na `05-wall`):
- [ ] **Decyzja D‑047: rozszerzyć MVP z „pojedyncza grafika" na „N prac"?** (zmienia D‑023/D‑030/D‑033) — czeka na Artura.
- [x] **Matryca układów z Mixtiles — ZROBIONE (D-051).** Zebrane wszystkie 45 ścian (pozycje z DOM edytora, zwalidowane) + config (border/kadr/mapowanie/cena). 43 różne układy → `shared/wall-layouts.js`, wpięte w `05-wall` v8: slot dyktuje pozycję+kształt, Ready-made wypełnia grafiką dopasowaną do orientacji, build-up dodaje puste sloty. Dane: `docs/mixtiles-positions.json` + `docs/mixtiles-layouts-data.json`.
- [ ] Iteracja ściany: klik w pusty slot = dodaj tu; materiał/rama na żywo na podglądzie; wpięcie „gotowych ścian" (droga A).
- [ ] **Koszyk + checkout** — po ustaleniu modelu ściany (był „następnym ekranem", teraz PO ścianie). `reference/prototype-html-15/Latenca-Cart.html`.
- [ ] Kolekcje i Artyści — poza ścieżką główną, tylko jeśli MVP ich potrzebuje.

Odłożone / do posprzątania:
- [ ] **Nakładka wymiarów na produkcie** („50×70 cm" ze strzałkami) — Artur: „temat na bardzo później". Reszta ulepszeń w `UX-CRITIQUE-landing-product.md`
- [ ] Usunąć pliki‑eksperymenty `landing-B.html`, `landing-C.html`, `landing-wall.html` (zastąpione przez `01-home` v13)
- [ ] Wymienić `dresser-zoom.webp` albo ograniczyć ten pokój do ≤50×70 (D-035 — kadr nie mieści 70×100)

## Etap 2: właściwy kod (jeszcze nie zaczynamy)

- [ ] Analiza `12. Printly` i decyzja **kopiować / zaadaptować / napisać od nowa** — ruch kamery, system ram, formaty i materiały (te same trzy zdjęcia pokoi)
- [ ] Krok 1: kręgosłup sklepu (katalog → produkt → konfigurator → koszyk)
- [ ] Baza wiedzy projektowej, warstwy A/B/D (D-024) — warunek jakości doradcy od dnia 1
- [ ] ⚠️ **Log kosztu każdej sesji od pierwszej rozmowy** — jedyna rzecz, której nie da się odtworzyć wstecz
- [ ] Przeliczyć limity kosztów na **dwa** wejścia do AI, nie jedno (`AI_COST_MODEL.md` §9)

## Etap 3: dystrybucja

- ⏸ ~~Ręczny test dystrybucji (D-028)~~ — **zamknięte do czasu MVP.** Patrz „Kolejność prac" wyżej

---

## Ryzyka

- **Dystrybucja/CAC to ryzyko nr 1**, nie produkt. W formule fosy (D-025) dystrybucja wynosi dziś **~0**. Latenca nie ma jeszcze fosy — ma projekt mechanizmu
- **CAC ~$55–120 vs ~$40 zysku/zamówienie** → pojedyncza sprzedaż na zimnym ruchu jest stratna. Stąd zestawy i rynek USA
- **Over-building** — budowa infrastruktury przed walidacją popytu. Stąd mockupy, nie aplikacja
- **Koszt AI** jest zabezpieczony sześcioma warstwami (`AI_COST_MODEL.md`); maks. ~1 zł za sesję. Sklep działa bez doradcy, więc rachunek za AI nigdy nie zatrzyma sprzedaży

---

## Otwarte pytania

- **Dystrybucja** — który kanał realnie dowozi pierwszych obcych klientów taniej niż reklama? Pinterest jest **hipotezą do testu**, nie kanałem zatwierdzonym
- **Czy przy nieznanej sztuce pokój znaczy więcej niż przy własnych zdjęciach klienta?** Mixtiles może pominąć pokój, bo emocja siedzi w treści. U nas treść jest obca. **Rozstrzygną to klienci, nie analiza**
- Akcent wizualny, zestaw warstw customizacji, marża i rynek docelowy — patrz `PRODUCT_BIBLE.md` sekcja 11

---

## Podgląd makiet

```
python -m http.server 8099    # uruchom w katalogu 18
```
→ **http://localhost:8099/prototypes/index.html** — bieżące makiety, nasze zamrożone wersje, 11 prototypów z 15 i 201 wersji archiwalnych.
**Zanim zaczniesz projektować panel od zera — sprawdź tam. Najprawdopodobniej już istnieje.**
