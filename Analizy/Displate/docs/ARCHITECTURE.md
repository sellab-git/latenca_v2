# ARCHITECTURE — wywnioskowana + rekomendacja

## Obserwacje
- Frontend z SSR (szybkie strony produktów pod SEO tysięcy designów/fandomów).
- Bogate strony produktów (warianty, cena, promocje) renderowane serwerowo.
- Tracking: GA4/GTM (event view_item, value, google_business_vertical: retail), TikTok Pixel, Google Ads/remarketing.
- Katalog o ogromnej skali (2.5M+ pozycji) → silne wyszukiwanie/faceting.

## Rekomendowana architektura dla NAS
```
[Web (Next.js SSR/ISR)] → [API Gateway/BFF]
   ├── Catalog/Search Service ── indeks (Algolia/OpenSearch) + DB
   ├── Product/Variant Service ── warianty, macierz cen, dostępność
   ├── Pricing/Promo Engine ── reguły, kody, rabaty ilościowe, Omnibus
   ├── Marketplace Service ── twórcy, uploady, weryfikacja, royalties
   ├── Custom Print Service ── upload → walidacja druku (DPI) → preflight
   ├── Subscription Service (Club) ── perki, dostęp do dropów
   ├── Order/Checkout ── Stripe/PSP
   └── Fulfillment ── druk na metalu, wysyłka, statusy
[Postgres] [Redis] [Object storage/CDN] [Queue] [Search index]
```

## Zasady
- Wycena i promocje WYŁĄCZNIE serwerowo.
- Wyszukiwarka jako serwis pierwszej klasy (skala katalogu).
- Uploady custom z walidacją rozdzielczości pod druk.
- SSR/ISR i pełne dane strukturalne (schema.org Product) dla SEO.
