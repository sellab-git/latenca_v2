# RESEARCH — Ideogram vs Midjourney (web) — WYNIKI

> Badanie wykonane realnie w **Claude Chrome** (zalogowany: Ideogram `arturpawlowski`, Midjourney bez subskrypcji).
> Brief źródłowy: `docs/RESEARCH-ideogram-midjourney-brief.md`.
> Cel: materiał do decyzji, czy i jak przeprojektować **Home** i **Product** w stronę prostszej logiki generatorów.

## Status weryfikacji (uczciwie)

- **Desktop ~1439px** — zweryfikowane klikaniem.
- **NIE zweryfikowane — realne generowanie**: Ideogram miał 12 kredytów, Midjourney bez subskrypcji (pole odpala paywall). Sekcja „pole w akcji" opisana z widocznego UI + struktury stron, oznaczona `[WNIOSEK]` tam, gdzie nie kliknięto końcowego „generuj".
- **NIE zweryfikowane — mobile**: `resize_window` nie przeładował realnego viewportu (JS: `innerWidth` dalej 1439px). Widoku telefonu brak — do obejrzenia na realnym urządzeniu.

Legenda: `[KLIK]` = sprawdzone realnie · `[WNIOSEK]` = domysł z UI.

---

## 🎯 Najważniejsze dla nas (skrót)

1. **Jedno trwałe pole u góry, sticky, obecne między ekranami** — oba tak robią. To rdzeń „prostoty". Przenosi się do nas 1:1 (u nas = doradca, nie prompt).
2. **Midjourney = czystszy wzorzec „jedno pole na ekran"** niż Ideogram. Ideogram na Home ma **dwa** pola naraz (prompt u góry + osobny, **płatny** Search nad feedem) — dla naszej zasady „jedno okno rozmowy na ekran" to **antywzorzec**.
3. **Przełączanie obrazów w szczególe: Ideogram NIE zmienia URL** (brak wpisu w historii) — to dokładnie nasza zasada z D‑034. **Midjourney zmienia URL** przy każdym przeskoku (dokłada wpis). Tu wzorem jest **Ideogram**.
4. **„Rozmowa" u Midjourney NIE jest rozmową.** Strona Create (`/imagine`) to chronologiczny **strumień pojedynczych zleceń** (data → prompt → 4 obrazy), nie wątek czatu z turami. Poczucie rozmowy daje **trwałe pole + rosnąca historia pod spodem**, nie prawdziwy dialog. → Możemy uzyskać ten sam efekt bez budowania pełnego czatu (ważne też dla kosztów AI).
5. **Nasza strona produktu z konieczności będzie „cięższa"** niż ich — u nich panel = metadane + akcje twórcze; u nas dochodzi rozmiar/materiał/rama/cena/mockup/koszyk. **Nasza prostota musi się objawić gdzie indziej** (jedno pole, czysty feed), nie na stronie produktu.

---

## Silne wzorce — oba robią tak samo (→ adoptujemy)

