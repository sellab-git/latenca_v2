# PROJECT_STATUS

> Jedyne źródło prawdy o **bieżącym stanie** projektu — „gdzie jesteśmy teraz". Nadpisywane swobodnie.
> Czytaj to jako pierwsze każdą sesję.

Ostatnia aktualizacja: 2026-07-20

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

Gotowe: **`01-home`**, **`03-product`** (stan sprzed doradcy, nietknięty jako punkt odniesienia), **`04-advisor`** (strona produktu + doradca, D-034; skala w cm, D-035; obcięty panel, D-036).

Brakujące ekrany MVP — istnieją w projekcie 15, ale bez nowej nawigacji i bez spójności z doradcą:
- [ ] **Katalog (Explore)** — `reference/prototype-html-15/Latenca-Explore.html`
- [ ] **Koszyk + checkout** — `reference/prototype-html-15/Latenca-Cart.html`, zasady w `docs/` (zasady koszyka i checkoutu są zablokowane)
- [ ] Kolekcje i Artyści — dopiero jeśli MVP ich naprawdę potrzebuje (artyści = sama atrybucja)

Do decyzji po drodze:
- [ ] Wymienić `dresser-zoom.webp` albo ograniczyć ten pokój do ≤50×70 (D-035 — kadr nie mieści 70×100)
- [ ] Uzupełnić opisy wersji `01-home` i `02-design-journey` w `versions/labels.json` (dziś puste wiersze w indeksie)

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
