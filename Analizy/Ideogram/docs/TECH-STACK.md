# TECH-STACK — Ideogram (obserwacja) + rekomendacja

## Zaobserwowane
- Frontend: Next.js/React, font Manrope.
- Własne REST API /api/... (bez zewn. BaaS widocznego publicznie).
- Model kredytowy (fast/slow), plany + Upgrade.
- Publiczne API dla developerów + Dashboard.

## Rekomendacja dla NAS
- Frontend: Next.js (App Router) + Tailwind + shadcn/ui; masonry feed (np. wirtualizacja) do Explore.
- Backend: Node/Fastify lub Python/FastAPI (Python bliżej ekosystemu ML) + kolejka (BullMQ/Celery/SQS).
- Modele: workery GPU (self-host lub dostawca), rejestr modeli + training pipeline dla custom.
- DB: PostgreSQL + Prisma/SQLAlchemy + pgvector (similarity/feed).
- Cache/kolejki: Redis.
- Storage: S3/R2 z sygnowanymi URL; CDN dla obrazów.
- Billing/kredyty: Stripe + własny licznik kredytów per model/speed.
- Obserwowalność: Sentry + analityka produktowa.
- Publiczne API + dashboard developerski (klucze, limity).

## Uzasadnienia
- Kolejka+GPU: generacja i training są długie i kosztowne.
- pgvector: feed, "podobne", moderacja duplikatów, rekomendacje.
- Kredyty per model+speed: monetyzacja i kontrola kosztów GPU.
