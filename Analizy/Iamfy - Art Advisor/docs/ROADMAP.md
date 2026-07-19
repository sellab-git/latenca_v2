# ROADMAP — Plan fazowy

> Plan własny. Zakłada NIE kopiowanie Fy!, lecz zbudowanie lepszego produktu na bazie wniosków z analizy. Przewaga konkurencyjna wciąż otwarta — Faza 0 pomaga ją zdefiniować.

## Faza 0 — Fundament i decyzje (1–2 tygodnie)
- Warsztat: zdefiniowanie przewagi konkurencyjnej (kandydaci: własne zdjęcie wnętrza + inpainting; lepsza wyjaśnialność doboru; nisza stylistyczna; szybkość/jakość kuracji).
- Wybór stacku (Next.js vs SvelteKit; Shopify vs Medusa).
- Setup repo, CI, środowiska, feature flags.
- Zebranie/rozszerzenie katalogu prac z tagami i embeddingami.

## Faza 1 — MVP (4–6 tygodni)
Cel: użytkownik wchodzi, dostaje trafną kurację i widzi ją na ścianie.
- Ścieżka B (brief tekstowy) + ekstrakcja encji przez agenta.
- Generacja 3 nazwanych kuracji z uzasadnieniem.
- Semantyczne dopasowanie prac (pgvector).
- Wizualizacja 2.5D (mockupy ram/ścian).
- Zapis "moja ściana" + podstawowy strip "For You".
- Integracja koszyka (headless commerce).
- Analityka zdarzeń (PostHog).

## Faza 2 — v1 (4–6 tygodni)
Cel: pełne, płynne doświadczenie i konwersja.
- Ścieżka A (Quiz strukturalny) + płynne łączenie z briefem (pamięć międzyetapowa).
- Chat iteracyjny (SSE streaming) z aktualizacją ściany w locie.
- Udostępnianie ściany (link, OG-obrazy do social).
- Dopracowany For You (wishlist/kontekst, cache).
- A/B testy nazewnictwa kuracji i CTA.

## Faza 3 — v2 (przewaga) (6–8 tygodni)
Cel: wyraźna przewaga nad Fy!.
- **Inpainting w zdjęciu wnętrza użytkownika** (upload własnej ściany) — flagowa funkcja.
- Wyjaśnialność doboru ("dlaczego ta praca") jako element zaufania i edukacji.
- Personalizacja długoterminowa (konta, historia gustu).
- Optymalizacja kosztów AI (cache embeddingów, batch, tańsze modele do rutyny).

## Faza 4 — Skalowanie i wzrost (ciągłe)
- SEO stron kuracji/artystów, treści.
- Program partnerski / artyści.
- Rozszerzenie katalogu i formatów (ramy, materiały).
- Consent-first marketing (piksele dokładane świadomie).

## Metryki sukcesu (do doprecyzowania)
- Trafność kuracji (CTR na prace, "set as my wall" rate).
- Konwersja brief → koszyk → zakup.
- Udostępnienia ścian (współczynnik wirusowy).
- Koszt AI na sesję vs wartość koszyka.

## Ryzyka
- Koszt/latencja generatywnej wizualizacji → mitigacja: 2.5D najpierw, inpainting za flagą.
- Jakość katalogu i tagów → mitigacja: inwestycja w dane w Fazie 0.
- Prawne: brak kopiowania treści/brandingu Fy!; własne teksty, grafiki, nazwy.
