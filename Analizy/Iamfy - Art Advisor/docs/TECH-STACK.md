# TECH-STACK — Stos technologiczny (rekomendacja)

> Rekomendacja własna. Fy! zaobserwowano na SvelteKit + Vite + Shopify (headless). Poniżej wybór pod NASZ produkt, z uzasadnieniem. Nie jest to wymóg kopiowania ich stacku.

## 1. Frontend

**Rekomendacja: Next.js (App Router) + React + TypeScript.**
- Uzasadnienie: największy ekosystem, łatwe zatrudnienie/utrzymanie, SSR/ISR pod SEO stron produktowych, świetne wsparcie dla streamingu odpowiedzi AI (React Server Components + Suspense).
- Alternatywa: SvelteKit (jak Fy!) — lżejszy, bardzo szybki DX; wybrać, jeśli zespół już go zna. Decyzja do podjęcia świadomie.
- UI: Tailwind CSS + biblioteka komponentów (shadcn/ui). Animacje: Framer Motion (loader kuracji, przejścia).
- Stan sesji: lekki store (Zustand) + trwałość w backendzie (sessionFingerprint).

## 2. Backend / API

**Rekomendacja: Node.js + Fastify (lub NestJS przy większym zespole), TypeScript.**
- Uzasadnienie: wspólny język z frontendem, szybki, dobre wsparcie streamingu (SSE) dla odpowiedzi agenta.
- API: REST dla operacji CRUD + SSE/streaming dla czatu i generacji. Endpointy modelowane na własnym API-SPEC.md.

## 3. Baza danych + wektory

**Rekomendacja: PostgreSQL + Prisma ORM + rozszerzenie pgvector.**
- Uzasadnienie: jedna baza na dane relacyjne (użytkownicy, przestrzenie, kuracje, produkty) i na embeddingi (semantyczne dopasowanie prac do briefu).
- pgvector: wyszukiwanie podobieństwa (brief → embedding → najbliższe prace). Kluczowe dla jakości rekomendacji.
- Cache: Redis (sesje, rate-limit, kolejki generacji, cache For You).

## 4. Warstwa AI

- **Agent LLM** (dostawca do wyboru: OpenAI / Anthropic / open-source) — ekstrakcja encji z briefu, prowadzenie czatu, nazywanie i uzasadnianie kuracji.
- **Embeddingi** — model do wektoryzacji opisów/tagów prac i briefów.
- **Wizualizacja na ścianie** — dwie opcje:
  - Kompozycja 2.5D (osadzanie pracy w gotowych mockupach ram/ścian) — tańsze, szybkie, deterministyczne.
  - Inpainting/generatywne (osadzenie w zdjęciu wnętrza użytkownika) — mocniejsza przewaga UX, wyższy koszt/latencja. Rekomendacja: start od 2.5D, inpainting jako v2.
- Orkiestracja promptów: warstwa "skills" (jak zaobserwowane u Fy! /advisor/skills) — modularne umiejętności agenta (curate, refine, name, explain).

## 5. E-commerce / katalog

- **Rekomendacja: headless commerce.** Shopify (jak Fy!) LUB Medusa.js (open-source, pełna kontrola).
- Katalog prac (produkty, warianty, formaty, ramy) + koszyk + checkout obsługiwane przez platformę commerce; nasz "advisor" jest warstwą odkrywania nad katalogiem.

## 6. Infrastruktura / DevOps

- Hosting frontendu: Vercel (Next.js) lub Netlify.
- Backend: kontenery (Docker) na Fly.io / Render / AWS ECS.
- Kolejki: BullMQ (Redis) do generacji wizualizacji.
- Storage assetów: S3-kompatybilny (R2 / S3).
- Obserwowalność: OpenTelemetry + Sentry (błędy), analityka produktowa (PostHog — self-host friendly).

## 7. Analityka i marketing (obserwowane u Fy! — do świadomego wyboru)

Fy! używa: Microsoft Clarity, Pinterest, Facebook Pixel, GTM, Trustpilot, Attentive.
- Rekomendacja prywatnościowa: zacząć od PostHog + GTM; piksele reklamowe dokładać świadomie z zgodą (consent).

## 8. Tożsamości / identyfikatory

- Fy! stosuje identyfikatory typu CUID. Rekomendacja: CUID2 lub UUIDv7 dla encji (sortowalne, bezpieczne).

## 9. Zasady jakości

- TypeScript end-to-end, walidacja schematów (Zod).
- Testy: Vitest (unit), Playwright (e2e krytycznych flow: quiz, curate, wizualizacja).
- Feature flags dla stopniowego rolloutu (np. inpainting).
