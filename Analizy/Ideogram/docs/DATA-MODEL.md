# DATA-MODEL — propozycja (inspirowana Ideogram)

## Encje

### User
id, handle, email, plan, creditsFast, creditsSlow, creditsResetAt, createdAt

### Model
id, family[BASE|CUSTOM], version(np. 4.0/3.0), displayName, quality, maxResolution, isLegacy, ownerId?(custom)

### CustomModelTrainingJob
id, ownerId, status[QUEUED|RUNNING|DONE|FAILED], trainingAssets[], resultModelId, createdAt

### GenerationRequest
id, userId, promptRaw, promptMagic?, modelId, aspectRatio, width, height,
renderingSpeed[TURBO|AUTO|FAST], numImages, seed, status, createdAt

### Image
id, generationId, storageKey, width, height, seed, model, aspectRatio,
resolution, rendering, isPublic, likeCount, embedding(vector), createdAt

### EditOperation
id, imageId, type[EDIT|UPSCALE|REMOVE_BG|LAYERIZE_TEXT|INPAINT], resultImageId, createdAt

### Like / Follow / Collection
Like: userId, imageId
Follow: followerId, followeeId
Collection: id, userId, name, imageIds[]

### Category (Explore)
id, slug[poster|t-shirt|logo|marketing|print-on-demand], name

## Wyszukiwanie
- Image.embedding → pgvector (similaritySearch, "podobne", rekomendacje feedu).
- Kategorie + tagi do filtrowania Explore.

## Kredyty
- Quota liczona per (modelId, renderingSpeed, requestAction) — jak user_task_quota_stats.
