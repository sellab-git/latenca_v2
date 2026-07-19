# API-SPEC — propozycja (własna)

## Katalog
GET /api/art?query=&style=&orientation=&page=  → lista ArtItem (Algolia/OpenSearch backed)
GET /api/art/:id

## Gallery templates
GET /api/gallery-templates?size=small|medium|large
GET /api/gallery-templates/:id

## Design / edytor
POST /api/designs                      → utwórz design (source)
GET  /api/designs/:id
PATCH /api/designs/:id                  → aktualizuj tiles/layout
POST /api/designs/:id/tiles             → dodaj tile {assetId,size,frame,effect}
PATCH /api/designs/:id/tiles/:tileId    → zmień size/frame/effect/border
DELETE /api/designs/:id/tiles/:tileId
POST /api/designs/:id/price             → serwerowa wycena (zwraca breakdown)

## Uploady
POST /api/uploads/sign                  → sygnowany URL do object storage
POST /api/assets                        → rejestracja assetu po uploadzie

## AI generation (photo-to-art)
GET  /api/ai/themes?category=pet|family|kids|places
POST /api/ai/jobs        {aiThemeId, inputAssetId}  → {jobId, status:QUEUED}
GET  /api/ai/jobs/:jobId                → status + outputAssetIds gdy DONE
(webhook wewnętrzny model→backend na zakończenie)

## Advisor (integracja z Fy!)
POST /api/advisor/curate {brief|quiz, context}  → kuracje + uzasadnienia
POST /api/advisor/chat   {message, sessionId}   → SSE stream + zaktualizowany dobór

## Checkout
POST /api/orders {designId} → tworzy PaymentIntent (Stripe)
GET  /api/orders/:id

## Zasady
- Wycena i finalna cena WYŁĄCZNIE serwerowo.
- AI joby asynchroniczne (poll lub SSE statusu).
- Rate limiting na uploady i AI joby.
