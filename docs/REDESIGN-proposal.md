# REDESIGN — propozycja zmian Home + Product (na bazie Ideogram/Midjourney)

> Materiał wejściowy: `docs/RESEARCH-generators.md` + zrzuty `reference/generators-screens/`.
> Cel: ustalić **kierunek** zmian dla `01-home` i `04-advisor`, zanim dotknę plików.
> Status: **propozycja do decyzji.** Nic jeszcze nie budowane.

## Kierunek w jednym zdaniu

Bierzemy od generatorów **powściągliwość i jedno trwałe pole**, a od Ideogram **nawigację kategoriami użytkowymi** — ale **nie kopiujemy ich wyglądu** (mamy swój ciepły system: kremowe tło #F6F3ED + lawenda, serif Lora). Ich stark‑white/dark to nie my.

## Zasada nadrzędna (co bierzemy / czego NIE)

**Bierzemy:**
- Jedno dominujące pole u góry, przyklejone, **obecne na każdym ekranie** (u nas = doradca).
- Progressive disclosure — parametry zwinięte do chipów, nie formularz.
- Feed „cichy" w spoczynku (kafel = obraz; podpisy/akcje dopiero na hover).
- Sidebar → dolny tabbar na mobile.
- Kategorie użytkowe w nawigacji (jak Poster/Print on demand u Ideogram).

**NIE bierzemy:**
- Ich kolorystyki i typografii (mamy swoją).
- Warstwy społeczności generatorów (autor+Follow, licznik ♥ na cudzych, Share cudzej pracy).
- UI generacji (model, seed, proporcje jako input, Upscale, Remix, kredyty).
- Ideogramowego modelu **dwóch pól naraz** (prompt + osobny Search) — to nasz antywzorzec.

---

## HOME — proponowane zmiany

**Stan dziś:** `01-home` to bogata strona marketingowa (hero + benefit + pokoje + zestawy + browse‑by‑category + polecani artyści + how‑it‑works + discover z zakładkami). Długa, wielosekcyjna.

**Co widzieliśmy u generatorów:** odwrotność — pole + od razu katalog, minimum sekcji. Midjourney nie ma nawet hero; Ideogram ma lekki hero i od razu siatkę.

**Propozycja — góra strony (nad zgięciem):**
1. Jedna linia marki/wartości (krótko, nie wielosekcyjny hero).
2. **Pole doradcy** — „drzwi frontowe" (D‑022), na całą szerokość, jak u nich.
3. **Od razu katalog** pod polem (siatka kafli‑produktów).

**Propozycja — niżej (dla tych, co przewiną):** zamiast pełnego stosu marketingowego zostawiamy **cienką warstwę zaufania**: jeden pasek „jak to działa" + pokoje/zestawy. Reszta sekcji do cięcia.

**Powód:** generatorowi wystarcza pole+siatka, bo user przychodzi, wiedząc, po co. Zimny kupujący u nas nas nie zna — sklep potrzebuje *trochę* kontekstu (co to, dlaczego, jak). Ale dzisiejsza Home ma go za dużo. Szukamy środka.

### 🔵 DECYZJA 1 — jak radykalnie zmieniamy Home?
- **A. Pełny generator:** pole + siatka, prawie nic więcej. Najodważniej, najprościej, ale sklep bez warstwy zaufania.
- **B. Hybryda (moja rekomendacja):** pole + siatka na górze, cienka warstwa zaufania pod zgięciem. Prostota generatora + minimum tego, czego potrzebuje sklep.
- **C. Zachowawczo:** zostaje bogata Home, dokładamy tylko trwałe pole i porządkujemy gęstość.

---

## POLE / WYSZUKIWANIE — koniec z „3 oknami AI"

**Problem, który sam zauważyłeś:** groziło nam kilka pól do rozmowy z AI na jednej stronie. **Jak to rozwiązali generatorzy:** nie jednym magicznym polem — tylko **jednym polem na ekran**, a funkcje rozdzielili na ekrany (nawet Ideogram search ma osobno i płatnie, MJ search tylko na Create).

**Propozycja:** doradca staje się **jedynym trwałym polem**, obecnym na każdym ekranie; **kasujemy osobny pasek wyszukiwania.**
- Na Home/katalogu: to pole = „drzwi" — piszesz, czego chcesz, ono prowadzi po katalogu.
- Na stronie produktu: to samo pole = doradca reagujący na obraz, który wisi.
- Kontekst zmienia ekran, nie liczba pól.

### 🔵 DECYZJA 2 — czym jest pole na Home?
- **A. Pole = doradca, wyszukiwanie = rozmowa z nim** („pokaż coś spokojnego, niebieskiego"). To **nasz wyróżnik** — brak osobnego search, doradca JEST wyszukiwarką. ⚠️ Uczciwie: to zakład produktowy — doradca musi dobrze ogarniać zapytania „pokaż mi…", nie tylko „doradź mi".
- **B. Pole na Home = zwykłe wyszukiwanie**, doradca dopiero na produkcie. Prościej zbudować, mniej wyróżniające.

*(Moja rekomendacja: A jako cel, ale w MVP pole może zaczynać od prostego wyszukiwania i „urastać" do doradcy — schodzimy na to przy prawdziwym kodzie.)*

---

## MOBILE — nowa decyzja z pikseli

Zobaczyliśmy realną różnicę: **Midjourney kładzie pole na DOLE** (przy kciuku, jak komunikator), **Ideogram na GÓRZE** pod hero. Oba zwijają nawigację w dolny tabbar.

### 🔵 DECYZJA 3 — gdzie pole doradcy na mobile?
- **A. Dół (jak MJ):** kciukowo wygodniej, czuje się bardziej „rozmową". ⚠️ Na katalogu „szukajka na dole" bywa mniej oczywista.
- **B. Góra (jak Ideogram):** pole jako stały nagłówek, spójne z desktopem.

*(Moja rekomendacja: A dla trybu rozmowy/produktu, ewentualnie B dla czystego katalogu — do sprawdzenia na makiecie.)*

---

## PRODUCT (`04-advisor`) — mniejsze zmiany

**Dobra wiadomość:** zrzuty **potwierdziły nasz szkielet.** Ich strona szczegółu = obraz + prawy rail z akcjami + pasek miniatur; na mobile obraz + stos pod nim + **dolny sticky‑pasek akcji** — to dokładnie nasz `.buybar` z D‑034. Produktu **nie wywracamy.** Proponowane drobne zmiany:

1. **Ujednolicić górny pasek** — pole doradcy to ten sam trwały bar, co na Home (dziś na produkcie jest osobny pasek wyszukiwania → do usunięcia, spójnie z DECYZJĄ 2).
2. **Konfigurator jako czystsze rzędy chipów** (progressive disclosure jak u nich) — ale ⚠️ **materiał zostaje pierwszy i widoczny**, bo determinuje rozmiary i ceny (to nie Mixtiles). Nie chowamy tego, co zmienia cenę.
3. **Potwierdzić dolny buybar na mobile** — zgodne z tym, co widzieliśmy, prawdopodobnie zero zmian.

**Świadoma granica:** nasza strona produktu **musi** zostać „cięższa" niż ich (rozmiar/materiał/rama/cena/mockup/koszyk — oni tego nie mają). Prostotę pokazujemy na Home i w feedzie, nie na produkcie.

---

## Czego NIE ruszamy

- Design system (kolory, typografia, tokeny) — zostaje, tylko stosowany powściągliwiej.
- Logika skali w pokojach (D‑035) — zamknięta do etapu prawdziwego kodu.
- Sam mechanizm doradcy (D‑034 jeden ekran/dwa stany) — potwierdzony, zostaje.

---

## Zebrane decyzje do ustalenia

1. **Home — radykalność:** A pełny generator / **B hybryda (rek.)** / C zachowawczo.
2. **Pole na Home:** **A doradca‑jako‑wyszukiwarka (rek., cel)** / B osobne wyszukiwanie.
3. **Pole na mobile:** **A dół (rek.)** / B góra.

Po ustaleniu tych trzech: kopiuję `01-home` i `04-advisor`, robię nowe wersje na makietach (mobile‑first, weryfikacja w przeglądarce), zamrażam w `versions/`. Nie wcześniej.
