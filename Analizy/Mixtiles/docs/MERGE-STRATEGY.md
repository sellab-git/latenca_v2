# MERGE-STRATEGY — połączenie Fy! + Mixtiles w jeden system "2026"

## Wizja
Jeden produkt, w którym AI-advisor (siła Fy!) prowadzi użytkownika od pomysłu do gotowej, spersonalizowanej ściany produkowanej i wieszanej w stylu Mixtiles.

## Zunifikowany przepływ
1. Wejście podwójne (jak Fy!): quiz LUB brief w języku naturalnym + opcjonalny upload zdjęcia wnętrza.
2. Advisor ekstrahuje intencję → proponuje kierunek (paleta, styl, układ).
3. Trzy źródła treści zbiegają się (jak Mixtiles):
   - własne zdjęcia użytkownika (edytor),
   - generacja AI photo-to-art z motywów,
   - katalog gotowej sztuki + kurowane układy Gallery Walls.
4. Advisor komponuje ścianę: dobiera prace/układ, nadaje nazwę kuracji, tłumaczy "dlaczego".
5. Edytor WYSIWYG (siła Mixtiles): rama / rozmiar / efekt / border — personalizacja per-tile z ceną liczoną na żywo.
6. Wizualizacja ściany: start od mockupów 2.5D, docelowo inpainting w realnym zdjęciu wnętrza użytkownika.
7. Zapis "moja ściana" + udostępnienie (link, obraz OG) jako artefakt i kanał wirusowy.
8. Checkout (Stripe) → produkcja/druk → wysyłka → magnetyczne wieszanie "peel & stick".

## Podział ról
- **Fy! (advisor)** = mózg doboru: quiz + brief, kuracje z uzasadnieniem, chat iteracyjny, "For You".
- **Mixtiles (produkcja)** = ręce i sklep: edytor ram/rozmiarów/efektów, gotowe layouty Gallery Walls, generatory photo-to-art, mechaniki handlowe, magnetyczne wieszanie, checkout.

## Co bierzemy z każdej strony
### Z Fy!
- Konwersacyjny advisor + quiz jako podwójne wejście.
- Nazwane kuracje z wyjaśnialnością ("dlaczego ta praca/układ").
- Rekomendacje "For You" z pamięcią sesji i kontekstem.
- Chat, który zawsze kończy się konkretnym outputem na ścianie.

### Z Mixtiles
- WYSIWYG edytor: rama (Frameless/Black/White/Oak/Wide.../Canvas), rozmiar (28×21…69×50), efekt (Original/Silver/Noir/Vivid/Dramatic), border.
- Gotowe kurowane układy ścian (szablony ze slotami) z wymiarami i wyceną.
- Generator AI photo-to-art z motywów (upload → stylizacja → osadzenie).
- Katalog gotowej sztuki (wyszukiwanie typu Algolia).
- Mechaniki: próg darmowej wysyłki, kotwice cenowe (przekreślona cena), BEST SELLER.
- Fizyczna innowacja wieszania (element brandu, nie kod).

## Zunifikowany model danych (skrót)
- Design (source: ADVISOR|EDITOR|GALLERY_WALL|AI|COLLECTION) → Tile[] → Asset (UPLOAD|AI_RENDER|CATALOG).
- Advisor produkuje Curation → mapowaną na Design (sloty wypełnione dobranymi/wygenerowanymi pracami).
- Wycena zawsze serwerowa: cena = f(size, frame) sumowana per-tile.

## Architektura integracji
```
[Web app]
   ├── Advisor Service (Fy!) ── LLM + pgvector (dobór, kuracje, chat)
   ├── Editor/Design Service (Mixtiles) ── tiles, layouty, wycena serwerowa
   ├── AI Generation Service ── photo-to-art (kolejka + modele + storage)
   ├── Catalog Service ── sztuka (Algolia/OpenSearch + DB)
   ├── Order/Checkout ── Stripe
   └── Fulfillment ── druk, wysyłka, statusy
[Postgres+pgvector] [Redis] [Object storage] [Queue]
```
Most: Advisor zwraca kurację → Design Service tworzy Design z tiles → Editor pozwala dopracować → Checkout.

## Przewaga vs każdy z osobna
- Fy! sam: świetny dobór, słaby pipeline produktowy.
- Mixtiles sam: świetny produkt, ręczne odkrywanie treści (bez doradcy).
- **Połączenie**: prowadzone doradztwo AI → natychmiastowa, dopracowana, spersonalizowana ściana → produkcja i wieszanie. To jest różnicowanie.

## Kolejność wdrożenia (skrót — pełne w ROADMAP.md)
1. Rdzeń edytora + wycena + checkout (Mixtiles-core).
2. Advisor (brief → kuracja → Design) wpięty w edytor.
3. Quiz + chat iteracyjny + "For You".
4. Generatory photo-to-art i katalog.
5. Inpainting w zdjęciu wnętrza (przewaga v2).

## Ryzyka
- Złożoność integracji trzech pipeline'ów → wdrażać etapami, advisor jako warstwa nad gotowym edytorem.
- Koszt/latencja generacji i wizualizacji → 2.5D najpierw, AI za flagą.
- Prawne: własne teksty/grafiki/nazwy, brak kopiowania 1:1 Fy!/Mixtiles.
