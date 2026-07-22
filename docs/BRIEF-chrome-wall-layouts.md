# BRIEF (Claude Chrome) — kompletny zrzut logiki „Gallery Walls" Mixtiles

**Kto:** Artur w Claude Chrome (builder Mixtiles jest interaktywny — trzeba klikać).
**Cel:** zebrać **kompletny, zmierzony** zestaw danych o kompozycjach gallery-wall Mixtiles + konfiguratorze, tak żeby dało się **odtworzyć tę logikę u nas na naszych 9 rozmiarach Gelato**. Po tym zrzucie **niczego nie zgadujemy** — brakujące pola = wracamy i domierzamy.

## Zasada IP (trzymaj się jej)
Zbieramy **wzorce rozmieszczenia + wymiary + opcje konfiguratora** (fakty funkcjonalne). **Nie** kopiujemy ich zdjęć, kodu, brandu, tekstów ani ich listy rozmiarów. Nasze rozmiary są własne (Gelato). Ich układy przerabiamy na NASZE dane.

## Nasze rozmiary (na to mapujemy — NIE zmieniamy ich)
- Pion: 30×40 · 50×70 · 70×100 · Poziom: 40×30 · 70×50 · 100×70 · Kwadrat: 30×30 · 50×50 · 70×70

---

## CO JUŻ WIEM z Twoich screenów (potwierdź / popraw, nie zaczynaj od zera)
1. **Model = nazwane, SZTYWNE kompozycje.** Każda „gallery wall" to produkt z nazwą (np. *16 Snapshots*, *Symphony Of Frames*, *The Perfect Four*), stałą liczbą ramek i stałym rozmieszczeniem. Nie układasz dowolnie — wybierasz gotową kompozycję i **wypełniasz ją zdjęciami**.
2. **Warianty rozmiaru:** filtr **Small / Medium / Large** skaluje całą ścianę. Każdy produkt ma wymiar całkowity „W cm × H cm" (np. 122×79, 64×79, 97×71, 185×97).
3. **Konfigurator (zakładki):** **Frame · Border · Effect · Photos**.
   - **Frame:** Frameless, Black, White, Oak (+$48), Wide Black (+$96), Wide White (+$96), Wide Walnut (+$96), Earthy Blend (+$48), Classic Blend (+$48), Harmony Mix (+$30). *„Blend/Mix" = różne kolory ramek na jednej ścianie.*
   - **Border:** None / Shallow / Medium / Deep (to passe-partout / margines).
   - **Effect:** Original / Silver / Noir / Vivid / Dramatic (filtry zdjęcia).
   - **Photos:** dodawanie/wybór zdjęć z „✓", puste ramki widać jako pusty kontur (jak nasz placeholder).
4. **Typy kompozycji, które widziałem:** siatki jednorodne (12 Memories 4×3, 16 Snapshots 4×4, The Memory Mosaic 4×4), rzędy (Parallel Triplet 3, Soft Melodies 4, Lifting Spirits 3 duże), kwartety 2×2 (Timeless Quartet, The Perfect Four, Harmony In Four = 2 pion + 2 poziom), symetryczne wokół środka (Symphony Of Frames = 4 małe wokół 1 dużej, Bold Statement = ramki wokół dużego poziomego środka), klastry schodkowe/mieszane (Wild Visuals, Cozy Trio, Drifting Shapes, Bright And Cherished, Mirrored Memories).
5. **Ikona linijki** (obok „Zoom" w builderze, prawy-dolny róg podglądu) — prawdopodobnie pokazuje wymiary. **Użyj jej do realnych cm.**

Twoje zadanie: **potwierdzić powyższe i UZUPEŁNIĆ do kompletu** — dokładne pola niżej.

---

## CZĘŚĆ 0 — Jakie są ścieżki? (ustal raz)
- Czy oprócz **gotowych nazwanych ścian** istnieje osobny flow **„zbuduj własną / od zdjęć"**, który **generuje** układ z N zdjęć? Jeśli tak — jak działa, ile zdjęć, czy sam dobiera układ?
- Czy w obrębie jednej nazwanej ściany da się **dodać/usunąć ramkę**, czy liczba jest sztywna?
- **Zachowanie „przesuwania":** wybierz kompozycję i spróbuj — czy po dodaniu/usunięciu zdjęcia albo kliknięciu ramki układ **sam się reorganizuje** (przesuwa w lewo/prawo), czy pozostaje sztywny? Opisz DOKŁADNIE co się dzieje (to kluczowe — Artur to widział).

## CZĘŚĆ 1 — System rozmiarów (zrób RAZ, w builderze)
1. Otwórz jedną ścianę → przełącz **Small / Medium / Large**. Podaj **dokładne wymiary całkowite (W×H cm)** dla każdego wariantu.
2. Użyj **ikony linijki** → podaj **rozmiary pojedynczych ramek w cm** (dla każdego wariantu). Czy w obrębie jednej ściany ramki są jednakowe czy różne?
3. Wypisz **wszystkie odrębne rozmiary kafla i orientacje**, jakie w ogóle występują (pion/poziom/kwadrat + cm).
4. **Odstęp między ramkami (gap):** zmierz (cm) albo oszacuj jako % szerokości kafla. Stały czy zmienny?

## CZĘŚĆ 2 — Konfigurator (zrób RAZ, potwierdź listy)
Dla jednej ściany przejdź każdą zakładkę i potwierdź/uzupełnij:
- **Frame:** pełna lista + dopłaty (potwierdź moją listę wyżej). Czy „Blend/Mix" faktycznie miesza kolory ramek między kaflami?
- **Border:** None/Shallow/Medium/Deep — **co realnie zmieniają** (szerokość marginesu)? Zmierz linijką jeśli się da.
- **Effect:** lista filtrów (potwierdź).
- **Photos:** ile zdjęć wymaga ściana „N" (np. *16 Snapshots* — przycisk mówił „Add 8 Photos" mimo 16 kafli — WYJAŚNIJ mapowanie zdjęcie→kafel; czy część kafli jest prefill demo?). Czy można **zostawić puste ramki**? Jak **przycina** zdjęcie pionowe do kafla kwadratowego — środek? da się przesunąć kadr?

