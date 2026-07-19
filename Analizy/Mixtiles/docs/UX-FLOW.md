# UX-FLOW — Przepływy Mixtiles

## Wspólny rdzeń
Każda ścieżka kończy się tym samym: kafelek(i) → personalizacja (rama/rozmiar/efekt/border) → koszyk → checkout → wysyłka → magnetyczne wieszanie.

## A. Frame Your Photos (edytor WYSIWYG) — `/photos`
1. Wejście do edytora z canvasem prezentującym tiles (poziomy scroll między kafelkami).
2. Dolny pasek narzędzi: **Frame | Size | Effect | Border | (+ dodaj zdjęcie)**.
3. **Frame**: panel "Select Frame" — Frameless, Black, White, Oak (+$3), Wide Black/White/Walnut (+$6), Canvas (+$20). Podgląd rogu ramy.
4. **Size**: "Select Size" — karuzela rozmiarów z ceną "each" (28×21 … 69×50 cm). Zaznaczony aktywny.
5. **Effect**: "Select Effect" — miniatury filtrów (Original, Silver, Noir, Vivid, Dramatic…).
6. **Border**: obramowanie wewnętrzne.
7. Koszyk w prawym górnym rogu aktualizuje kwotę na żywo; pasek "Free shipping + 25% off" pokazuje próg.
8. "Done" zamyka panel, zmiany widoczne natychmiast na tile.

### Zasady UX
- Zmiany są natychmiastowe i wizualne (WYSIWYG).
- Personalizacja per-tile (każdy kafelek osobno).
- Cena liczona per-tile i sumowana w koszyku na żywo.

## B. Photo-to-Art / Pet Portraits (generator AI) — `/photo-to-art`
1. Galeria motywów (karty z przykładami + przycisk "Create"): The Photoshoot, Bath time, Sleepy, High Society, Pet Anatomy, Guilty as charged, Extreme sports, Kitchen tails, Clean & fluffy.
2. Każda karta ma karuzelę przykładów i miniaturę "źródłowego" zdjęcia (pokazuje transformację input→output).
3. Klik "Create" → modal **"Upload Pet Photo"** (duży przycisk "+").
4. Po uploadzie: generacja AI w wybranym stylu → warianty osadzone w ramie/na ścianie.
5. Wybór wariantu → przejście do personalizacji (rama/rozmiar) → koszyk.

### Zasady UX
- Motyw jako punkt startowy (nie pusty prompt) — obniża próg wejścia.
- Pokazanie "before/after" buduje zaufanie do jakości AI.
- Generacja jest środkiem do produktu fizycznego, nie celem samym w sobie.

## C. Gallery Walls (kurowane układy) — `/browse`
1. Filtr rozmiaru: Small / Medium / Large.
2. Siatka gotowych układów z: nazwą, wymiarami (np. 104×69 cm), liczbą kafelków, ceną "From" + ceną przekreśloną, oznaczeniem "BEST SELLER".
3. Wizualizacje w realistycznych wnętrzach (sofa, sypialnia, biurko).
4. Wybór układu → wypełnienie slotów własnymi zdjęciami → personalizacja → koszyk.

### Zasady UX
- Szablon rozwiązuje problem "nie wiem jak ułożyć ścianę".
- Kotwica cenowa (przekreślona cena) + BEST SELLER = dowód społeczny.

## D. Art Collection (katalog) — `/collection`
1. "Decorate Your Walls in Minutes" → "Browse Art".
2. Przeglądanie/wyszukiwanie gotowej sztuki (kategorie, style), indeks Algolia.
3. Wybór pracy → oprawienie (rama/rozmiar) → koszyk.

## Stany brzegowe / uwagi
- Sekcje ładują się jako SPA (spinner, dynamiczne dane) — istotne dla SEO (SSR/prerender).
- Chat wsparcia (Intercom) dostępny na każdej stronie.
