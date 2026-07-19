# Architektura systemu

## Widok z lotu ptaka
```
┌─────────────────────────────────────────────────────────────┐
│ FRONTEND (SvelteKit)                                         │
│ Chat UI · Quiz · Wizualizacja ściany · Shortlist · For You   │
└───────────────┬─────────────────────────────────────────────┘
                │ REST / JSON (fetch)
┌───────────────▼─────────────────────────────────────────────┐
│ BACKEND API (Node)                                           │
│ /api/spaces  /api/curate  /api/for-you  /api/visualize       │
└───┬───────────────┬───────────────┬──────────────┬──────────┘
    │               │               │              │
┌───▼────┐ ┌────────▼────┐ ┌────────▼───┐ ┌────────▼─────┐
│ DB     │ │ AI ENGINE   │ │ RECOMMENDER│ │ VISUALIZER   │
│Postgres│ │ (LLM agent) │ │ (wektory)  │ │ (inpainting) │
│+Prisma │ │ skills/tools│ │ pgvector   │ │ obraz→ściana │
└────────┘ └─────────────┘ └────────────┘ └──────────────┘
    │
┌──────▼──────┐
│ KATALOG PRAC │
│ (produkty)   │
└─────────────┘
```

## Komponenty

### 1. Frontend (SvelteKit + Vite)
SPA/SSR z reaktywnym stanem sesji. Kluczowe widoki: RoomEntry, QuizPanel, ChatThread,
CurationList, WallVisualizer, ShortlistBar, ForYouStrip. Stan sesji trzymany lokalnie
(store) + synchronizowany z backendem po `spaceId`.

### 2. Backend API (Node — Fastify lub SvelteKit endpoints)
Cienka warstwa REST. Orkiestruje: parsowanie intencji → wołanie AI Engine → zapis kuracji →
zwrot do frontu. Bez logiki biznesowej w kontrolerach (delegacja do serwisów).

### 3. AI Engine (agent LLM z narzędziami "skills")
Sercem jest agent, który: (a) ekstrahuje strukturę z free-textu (pokój, styl, paleta, budżet),
(b) decyduje o użyciu narzędzi (search katalogu, kompozycja galerii, generacja opisu),
(c) komponuje kuracje. Wzorowane na modularnej architekturze "skills". Szczegóły: docs/AI-ENGINE.md.

### 4. Recommender (wyszukiwanie wektorowe)
Każda praca ma embedding (obraz + metadane: styl, paleta, tematyka). Rekomendacje = podobieństwo
kosinusowe do wektora intencji użytkownika, z filtrami (rozmiar, budżet) i wykluczeniami
(`excludeHandles`). pgvector w Postgresie.

### 5. Visualizer (wizualizacja na ścianie)
MVP: kompozycja obrazu w ramie na predefiniowanych mockupach ścian (nakładka + perspektywa).
v1: inpainting na zdjęciu pokoju użytkownika (model dyfuzyjny / API zewnętrzne), wykrycie ściany,
skalowanie do realnych wymiarów.

## Przepływ danych (główny scenariusz "curate")
1. Użytkownik wysyła brief (quiz lub tekst) → `POST /api/curate`.
2. AI Engine parsuje intencję → buduje wektor zapytania.
3. Recommender zwraca kandydatów z katalogu.
4. AI Engine komponuje 2-3 kuracje + pisze uzasadnienia.
5. Backend zapisuje kuracje w Space → zwraca do frontu.
6. Front renderuje listę + odpala `POST /api/visualize` dla wybranej kuracji.

## Zasady niefunkcjonalne
- Bezstanowa autoryzacja sesji przez `sessionFingerprint` (+ opcjonalne konto w v2).
- Idempotentność zapisu kuracji (klucz idempotencji per request).
- Cache embeddingów katalogu (przeliczane offline przy imporcie prac).
- Rate limiting na endpointach AI (koszt LLM).
