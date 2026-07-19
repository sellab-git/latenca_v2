# ArtAdvisor — Projekt asystenta kuracji sztuki na ścianę

## Cel projektu
Budujemy konwersacyjnego asystenta AI, który pomaga użytkownikom dobrać i skomponować
sztukę na ścianę. System łączy: (1) rozmowę w języku naturalnym, (2) krótki quiz preferencji,
(3) silnik rekomendacji, (4) fotorealistyczną wizualizację obrazu w oprawie na ścianie
użytkownika, oraz (5) gotowe "kuracje" (zestawy prac) z cenami i uzasadnieniem AI.

To ma być LEPSZA wersja istniejących rozwiązań (np. Fy! Art Advisor) — patrz docs/COMPETITIVE-ANALYSIS.md
gdzie opisano ich słabości i nasze przewagi.

## Jak czytać tę dokumentację
- `docs/PRD.md` — wymagania produktowe, persony, historyjki użytkownika
- `docs/COMPETITIVE-ANALYSIS.md` — analiza konkurencji i nasze przewagi
- `docs/ARCHITECTURE.md` — architektura systemu, diagram komponentów
- `docs/DATA-MODEL.md` — schemat bazy danych (Prisma)
- `docs/API-SPEC.md` — specyfikacja endpointów REST
- `docs/AI-ENGINE.md` — logika agenta LLM, prompty, narzędzia (skills)
- `docs/UX-FLOW.md` — przepływy ekranów, stany, komponenty UI
- `docs/TECH-STACK.md` — wybór technologii i uzasadnienie
- `docs/ROADMAP.md` — plan wdrożenia w fazach (MVP → v1 → v2)

## Zasady pracy dla Claude Code
1. Zanim zaczniesz kodować nowy moduł, przeczytaj odpowiedni plik w docs/.
2. Trzymaj się schematu danych z DATA-MODEL.md i kontraktów z API-SPEC.md.
3. Pisz testy dla logiki silnika rekomendacji i parsera intencji.
4. Nie hardkoduj kluczy API — używaj zmiennych środowiskowych (patrz .env.example).
5. Wszystkie prompty do LLM trzymaj w jednym miejscu (src/lib/ai/prompts/) — łatwiej iterować.
6. Priorytet: najpierw MVP z docs/ROADMAP.md, dopiero potem funkcje v1/v2.

## Stan projektu
Faza: bootstrap. Nic jeszcze nie zaimplementowane — zaczynamy od MVP.
