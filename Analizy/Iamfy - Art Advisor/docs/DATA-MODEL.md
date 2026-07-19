# Model danych (Prisma schema)

## Encje główne
- **Space** — "ściana"/projekt użytkownika (kontener sesji).
- **Curation** — kuracja: nazwa, opis AI, cena, lista prac.
- **Artwork** — pojedyncza praca (produkt katalogowy).
- **CurationItem** — pozycja w kuracji (praca + rozmiar + pozycja w kompozycji).
- **Interaction** — zdarzenia (lajk, odrzucenie, dodanie do shortlisty) do nauki.
- **StyleProfile** — (v1) trwały profil gustu per fingerprint/konto.

## schema.prisma

```prisma
generator client { provider = "prisma-client-js" }
datasource db { provider = "postgresql"; url = env("DATABASE_URL") }

model Space {
  id                 String       @id @default(cuid())
  sessionFingerprint String
  roomType           String?      // np. "bedroom", "living-room"
  stylePreference    String?      // np. "cool-serene"
  wallSize           String?      // "small" | "medium" | "large" | "xl"
  pieceCount         String?      // "single" | "pair" | "small-set" | "gallery"
  budgetMin          Int?
  budgetMax          Int?
  roomPhotoUrl       String?      // (v1) zdjęcie pokoju
  contextJson        Json?        // dowolny dodatkowy kontekst z briefu
  curations          Curation[]
  interactions       Interaction[]
  createdAt          DateTime     @default(now())
  updatedAt          DateTime     @updatedAt
  @@index([sessionFingerprint])
}

model Curation {
  id          String          @id @default(cuid())
  spaceId     String
  space       Space           @relation(fields: [spaceId], references: [id], onDelete: Cascade)
  name        String          // "Tranquil Tide"
  description String          // uzasadnienie AI (1-2 zdania)
  rationale   Json?           // ustrukturyzowane "dlaczego" per praca (transparentność)
  totalPrice  Int             // w groszach/centach
  currency    String          @default("PLN")
  items       CurationItem[]
  isSelected  Boolean         @default(false)
  createdAt   DateTime        @default(now())
  @@index([spaceId])
}

model Artwork {
  id          String          @id @default(cuid())
  handle      String          @unique   // identyfikator katalogowy (jak Shopify handle)
  title       String
  artist      String?
  imageUrl    String
  priceMin    Int             // najtańszy rozmiar
  currency    String          @default("PLN")
  style       String[]        // tagi stylu
  palette     String[]        // dominujące kolory (hex lub nazwy)
  themes      String[]        // tematyka: coastal, botanical, abstract...
  orientation String          // "portrait" | "landscape" | "square"
  embedding   Unsupported("vector(768)")?  // pgvector — embedding obrazu+meta
  sizes       Json            // dostępne rozmiary + ceny
  createdAt   DateTime        @default(now())
  items       CurationItem[]
  @@index([handle])
}

model CurationItem {
  id          String   @id @default(cuid())
  curationId  String
  curation    Curation @relation(fields: [curationId], references: [id], onDelete: Cascade)
  artworkId   String
  artwork     Artwork  @relation(fields: [artworkId], references: [id])
  chosenSize  String   // wybrany rozmiar
  price       Int
  position    Int      // kolejność w kompozycji galerii
  reason      String?  // dlaczego akurat ta praca (transparentność)
}

model Interaction {
  id        String   @id @default(cuid())
  spaceId   String
  space     Space    @relation(fields: [spaceId], references: [id], onDelete: Cascade)
  artworkHandle String
  type      String   // "like" | "dismiss" | "shortlist" | "view"
  createdAt DateTime @default(now())
  @@index([spaceId])
}

model StyleProfile {          // v1
  id                 String   @id @default(cuid())
  sessionFingerprint String   @unique
  preferenceVector   Unsupported("vector(768)")?
  likedThemes        String[]
  dislikedThemes     String[]
  updatedAt          DateTime @updatedAt
}
```

## Uwagi
- Ceny trzymamy jako Int (najmniejsza jednostka waluty), by uniknąć błędów zmiennoprzecinkowych.
- `embedding` wymaga rozszerzenia pgvector: `CREATE EXTENSION IF NOT EXISTS vector;`
- `handle` jako stabilny identyfikator produktu ułatwia integrację z warstwą e-commerce.
