# TECH-STACK — Mixtiles (obserwacja) + rekomendacja

## Zaobserwowane u Mixtiles
- Frontend: **Remix** (React), SSR.
- Płatności: **Stripe**.
- Wyszukiwanie katalogu: **Algolia** (+ Algolia Analytics).
- Analityka/CRM: **Amplitude**, **Braze**, **Intercom** (czat wsparcia).
- Marketing: Pinterest, Facebook Pixel, TikTok, Impact (afiliacja), Google Ads.
- Monitoring: **Sentry**.
- Dostępność: nakładka accessiBe (acsbapp.com).

## Rekomendacja dla NAS
- Frontend: **Next.js (App Router)** lub **Remix** — SSR pod SEO katalogu, streaming pod AI/advisor. Tailwind + shadcn/ui, Framer Motion.
- Backend: **Node + Fastify/NestJS** (TypeScript), REST + SSE.
- DB: **PostgreSQL + Prisma + pgvector**; Redis (cache/kolejki).
- Wyszukiwanie: **Algolia** lub self-host **OpenSearch/Typesense**.
- AI: usługi generatywne (image-to-image/dyfuzja) za kolejką (BullMQ/SQS); LLM do advisora.
- Płatności: **Stripe**.
- Storage: S3/R2 z sygnowanymi URL.
- Obserwowalność: Sentry + PostHog (privacy-friendly), piksele reklamowe za zgodą.
- Wieszanie: replikować UX "peel & stick / magnetic" po stronie produktu fizycznego (to element brandu, nie kod).

## Uzasadnienia skrótowo
- Remix/Next: SSR ważny dla SEO tysięcy stron sztuki i szybkiego edytora.
- Algolia: gotowe wyszukiwanie/faceting katalogu — szybciej do MVP.
- Kolejka do AI: generacja jest wolna i kosztowna, musi być asynchroniczna.
