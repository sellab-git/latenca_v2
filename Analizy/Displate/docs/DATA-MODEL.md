# DATA-MODEL — propozycja (inspirowana Displate)

## Encje

### Artist
id, handle, displayName, verified(bool), payoutInfoRef, createdAt

### Design (dzieło/motyw)
id, artistId?, source[ARTIST|LICENSED|CUSTOM], title, description, tags[],
category[GAMING|ANIME|SPACE|MOVIES|...], licenseId?, imageMasterKey, createdAt

### License (dla treści licencjonowanych — osobny tor)
id, ipOwner, terms, validFrom, validTo

### Product (produkt sprzedażowy oparty o Design)
id, designId, basePriceCents, isLimited(bool), limitedEditionInfo?, bestSeller(bool)

### Variant
id, productId, finish[MATTE|GLOSS|TEXTRA], size[M|L|XL], frame[NONE|NATURAL|GRAPHITE|WHITE|BLACK],
priceCents, lowest30dPriceCents, stockStatus

### CustomOrderAsset
id, userId, uploadKey, width, height, dpiOk(bool), createdAt

### CartItem / Order
Cart: userId/sessionId, items[{variantId|customAssetId, qty}]
Order: id, userId, lines[], amountCents, currency, promoApplied[], stripePaymentIntentId, status, shippingRef, createdAt

### PromoRule
id, type[PERCENT|CODE|QUANTITY|SET], params(jsonb), validFrom, validTo

### Subscription (Club)
id, userId, tier, perks[], status, renewsAt

### Review (na poziomie sklepu/produktu)
id, source[TRUSTPILOT|INTERNAL], rating, ...

## Wyszukiwanie
- Design.tags + category + embeddings → indeks (Algolia/OpenSearch/pgvector) dla filtrowania i "podobnych".

## Compliance
- Variant.lowest30dPriceCents wymagane (Omnibus).
