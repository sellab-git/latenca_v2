# ARCHITECTURE — wywnioskowana + rekomendacja

## Obserwacje
- Frontend: Next.js/React (SPA, font Manrope).
- Własne REST API pod /api/... :
  - /api/models/catalog — katalog modeli.
  - /api/account/user_task_quota_stats?modelVersion=&samplingSpeed=&requestAction=GENERATE — limity/kredyty per model/prędkość.
  - /api/generations/getRequestStats — statystyki żądań.
  - /api/images/similaritySearch — wyszukiwanie podobnych (feed/rekomendacje).
  - /api/images/batch_retrieve_metadata — metadane partii obrazów.
  - /api/users/settings, /api/users/follows/:id — konta i graf społecznościowy.
  - /api/licensing/self-serve-commercial/subscription — licencje komercyjne.
- Publiczne API dla developerów (developer.ideogram.ai).

## Rekomendowana architektura dla NAS
```
[Web (Next.js)] → [API Gateway/BFF]
   ├── Generation Service → kolejka → worker'y GPU (modele) → object storage
   ├── Prompt Service (enhancement / builder)
   ├── Model Registry (bazowe + custom modele, training jobs)
   ├── Image/Metadata Service (seed, params, similaritySearch/embeddingi)
   ├── Social Service (feed, likes, follows, remix, kolekcje)
   ├── Editing Service (upscale, remove bg, layerize, inpaint)
   ├── Billing/Credits Service (plany, kredyty, quota per model/speed)
   └── Public API + Dashboard
[Postgres + pgvector] [Redis] [Queue] [Object storage] [GPU workers]
```

## Zasady
- Generacja i training = zadania asynchroniczne (kolejka, status, webhooki).
- Similarity search na embeddingach (feed, "podobne", moderacja duplikatów).
- Kredyty egzekwowane serwerowo per model+speed (jak quota_stats).
- Pełne metadane + seed zapisywane przy każdej generacji.
