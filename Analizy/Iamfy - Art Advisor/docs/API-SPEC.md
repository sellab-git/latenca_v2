# Specyfikacja API (REST / JSON)

Bazowy prefix: `/api`. Wszystkie odpowiedzi JSON. Autoryzacja sesji przez nagłówek
`X-Session-Fingerprint` (bez logowania w MVP).

---

## POST /api/spaces
Tworzy nową przestrzeń (ścianę) dla sesji.
**Request:** `{ "sessionFingerprint": "string" }`
**Response 201:** `{ "id": "cuid", "createdAt": "iso" }`

## PATCH /api/spaces/:id
Aktualizuje kontekst przestrzeni (odpowiedzi quizu, budżet, zdjęcie pokoju).
**Request:**

```json
{
  "roomType": "bedroom",
  "stylePreference": "cool-serene",
  "wallSize": "medium",
  "pieceCount": "single",
  "budgetMin": 10000,
  "budgetMax": 30000
}
```

**Response 200:** pełny obiekt Space.
**Błędy:** 404 gdy Space nie istnieje / nie należy do fingerprintu.

---

## POST /api/curate
Główny endpoint — generuje kuracje na podstawie briefu (tekst lub quiz).
**Request:**

```json
{
  "spaceId": "cuid",
  "message": "A calming coastal print for a bedroom, soft blues and sandy tones",
  "quiz": { "wallSize": "medium", "pieceCount": "single", "style": "cool-serene" },
  "sessionFingerprint": "string"
}
```

(`message` i `quiz` opcjonalne, ale co najmniej jedno musi być obecne.)
**Response 200:**

```json
{
  "assistantReply": "I can help you find a calming coastal print...",
  "extractedIntent": { "room": "bedroom", "themes": ["coastal"], "palette": ["soft-blue","sand"] },
  "curations": [
    {
      "id": "cuid",
      "name": "Tranquil Tide",
      "description": "A soft, minimalist composition featuring a serene shoreline...",
      "totalPrice": 17685,
      "currency": "PLN",
      "items": [
        { "artworkHandle": "tranquil-shoreline-2", "title": "...", "imageUrl": "...",
          "chosenSize": "50x70", "price": 17685, "position": 1,
          "reason": "Chłodna paleta i horyzont wpisują się w spokojny nastrój sypialni." }
      ]
    }
  ]
}
```

---

## POST /api/for-you
Silnik rekomendacji — zwraca spersonalizowany strumień prac.
**Request:**

```json
{
  "sessionFingerprint": "string",
  "context": { "wishlistHandles": ["tranquil-shoreline-2"], "roomType": "bedroom" },
  "excludeHandles": ["already-shown-1"],
  "hits": 12
}
```

**Response 200:** `{ "items": [ { "handle": "...", "title": "...", "imageUrl": "...", "price": 12900, "score": 0.87 } ] }`

---

## POST /api/spaces/:id/curations
Zapisuje/persystuje kuracje (wywoływane wewnętrznie lub przy edycji).
**Response 200:** `{ "curations": [ ... ] }`

## POST /api/visualize
Generuje wizualizację kuracji na ścianie.
**Request:** `{ "curationId": "cuid", "roomPhotoUrl": "string|null", "wallSize": "medium" }`
**Response 200:** `{ "imageUrl": "https://.../render.png", "mode": "mockup" | "room-photo" }`

## POST /api/interactions
Rejestruje zdarzenie (lajk/odrzucenie/shortlist) do nauki.
**Request:** `{ "spaceId": "cuid", "artworkHandle": "...", "type": "like" }`
**Response 204.**

---

## Kody błędów (wspólne)
- 400 — walidacja payloadu.
- 404 — zasób nie istnieje / nie należy do fingerprintu.
- 429 — rate limit (endpointy AI).
- 500 — błąd wewnętrzny (loguj z trace id).