- **Górny pasek = jedno dominujące pole**, przyklejone (sticky), trwa przy scrollu i przy przejściu na szczegół. `[KLIK]`
- **Brak klasycznego nagłówka** — rolę nagłówka pełni pole, a nawigacja siedzi w **lewym sidebarze**. Logo w lewym górnym rogu. `[KLIK]`
- **Progressive disclosure**: parametry (model, liczba, proporcje, styl) zwinięte do małych chipów (Ideogram) albo schowane pod jedną ikoną suwaków (Midjourney). Użytkownik widzi jedno pole i jeden przycisk „wyślij", nie formularz. `[KLIK]`
- **Feed jako grid/masonry, „cichy" w spoczynku** — kafel bez hovera to czysty obraz; podpisy i akcje pojawiają się dopiero na hover. `[KLIK]`
- **Ciemny motyw, treść niesie kolor**, UI schodzi do tła. `[KLIK]`
- **Home = pole + od razu katalog pod spodem** (Midjourney w czystej formie; Ideogram z lekkim hero nad polem). `[KLIK]`
- **Nieskończone przewijanie** feedu (brak paginacji / „pokaż więcej"). `[KLIK]`

---

## Rozbieżności — tu MY wybieramy

| Temat | Ideogram | Midjourney | Nasz wybór |
|---|---|---|---|
| Liczba pól na Home | **Dwa** (prompt + osobny płatny Search) `[KLIK]` | **Jedno** na Explore `[KLIK]` | **Midjourney** — jedno pole (zasada „jedno okno na ekran") |
| Przełączanie obrazów w szczególe | **URL się NIE zmienia** `[KLIK]` | URL zmienia się co przeskok `[KLIK]` | **Ideogram** — zgodne z D‑034 (brak wpisu w historii) |
| Przeglądanie vs tworzenie | Scalone w Home (Home ≈ Explore) `[KLIK]` | Rozdzielone (Explore = cudze, Create = moje) `[KLIK]` | n/d — my nie tworzymy; „historia" to wynik doradcy |
| Charakter | Komercyjny/użytkowy (kategorie Poster / T‑shirt / Logo / Print on demand) `[KLIK]` | Artystyczny/społecznościowy (Moodboards, Style Creator, czysty masonry) `[KLIK]` | Nawigacja **kategoriami** bliżej Ideogram; **czystość jednego pola** bliżej Midjourney |
| Szczegół produktu | Pełna strona, URL `/g/<id>/<index>` `[KLIK]` | Lightbox nad feedem, ale routowalny URL `/jobs/<id>?index=<n>` `[KLIK]` | Do decyzji (patrz punkty decyzyjne) |

---

## Co się NIE przenosi na nas

- **UI istniejące tylko bo oni generują**: selektor modelu, liczba obrazów, proporcje jako *input*, seed, Upscale, Remove BG, Layerize text, Remix/Vary, chipy parametrów (stylize/chaos/sref/raw), kredyty/koszt generacji, Copy Prompt, negatywny prompt. `[KLIK/WNIOSEK]`
- **Warstwa społeczności generatorów**: autor + Follow, licznik polubień na cudzych generacjach, Share cudzej pracy, feed „Following", historia własnych zleceń. U nas katalog jest **kurowany do sprzedaży**, nie strumieniem cudzych generacji.
- **Ich prostota po części wynika z braku fizycznego produktu**: brak rozmiaru, materiału, ramy, ceny, koszyka, wysyłki, mockupu na ścianie. Tego u nas usunąć się nie da — dlatego strona produktu będzie bogatsza, a prostotę pokazujemy na Home i w feedzie.

---

## Trzy tezy Artura — werdykt

- **8.1 „Jedno pole u góry, nie zmienia położenia"** → PRAWDA na obu `[KLIK]`. Zastrzeżenie: Ideogram ma DRUGIE pole (Search) widoczne naraz na Home. Midjourney czystszy.
- **8.2 „Home = pole do rozmowy + od razu katalog pod spodem"** → Midjourney PRAWDA w czystej formie; Ideogram PRAWDA z hero‑tekstem i rzędem skrótów nad polem (siatka lekko odsunięta). `[KLIK]`
- **8.3 „Strony produktu podobne do zwykłej strony produktu (obraz + panel z akcjami z boku)"** → PRAWDA na obu `[KLIK]`. Ideogram = pełna strona; Midjourney = lightbox. Oba: obraz + panel + pasek miniatur.

---

## Findings po sekcjach (skrót)

**Nawigacja (0.3) `[KLIK]`**
- Ideogram sidebar: Home · My images · Collections · My likes | Prompt Builder · Image Studio · AI Apps · Models | API Dashboard/Docs | kredyty + Upgrade.
- Midjourney sidebar: Explore · Create · Edit · Organize | Personalize · Moodboards · Style Creator | Tasks · Subscribe | Dark Mode.

**Górne pole (1.1) `[KLIK]`**
- Ideogram: spinacz (upload/edit), model „✦ 4.0", liczba „🖼 4", proporcje „9:16", Auto, globus (widoczność), folder (zapis), ↑ wyślij. Placeholder: „Generate new or upload & edit…". Focus nie pokazuje historii.
- Midjourney: „Add Images", ikona suwaków (parametry), „⚡". Placeholder (bez planu): „Subscribe to start creating…". Klik w pole bez subskrypcji → modal Subscribe.

**Kafel feedu (2.2) `[KLIK]`**
- Ideogram: ~4 kolumny, kadrowanie do kafla; hover → „…", Share, autor+czas, ♥ licznik.
- Midjourney: prawdziwy masonry, obrazy nieprzycięte; hover → tylko autor + „+”(follow) i ♥. Czyściej.

**Zakładki nad siatką (2.3) `[KLIK]`**
- Ideogram: Explore/Following + kategorie All · Poster · T‑shirt · Logo · Marketing · Print on demand + osobne pole Search.
- Midjourney: Top Day / Likes + przełącznik Styles / Images / Videos.

**Poprawianie obrazu (3.3–3.4)**
- Ideogram `[KLIK — widoczne przyciski]`: Edit · Remix · Upscale · Remove BG · Layerize text. Mechanizm „chcę cieplejszy" = **Remix** (weź obraz → zmień opis → wariant).
- Midjourney `[WNIOSEK]`: Vary/Rerun/Upscale — zablokowane bez subskrypcji.
- Dla nas: oba pokazują gest „stoję na obrazie i modyfikuję go w polu" → nasz „zamień na cieplejszy", tylko u nas = **pokaż inny z katalogu**, nie generuj.

**Osobne pole „szukaj" (3.6) `[KLIK — sprawdzone dokładnie]`**
- Ideogram: DWA pola. Prompt u góry + osobny „Search all…" (🔒 płatny, paywall Plus $15/mo).
- Midjourney: jedno pole na Explore; lupa dopiero na Create.
- Wniosek: „jedno okno na ekran" → wzór **Midjourney‑Explore**.

**Szczegół (4.1–4.5)**
- Wejście: Ideogram → pełna strona `/g/<id>/<index>`; Midjourney → lightbox nad rozmytym feedem, URL `/jobs/<id>?index=<n>`. `[KLIK]`
- Układ: oba obraz + panel po prawej + pasek miniatur (Ideogram poziomy na dole, Midjourney pionowy po prawej). `[KLIK]`
- Metadane Ideogram (po „View additional details"): Type, Model, Aspect ratio, Resolution, Rendering, Seed, Created. Midjourney: prompt + negatywny prompt + chipy (stylize/chaos/ar/sref/raw/hd/profile). `[KLIK]`
- **Nawigacja ←/→ i URL** `[KLIK]`: Ideogram zmienia obraz **bez zmiany URL**; Midjourney zmienia obraz **i URL**. → dla D‑034 wzór = Ideogram.

**Explore vs Home (5.3) `[KLIK]`**
- Ideogram: Home (`/`) ≈ Explore (`/t/explore`) — ten sam widok, Home ma dodatkowy hero.
- Midjourney: Explore (cudze) i Create (`/imagine`, moje) — osobne ekrany.

---

## 🧭 Wnioski dla redesignu (moje) — PUNKTY DECYZYJNE

To badanie nie przesądza redesignu — otwiera trzy pytania. Do rozstrzygnięcia razem, zanim dotknę plików.

**D‑A. Czy jedno trwałe pole na górze zastępuje i „szukaj", i osobne czaty na każdym ekranie?**
Generatory rozwiązały „3 pola AI" nie przez jedno magiczne pole, tylko przez **rozdzielenie funkcji na ekrany** + jedno pole na ekran. Dla nas to znaczy: doradca = jedno trwałe pole u góry; wyszukiwanie katalogu = to samo pole na Home/Explore (bo tam pole jest „drzwiami"), a na stronie produktu pole = doradca reagujący na to, co wisi. Nigdzie dwa pola naraz.

**D‑B. Home: czy przechodzimy na „pole + od razu feed" w stylu Midjourney (bez dużego hero)?**
Nasz obecny Home ma hero + sekcje. Wzór Midjourney to mniej: pole + od razu katalog. Do rozważenia, czy tracimy tym coś, czego sklep potrzebuje (kategorie, „jak to działa", zaufanie), czy zyskujemy prostotę.

**D‑C. „Rozmowa" bez czatu.**
Skoro nawet Midjourney nie ma prawdziwego czatu, nasz doradca może być **trwałym polem + rosnącą historią propozycji**, a nie pełnym dialogiem. Tańsze w AI, prostsze do zbudowania, ten sam efekt „prowadzonej rozmowy". Zgodne z modelem kosztów (mniej realnych tur LLM).

**D‑D. Strona produktu zostaje „cięższa" — świadomie.**
Nasz `04-advisor` już jest konfiguratorem zakupu (rozmiar/materiał/rama/cena/mockup). Tego nie upraszczamy do ich poziomu — wyrównujemy tylko **szkielet i nawigację** z nowym Home, żeby całość była spójna.

**Czego NIE dowiedliśmy (luki do świadomej decyzji):** realny flow generowania (nie odpalony). Mobile — **uzupełnione** (patrz niżej, zrzuty Playwright).

---

## 📸 Obserwacje z realnych zrzutów (Playwright, desktop 1440 + mobile 390)

> Zrzuty leżą **lokalnie**, niepushowane: `reference/generators-screens/` (obce grafiki + branding = tylko benchmark). Poniżej to, co widać dopiero na pikselach, a czego opis tekstowy nie oddał.

**1. Kontrast gęstości jest ostry — i to on decyduje o „prostocie".** `[KLIK — widziane]`
Midjourney desktop: cienki sidebar + JEDNO pole na całą szerokość + od razu siatka 4 kolumny, prawie zero chrome, dużo bieli. Ideogram desktop: szerszy sidebar, wielki serif‑owy hero „Your next creation starts here", rząd pill‑skrótów, pole **z widocznymi chipami** (4.0/4/9:16/Auto/globus/folder), pod tym rząd kategorii + osobne pole Search. Ideogram wygląda jak **dashboard narzędzia**, Midjourney jak **galeria**. Jeśli celujemy w „proste i nowoczesne" — wzorem powściągliwości jest **Midjourney**.

**2. Pozycja pola na mobile RÓŻNI się między nimi — realny wybór dla nas.** `[KLIK — widziane]`
- **Midjourney mobile: pole na DOLE**, tuż nad tabbarem, w zasięgu kciuka (jak w komunikatorze). Zero hero. 2 kolumny. Tabbar: Menu · Explore · Create · Sign up.
- **Ideogram mobile: pole na GÓRZE** pod serif‑hero. Kategorie + Search zwinięty do samej **lupy**. 2 kolumny. Tabbar 5 pozycji z **czarnym [+] na środku**: Home · Library · [+] · Tools · Account.
→ Dla doradcy na mobile: dół (MJ) = bardziej „rozmowa" i kciukowo wygodniej; góra (Ideogram) = pole jako stały nagłówek. **To jest decyzja do podjęcia.**

**3. Oba zwijają sidebar w dolny tabbar na mobile** `[KLIK]` — wzorzec, który 15 już ma. Nasza nowa nawigacja może z tego skorzystać 1:1.

**4. Nawet Ideogram chowa drugie pole na mobile** `[KLIK]` — Search staje się samą lupą obok kategorii. Czyli „jedno widoczne pole" to wzorzec, do którego schodzą OBAJ, gdy brakuje miejsca. Wzmacnia naszą zasadę.

**5. Strona produktu na mobile: obraz dominuje, autor pod nim, akcje w DOLNYM sticky‑pasku** `[KLIK — Ideogram]`. Prawy rail z desktopu zwija się w stos pod obrazem + przyklejony pasek akcji na dole. To dokładnie nasz wzorzec `.buybar` z D‑034 (sticky „Dodaj do koszyka" na mobile).

**6. Pole naprawdę nigdy nie znika** `[KLIK — Ideogram]` — na stronie szczegółu prompt bar zostaje u góry (zwężony, ze strzałką ← wstecz). Field jest stałym elementem między ekranami, nie tylko na Home. To potwierdza wykonalność naszego „doradca = jedno trwałe pole na każdym ekranie".

**Wniosek z pikseli:** tekstowo obie strony brzmiały podobnie; wizualnie **Midjourney jest wzorem powściągliwości, Ideogram wzorem nawigacji sklepowej** (kategorie Poster/T‑shirt/Print on demand). Nasz kierunek: powściągliwość i jedno pole jak MJ + kategorie użytkowe jak Ideogram. Nowa decyzja do dodania: **pozycja pola doradcy na mobile (dół vs góra).**
