# Latenca — archiwum wersji Home

Zasada: **nic nie nadpisujemy.** Każda wersja strony głównej zostaje zamrożona, żeby zawsze można było do niej wrócić.

## Gdzie co jest
- **Wersja robocza (zawsze najnowsza):** `mockups/01-home.html`
- **Zamrożone wersje HTML:** `mockups/versions/01-home-vN.html` — otwórz w przeglądarce, żeby zobaczyć starą wersję na żywo
- **Screeny + opisy per wersja:** `review/vN/` (desktop / tablet / mobile PNG + `CHANGES-vN.md` jeśli jest)

## Wersje

| Wersja | Co to jest | Plik HTML |
|--------|------------|-----------|
| **v1** | Pierwszy kompletny, responsywny Home — „bardzo dobry sklep premium" (hero, shop by room, curated sets, artyści, kategorie, galeria Discover) | `mockups/versions/01-home-v1.html` |
| **v2** | „Confidence-first" — duży kafel „Design my wall" jako konsultacja, chipy AI, mniej treści, przemodelowana kolejność sekcji | `mockups/versions/01-home-v2.html` |
| **v3** | „Product-led" — Home jako **produkt (AI Wall Designer)**, nie sklep: demo inteligencji, narracja pytań, usunięta galeria Discover i kategorie | `mockups/versions/01-home-v3.html` |

## Jak dodajemy kolejną wersję (konwencja na przyszłość)
1. Pracujemy na `mockups/01-home.html`.
2. Gdy wersja jest gotowa: kopiujemy ją do `mockups/versions/01-home-v{N+1}.html`.
3. Robimy screeny do `review/v{N+1}/` (desktop/tablet/mobile) + opis `CHANGES-v{N+1}.md`.
4. Bieżący plik zostaje najnowszą wersją; stare pozostają nietknięte.
