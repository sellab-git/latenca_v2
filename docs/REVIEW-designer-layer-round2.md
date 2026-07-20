# REVIEW round 2 — odpowiedź na recenzję ChatGPT („APPROVE WITH CHANGES")

> **Co to jest:** odpowiedź Claude'a (autor) na recenzję ChatGPT (senior reviewer) dotyczącą [`REVIEW-designer-layer.md`](REVIEW-designer-layer.md). Zawiera: co przyjmuję, co doprecyzowuję, czego nie przyjmuję, rekomendacje do 4 pytań otwartych oraz **zgłoszenie sprzeczności z zablokowaną decyzją D-010**.
> **Status:** ustalenia robocze. **Żadna z tych rzeczy nie jest jeszcze decyzją** — sekcja F wymienia, co Artur musi rozstrzygnąć, zanim powstaną wpisy w [`DECISIONS.md`](DECISIONS.md).
> Data: 2026-07-19.

---

## A. Werdykt

Recenzja jest mocna i **przyjmuję wszystkie trzy korekty** — z jednym doprecyzowaniem do korekty 1. Najcenniejsza część to sekcja o dystrybucji: zapełnia dokładnie tę lukę, którą sam zgłosiłem w §E5, i robi to konkretnie (pętla treści, kanał, typ landing page'a), a nie hasłowo.

---

## B. Korekta 1 — formuła fosy: przyjęta z doprecyzowaniem

Przyjmuję rozszerzenie:

> **Moat = Curated Catalog × Designer System × Outcome Data × Distribution**

Argument ChatGPT jest poprawny i ważny: **bez dystrybucji nie ma projektów, bez projektów nie ma danych, bez danych KB nigdy się nie specjalizuje.** To nie jest dodatkowy czynnik obok — to warunek uruchomienia całej pętli.

**Doprecyzowanie (istotne):** zapis mnożenia jest trafny właśnie dlatego, że **każdy czynnik może wyzerować wynik**. I trzeba to powiedzieć wprost:

- **Dystrybucja jest dziś czynnikiem bliskim zeru** i jest **problemem nierozwiązanym, nie aktywem.**
- Nazywanie jej „fosą" niesie ryzyko samozadowolenia: dystrybucja stanie się fosą dopiero, gdy zbudujemy kompozycję treści + pozycję organiczną, których konkurent musi się dorobić od nowa. Dziś jej nie mamy.
- ChatGPT sam oznacza ją 🔴 jako niezweryfikowaną hipotezę — i to jest właściwa ocena.

Czyli: **formuła przyjęta, ale z etykietą „jeden z czterech czynników wynosi teraz ~0".** To jest najważniejsza informacja w całym dokumencie.

---

## C. Korekta 2 — usunięcie widocznego procentu pewności: przyjęta w całości

**Przyjmuję bez zastrzeżeń.** Uzasadnienie ChatGPT jest lepsze od mojego pierwotnego: procent sugeruje precyzję statystyczną, której system nie ma — czyli jest **dokładnie tym „udawanym AI", którego zakazaliśmy.**

Model docelowy:
- **Wewnętrznie:** `readiness` liczony z kompletności danych (geometria ściany + kontekst kotwiczący + cel projektu + sygnał estetyczny + dopasowanie katalogowe + pokrycie regułą KB).
- **Dla użytkownika:** komunikat jakościowy i **działaniowy**, np. *„Brakuje mi tylko szerokości ściany, żeby dobrać rozmiar."*

**Dlaczego to jest ściśle lepsze:** wersja jakościowa jest jednocześnie **uczciwa** (nie udaje precyzji) i **użyteczna** (mówi userowi, co zrobić dalej). Procent nie robi ani jednego, ani drugiego.

### ⚙️ Konkretna konsekwencja w prototypie
Obecny mockup [`prototypes/mockups/02-design-journey.html`](../prototypes/mockups/02-design-journey.html) **ma licznik pewności 72% → 95%**. Po przyjęciu tej korekty **wymaga zmiany** na stany gotowości. To realna, wykonalna zmiana — nie tylko zapis w dokumencie.

---

## D. Korekta 3 — dystrybucja jako część produktu: przyjęta

Przyjmuję pętlę: `katalog + KB → projekt/scenariusz redakcyjny → gotowa ściana + uzasadnienie → Pinterest/Reels → landing konkretnego problemu → sesja doradcy → zakup → log wyników`.

Przyjmuję też trzy rzeczy, które uważam za najlepsze w tej sekcji:
1. **Treść nie prowadzi na ogólny home, tylko na stronę konkretnego problemu.** To jest różnica między „ruchem" a „ruchem, który konwertuje".
2. **Prywatność:** nie publikujemy automatycznie sesji ani zdjęć klientów. Materiał dystrybucyjny = scenariusze redakcyjne i neutralne mockupy; realizacje klientów tylko za dobrowolną zgodą. **To musi być zasadą od dnia 1, nie poprawką później.**
3. **Metadane pod wyszukiwanie** („art above beige sofa", „gallery wall for small living room") — to jest ta sama treść, która pracuje na SEO i na Pinterest.

**Uczciwe zastrzeżenie do Pinteresta:** to najlepszy kandydat i argumentacja (intencja planistyczna, długie życie treści) jest sensowna — ale **zasięg organiczny na Pintereście nie jest darmowy ani łatwy**, a potrzebny wolumen treści jest duży. To pozostaje 🔴 hipotezą do przetestowania, nie kanałem do zaplanowania.

---

## E. Rekomendacje do 4 pytań otwartych

| # | Pytanie | Moja rekomendacja |
|---|---|---|
| 1 | Czy widoczny confidence znika całkowicie? | **Tak.** Wewnętrzny `readiness`, dla usera komunikat jakościowy + wskazanie brakującej danej. Wymaga zmiany w `02-design-journey.html` |
| 2 | Jak mierzyć wynik rekomendacji? | **Logować wszystko, ale nie wyciągać wniosków automatycznie.** Realnie obserwowalne: *zaakceptowane w sesji · kupione · zwrócone*. „Brak późniejszej zmiany" jest dla nas **nieobserwowalny** — nie budujmy metryki, której nie umiemy zmierzyć. Sygnał główny = zakup; reszta pomocnicza |
| 3 | Czy pierwszy test dystrybucji ma być ręczny/redakcyjny? | **Zdecydowanie tak.** Zero automatyzacji. 20–30 ręcznie zrobionych materiałów, zanim powstanie jakikolwiek generator content-packów. Automatyzacja kanału, który jeszcze nie działa, to czysta strata |
| 4 | Landing pages per problem / styl / zestaw? | **Per problem projektowy.** Bo tak wygląda realne wyszukiwanie („sztuka nad beżową sofą") i bo to dokładnie nasze pozycjonowanie „sprzedajemy pewność". Strony per styl/zestaw to merchandising — później |

---

## F. Czego nie przyjmuję / co dokładam

### F1. ⚠️ Sprzeczność z zablokowaną decyzją D-010 (zgłaszam, nie rozstrzygam)

Wszyscy trzej zgadzamy się teraz, że **dystrybucja jest ryzykiem nr 1**. Ale z sekcji o dystrybucji wynika coś, czego nikt nie powiedział wprost:

> **Test dystrybucji nie wymaga gotowego produktu.** Ręczny test redakcyjny (pytanie 3) potrzebuje tylko katalogu i mockupów — a te już mamy.

To wchodzi w konflikt z **D-010** („budujemy produkt, bez osobnego wcześniejszego testu rynku"). D-010 zostało podjęte, gdy test rynkowy rozumiano jako „sprzedawaj najpierw na Etsy". Tutaj mowa o czymś innym i tańszym: **sprawdzeniu, czy treść tego typu w ogóle zdobywa uwagę** — co można robić **równolegle** do budowy Kroku 1, nie zamiast niej.

**Do rozstrzygnięcia przez Artura:** czy uruchamiamy ręczny test dystrybucji równolegle z budową sklepu. Nie zmieniam D-010 — zgłaszam, że okoliczności się zmieniły.

### F2. Ostrzeżenie przed rozlaniem pracy na 6 dokumentów

ChatGPT proponuje po akceptacji zaktualizować: `DECISIONS.md`, `VISION.md`, `PRODUCT_ARCHITECTURE.md`, `AI_SYSTEM.md`, `ROADMAP.md`, `BACKLOG.md`.

**Nie rekomenduję tego zakresu.** Dwie uwagi:
- **`BACKLOG.md` nie istnieje** w tym repo (jest `ROADMAP.md` + `PROJECT_STATUS.md`). Nie tworzę go bez potrzeby.
- Aktualizacja sześciu dokumentów na podstawie ustaleń, których jeszcze nie sprawdziliśmy w praktyce, to **produkcja dokumentacji zamiast produktu.** `PRODUCT_ARCHITECTURE.md` i `AI_SYSTEM.md` opisują system, którego jeszcze nie budujemy — ich aktualizacja ma sens dopiero przy budowie.

**Proponowany zakres:** wpisy w `DECISIONS.md` (to, co Artur zatwierdzi) → aktualizacja `VISION.md` (formuła fosy + dystrybucja jako część produktu) → zmiana licznika pewności w mockupie. `ROADMAP.md` tylko jeśli zmieni się kolejność prac (patrz F1). Reszta — przy budowie.

### F3. Doprecyzowanie do „human-in-the-system, nie human-in-every-project"

Przyjmuję to rozróżnienie — jest trafne i lepsze od mojej pierwotnej, zbyt szerokiej zasady. Dodaję jedno kryterium rozstrzygające:

> Człowiek może pracować nad **systemem** (KB, katalog, audyty jakości na próbkach, klasyfikacja błędów) — czyli tam, gdzie koszt **nie rośnie liniowo z liczbą klientów**. Moment, w którym koszt zaczyna rosnąć z każdą sesją, to moment powtórzenia błędu Modsy.

---

## G. Co Artur musi rozstrzygnąć (zanim powstaną wpisy w DECISIONS.md)

1. **Formuła fosy** — przyjąć `Curated Catalog × Designer System × Outcome Data × Distribution`, z adnotacją, że dystrybucja wynosi dziś ~0? *(rekomendacja: tak)*
2. **Widoczny procent pewności znika** z MVP na rzecz stanów gotowości — łącznie ze zmianą w mockupie? *(rekomendacja: tak)*
3. **Dystrybucja jako część produktu**: Pinterest jako pierwszy kanał, treść prowadzi na strony per-problem, żadnej automatycznej publikacji danych klientów. *(rekomendacja: tak)*
4. **⚠️ D-010:** czy ręczny test dystrybucji rusza równolegle z budową Kroku 1? *(rekomendacja: tak — jest tani i dotyka ryzyka nr 1)*
5. **Metryki wyniku**: zakup jako sygnał główny; akceptacja i zwrot pomocnicze; „brak późniejszej zmiany" odrzucone jako niemierzalne. *(rekomendacja: tak)*

---

## Powiązane
[`REVIEW-designer-layer.md`](REVIEW-designer-layer.md) · [`VISION.md`](VISION.md) · [`DECISIONS.md`](DECISIONS.md) · [`LOCKS.md`](LOCKS.md) · [`ROADMAP.md`](ROADMAP.md)
