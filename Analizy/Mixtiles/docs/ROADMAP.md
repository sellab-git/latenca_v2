# ROADMAP — Mixtiles jako filar wall-art 2026

Roadmapa wdrożenia wzorców z Mixtiles do naszego produktu. Mixtiles wnosi przede
wszystkim filar **personalizacji + podglądu na ścianie + prostoty produktu (montaż
bez wiercenia) + błyskawicznego, mobilnego checkoutu**.

> Zakres: wzorce, mechanika i architektura — nie kopiowanie treści, grafik, brandingu
> ani nazewnictwa Mixtiles.

## Faza 0 — Fundament (0–4 tyg.)
- Model danych zdjęcia/dzieła użytkownika: upload, przechowywanie, warianty kadru.
- Podstawowy pipeline obróbki obrazu (kadrowanie, skalowanie, poprawki jakości).
- Definicja produktu: rozmiary kafli/płyt, wykończenia, sposób montażu.
- Prywatność uploadów użytkownika (przechowywanie, retencja, usuwanie).

## Faza 1 — Wall Preview Engine (4–10 tyg.)
- Podgląd pojedynczego dzieła na ścianie (skala, proporcje, ramka).
- Tryb „na własnym zdjęciu ściany" (upload pokoju → nałożenie dzieła).
- Kadrowanie i dopasowanie w czasie rzeczywistym.
- Optymalizacja pod mobile (główny kanał tego filaru).

## Faza 2 — Układy galerii / gallery wall (10–18 tyg.)
- Kompozytor układów wielu dzieł (siatki, symetrie, odstępy).
- Sugestie układów w zależności od liczby i proporcji dzieł.
- Podgląd całej ściany galeryjnej przed zakupem.
- Zapisywanie i edycja projektu ściany (powrót do koszyka).

## Faza 3 — Personalizacja i treść (18–26 tyg.)
- Edycja/filtry/style dla zdjęć użytkownika.
- Integracja z Generation Service (Ideogram) — generowanie brakujących elementów
  układu zamiast wyłącznie uploadu.
- Integracja z Advisorem (Fy!) — dobór stylu/palety do wnętrza użytkownika.

## Faza 4 — Commerce i konwersja (26–34 tyg.)
- Błyskawiczny, mobilny checkout (jak najmniej kroków od projektu do zakupu).
- Koszyk „całej ściany" (wiele kafli jako jeden projekt).
- Up-sell układów (dokup kolejnych elementów do istniejącej ściany).
- Trust Layer: recenzje, dowód społeczny, gwarancja jakości/montażu.

## Faza 5 — Skalowanie (34+ tyg.)
- Fulfillment: pilotaż druku/produkcji kafli → multi-vendor.
- Rozszerzenie wariantów (rozmiary, wykończenia, materiały).
- Programy powrotu klienta (rozbudowa istniejącej ściany w czasie).
- Lokalizacja: waluty, języki, zgodność cenowa per rynek.

## Kamienie milowe (definicja „gotowe")
- **M1**: Wall Preview Engine → użytkownik widzi dzieło na swojej ścianie.
- **M2**: Układy galerii → projekt wieloelementowej ściany w koszyku.
- **M3**: Personalizacja + generacja → unikatowa treść w układzie.
- **M4**: Mobilny checkout → projekt ściany → zakup w minimalnej liczbie kroków.

## Ryzyka roadmapy
- Jakość podglądu na ścianie (skala/perspektywa) decyduje o zaufaniu — priorytet
  na dokładność renderu przed rozbudową funkcji.
- Prywatność uploadów (zdjęcia ścian/wnętrz użytkownika) — jasna retencja i usuwanie.
- Złożoność kompozytora galerii może przytłoczyć — sensowne domyślne układy i
  sugestie, Advisor jako warstwa upraszczająca.
- Fulfillment fizyczny — pilotaż jakościowy przed skalowaniem produkcji.
