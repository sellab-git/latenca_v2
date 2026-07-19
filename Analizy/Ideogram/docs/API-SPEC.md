# API-SPEC — obserwowane (Ideogram) + propozycja własna

## Obserwowane u Ideogram (do referencji, NIE do kopiowania)
GET  /api/models/catalog
GET  /api/account/user_task_quota_stats?modelVersion=&samplingSpeed=&requestAction=GENERATE
POST /api/generations/getRequestStats
POST /api/images/similaritySearch
POST /api/images/batch_retrieve_metadata
GET  /api/users/settings
GET  /api/users/follows/:id
GET  /api/licensing/self-serve-commercial/subscription
(+ publiczne API: developer.ideogram.ai)

## Proponowane API dla NAS
### Generacja
GET  /api/models                          → katalog modeli (base + custom)
GET  /api/quota?modelId=&speed=            → dostępne kredyty/limity
POST /api/generations {promptRaw, modelId, aspectRatio, width, height, speed, numImages}
     → {generationId, status:QUEUED, seed?}
GET  /api/generations/:id                 → status + images[]

### Prompt
POST /api/prompt/enhance {prompt}         → {enhancedPrompt}  (własny "magic prompt")

### Obrazy / metadane
GET  /api/images/:id                       → metadane (model, seed, ratio, resolution, rendering)
POST /api/images/similar {imageId|embedding} → podobne
POST /api/images/:id/remix                 → nowa generacja z bazowego promptu/seed

### Edycja
POST /api/images/:id/upscale
POST /api/images/:id/remove-bg
POST /api/images/:id/layerize-text
POST /api/images/:id/edit {mask, prompt}   → inpaint

### Custom modele
POST /api/models/custom/train {assets[]}   → {trainingJobId}
GET  /api/models/custom/:jobId

### Społeczność
POST /api/images/:id/like  | DELETE ...
POST /api/users/:id/follow | DELETE ...
GET  /api/explore?category=&query=&cursor=
POST /api/collections {name} | POST /api/collections/:id/images

## Zasady
- Generacja/training asynchroniczne (status polling lub SSE).
- Kredyty walidowane serwerowo per model+speed.
- Publikacja do Explore po moderacji.
