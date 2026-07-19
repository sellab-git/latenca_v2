# ARCHITECTURE — wywnioskowana + rekomendacja

> Na podstawie obserwacji zewnętrznych. To interpretacja, nie potwierdzony schemat Mixtiles.

## Obserwacje
- Frontend: **Remix** (React) — SSR + client hydration (globalne `__remixContext`, `__remixManifest`, `__remixRouter`).
- Edytor: canvas/DOM z personalizacją per-tile, stan cenowy liczony klientowo i weryfikowany serwerowo.
- Katalog sztuki: **Algolia** (wyszukiwanie/indeks) — sugeruje osobny serwis katalogowy.
- Płatności: **Stripe**.
- Generatory AI: osobny pipeline (upload → kolejka → model → warianty).
- Subdomeny tematyczne (kids., places.) — modularny podział treści.

## Rekomendowana architektura dla NAS
```
[Web app (Remix/Next.js)]
        │
[BFF / API Gateway]
   ├── Catalog Service (sztuka) ── Algolia/OpenSearch + DB
   ├── Editor/Design Service (tiles, layouty, wycena)
   ├── AI Generation Service (photo-to-art) ── kolejka + modele + storage
   ├── Advisor Service (dobór/kuracja — z Fy!) ── LLM + wektory
   ├── Order/Checkout Service ── Stripe
   └── Fulfillment Service (druk, wysyłka, statusy)
[Postgres] [Redis] [Object storage (S3/R2)] [Queue (BullMQ/SQS)]
```

## Zasady
- Wycena zawsze walidowana serwerowo (nie ufać cenie z klienta).
- AI generacja asynchroniczna (kolejka + webhook/poll o statusie).
- Assety (uploady, rendery) w object storage z sygnowanymi URL.
- Katalog oddzielony od edytora (różne cykle życia danych).