## CZĘŚĆ 3 — KATALOG KOMPOZYCJI (główny zrzut danych) ⭐
**Przejdź KAŻDĄ gallery-wall w filtrach Small, Medium, Large.** Dla każdej złóż rekord wg schematu niżej. Cel: pokryć **wszystkie liczby ramek (1…16+) i wszystkie typy kompozycji**.

**Najczystszy sposób na strukturę:** wejdź w ścianę → builder → **usuń/wyczyść zdjęcia, żeby zobaczyć same puste ramki** → zrób zrzut (pusta siatka pokazuje układ idealnie, jak na screenach *16 Snapshots*). Potem **linijka** → cm.

### Schemat rekordu (wypełnij per kompozycja — to jest format outputu):
```json
{
  "name": "16 Snapshots",
  "bestSeller": true,
  "frameCount": 16,
  "compositionType": "uniform-grid",         // grid | row | column | symmetric-center | staggered-cluster | mixed-cluster
  "sizeVariants": {                            // wymiar całkowity ściany per wariant
    "Small":  {"w": 97, "h": 97},
    "Medium": {"w": 130, "h": 130},
    "Large":  {"w": 175, "h": 175}
  },
  "gap": {"cm": 3, "note": "stały odstęp między kaflami"},
  "alignment": "grid",                         // grid | top-edge | centers | balanced-freeform
  "frames": [                                  // JEDNA ramka = JEDEN obiekt; kolejność dowolna
    {
      "i": 0,
      "orientation": "S",                      // P pion | L poziom | S kwadrat
      "cm": {"w": 20, "h": 20},                // z linijki (dla wariantu Medium — zaznacz który)
      "box": {"x": 4, "y": 4, "w": 21, "h": 21}// pozycja i rozmiar w % względem CAŁEJ ściany (0,0 = lewy-górny)
    }
    // ...pozostałe ramki
  ],
  "screenshot": "16-snapshots-empty.png",
  "confidence": {"box": "estimated-from-screenshot", "cm": "ruler"}  // wyraźnie: zmierzone vs oszacowane
}
```
**Ważne o `box`:** dla każdej ramki podaj przybliżone %: x, y (lewy-górny róg ramki jako % szerokości/wysokości całej ściany) oraz w, h (rozmiar ramki jako % ściany). To pozwoli mi 1:1 odtworzyć rozmieszczenie. Estymacja z pustego zrzutu jest OK — zaznacz to.

### Checklist nazw do pokrycia (z Twoich screenów — dodaj każdą, którą znajdziesz):
Parallel Triplet, Cozy Trio, Drifting Shapes, Lifting Spirits, Captured Affection · Timeless Quartet, Harmony In Four, The Perfect Four, Soft Melodies, Beautiful Lines · The Joyful Five, Symphony Of Frames · 6 Enduring Pictures, Embraced By Warmth, Boundless Moments, Dancing Lights · The Sweet Seven, Wild Visuals · Bright And Cherished · 12 Memories, Frame By Frame, Offbeat Set · 16 Snapshots, The Memory Mosaic, Mirrored Memories, Bold Statement.
(Grupuj je po liczbie ramek. Jeśli jest ich więcej — bierz wszystkie.)

## CZĘŚĆ 4 — Zachowanie i granice
- **Maksimum ramek** na jednej ścianie (widziałem 16 — sprawdź czy więcej).
- Czy są kompozycje na **1 i 2** ramki? (na screenach zaczyna się od 3 — potwierdź).
- Czy mieszają **orientacje** w jednej sztywnej kompozycji? (Harmony In Four = 2 pion + 2 poziom — potwierdź i policz ile kompozycji jest mieszanych vs jednorodnych).
- Jak wygląda **pusta ramka** w builderze (nasz odpowiednik placeholdera) — kontur? label?

---

## CO ODESŁAĆ (format)
1. **Lista rekordów JSON** (Część 3) — po jednym na kompozycję, z wypełnionymi `frames[].box` i `cm`.
2. **Zrzuty** — dla każdej kompozycji najlepiej **widok pustych ramek** (czysta struktura) + 1 render w pokoju.
3. **Część 1–2 i 4** — krótkie odpowiedzi na każde pytanie, z cyframi.
4. Przy każdej liczbie wyraźnie: **zmierzone linijką** vs **oszacowane ze zrzutu**.

## CO JA Z TYM ZROBIĘ
Zamienię rekordy na naszą matrycę `LAYOUTS` (per liczba ramek × typ kompozycji, z `box{x,y,w,h}` w %, orientacjami i odstępami), zmapuję ich rozmiary na nasze 9 Gelato, i wepnę do `05-wall` zamiast moich tymczasowych presetów — plus zdecydujemy, które typy kompozycji bierzemy na start.
