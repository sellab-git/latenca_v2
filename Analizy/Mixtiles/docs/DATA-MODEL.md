# DATA-MODEL — propozycja (inspirowana Mixtiles)

> Model własny. Nie odwzorowuje schematu Mixtiles.

## Kluczowe encje

### User
id, email, createdAt, locale, marketingConsent

### Asset (upload użytkownika lub render AI)
id, userId, type[UPLOAD|AI_RENDER], storageKey, width, height, source, createdAt

### Tile (pojedynczy kafelek na ścianie)
id, designId, assetId, size[28x21|32x32|32x42|42x32|50x50|50x69|69x50],
frame[FRAMELESS|BLACK|WHITE|OAK|WIDE_BLACK|WIDE_WHITE|WIDE_WALNUT|CANVAS],
effect[ORIGINAL|SILVER|NOIR|VIVID|DRAMATIC], border, positionX, positionY, priceCents

### Design (ściana budowana przez użytkownika)
id, userId, sessionId, source[EDITOR|GALLERY_WALL|AI|COLLECTION|ADVISOR],
galleryTemplateId?, tiles[], totalPriceCents, updatedAt

### GalleryTemplate (kurowany układ)
id, name, widthCm, heightCm, tileCount, slots[], basePriceCents, listPriceCents(przekreślona), bestSeller(bool)

### ArtItem (katalog gotowej sztuki)
id, title, artist?, tags[], style, orientation, imageKey, licenseInfo, embedding(vector)

### AiTheme (motyw generatora, np. "photoshoot")
id, name, category[PET|FAMILY|KIDS|PLACES], promptTemplateId, exampleAssets[]

### AiJob
id, userId, aiThemeId, inputAssetId, status[QUEUED|RUNNING|DONE|FAILED], outputAssetIds[], createdAt

### Order
id, userId, designSnapshot(jsonb), amountCents, currency, stripePaymentIntentId, status, shippingAddressRef, createdAt

## Wektory / wyszukiwanie
- ArtItem.embedding → pgvector/Algolia dla wyszukiwania i rekomendacji.
- Powiązanie z Advisor (Fy!) po tagach + embeddingach.

## Uwaga o cenach
Cena Tile = f(size, frame). Efekty/border bez dopłaty (wg obserwacji). Trzymać cennik w tabeli konfiguracyjnej, nie hardcode.
