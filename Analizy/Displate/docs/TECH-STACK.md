# TECH-STACK — Displate (obserwacja) + rekomendacja

## Zaobserwowane
- Frontend z SSR (React/Next-podobne), strony produktów bogate w warianty i schema danych.
- Analityka/marketing: GA4 + GTM (view_item, value, retail vertical), TikTok Pixel, Google Ads/remarketing.
- Skala katalogu wskazująca na dedykowaną wyszukiwarkę/faceting.

## Rekomendacja dla NAS
- Frontend: Next.js (App Router) + Tailwind + shadcn/ui; SSR/ISR pod SEO wielkiego katalogu; schema.org Product.
- Backend: Node/Fastify lub NestJS (TS); silnik reguł cenowych (np. własny lub biblioteka).
- DB: PostgreSQL + Prisma; Redis (cache/kolejki).
- Wyszukiwarka: Algolia lub OpenSearch/Typesense (faceting po kategoriach/fandomach).
- Płatności: Stripe (+ obsługa subskrypcji Club).
- Storage/CDN: S3/R2 + CDN dla obrazów; preflight druku (walidacja DPI).
- Analityka: GA4/PostHog; piksele za zgodą (consent).

## Uzasadnienia
- SSR/ISR: krytyczne dla SEO tysięcy stron designów/fandomów.
- Dedykowana wyszukiwarka: skala 2.5M+ pozycji.
- Rules engine: bogate mechaniki promocyjne (kody, ilościowe, sety, Club).
