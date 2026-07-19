# API-SPEC — propozycja (własna)

## Katalog / wyszukiwanie
GET /api/search?q=&category=&fandom=&sort=bestselling|trending|for-you&creator=verified&cursor=
GET /api/products/:id
GET /api/products/:id/variants
GET /api/collections/:slug          # kolekcje/fandomy

## Wycena
POST /api/pricing/quote {variantId|customAssetId, qty}  → {priceCents, lowest30d, discounts[]}

## Custom
POST /api/uploads/sign
POST /api/custom-assets {uploadKey}  → {assetId, dpiOk, printableSizes[]}

## Koszyk / zamówienie
POST /api/cart/items {variantId|customAssetId, qty}
POST /api/cart/promo {code}
POST /api/orders {cartId} → Stripe PaymentIntent
GET  /api/orders/:id

## Marketplace (twórcy)
POST /api/creator/designs {uploadKey, title, tags, priceCents}
GET  /api/creator/earnings
(weryfikacja i moderacja po stronie backendu)

## Subskrypcja (Club)
POST /api/club/subscribe
GET  /api/club/status

## Zasady
- Wycena/promocje serwerowo; rabaty ilościowe i sety jako reguły.
- Publikacja designów po moderacji (prawa autorskie + jakość).
- Zwracać lowest30d w wycenie (compliance).
