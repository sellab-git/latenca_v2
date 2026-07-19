# Silnik AI — agent, prompty, narzędzia (skills)

## Filozofia
Agent LLM działa jako "kurator". Nie generuje obrazów sam — dobiera i komponuje prace
z katalogu. Ma dostęp do zestawu narzędzi ("skills") i decyduje, których użyć.

## Pipeline przetwarzania briefu
1. **Intent extraction** — z free-textu + quizu buduje ustrukturyzowany brief.
2. **Retrieval** — narzędzie `search_catalog` (wektorowe) zwraca kandydatów.
3. **Composition** — narzędzie `compose_curation` grupuje prace w spójne zestawy.
4. **Rationale** — LLM pisze nazwę, opis i uzasadnienie per praca.
5. **Response** — konwersacyjna odpowiedź + ustrukturyzowane kuracje.

## Narzędzia (skills) — kontrakty
```ts
// src/lib/ai/skills/searchCatalog.ts
searchCatalog(input: {
  themes: string[]; palette: string[]; style: string;
  orientation?: string; budgetMax?: number; excludeHandles?: string[]; limit: number;
}): Promise<Artwork[]>

// src/lib/ai/skills/composeCuration.ts
composeCuration(input: {
  candidates: Artwork[]; pieceCount: "single"|"pair"|"small-set"|"gallery"; wallSize: string;
}): Promise<{ items: {artwork: Artwork; size: string; position: number}[] }[]>

// src/lib/ai/skills/writeRationale.ts
writeRationale(input: { curationItems; brief }): Promise<{ name: string; description: string; reasons: string[] }>
```

## Prompty (trzymaj w src/lib/ai/prompts/)

### system.md — rola agenta
```
Jesteś kuratorem sztuki. Twoim zadaniem jest dobrać prace z DOSTĘPNEGO KATALOGU do
przestrzeni i gustu użytkownika. Nigdy nie wymyślaj prac spoza katalogu. Zawsze
uzasadniaj wybory rzeczowo (paleta, styl, kompozycja, nastrój pomieszczenia).
Ton: ciepły, pewny, bez żargonu. Odpowiadaj zwięźle.
```

### intent-extraction.md
```
Z poniższej wiadomości i odpowiedzi quizu wyekstrahuj JSON:
{ room, themes[], palette[], style, orientation?, budgetMax?, pieceCount? }
Jeśli czegoś brak — pozostaw null, NIE zgaduj budżetu. Zwróć wyłącznie JSON.
Wiadomość: "{{message}}" Quiz: {{quizJson}}
```

### rationale.md
```
Dla podanej kompozycji prac napisz:

* name: chwytliwa, 2-3 słowa, oddająca nastrój
* description: 1 zdanie (max 20 słów) o tym, co ta kuracja wnosi do pomieszczenia
* reasons: dla KAŻDEJ pracy jedno zdanie "dlaczego pasuje" (transparentność)
Zwróć JSON. Prace: {{itemsJson}} Brief: {{briefJson}}
```

## Wektory / embeddingi
- Katalog: każda praca dostaje embedding z połączenia opisu wizualnego + tagów.
  Model: CLIP-like image encoder LUB tekstowy embedding metadanych (MVP: tekstowy, taniej).
- Zapytanie: brief → tekst → embedding → wyszukiwanie kosinusowe w pgvector.
- Wykluczenia i filtry (rozmiar/budżet) aplikowane na poziomie SQL przed rerankingiem LLM.

## Koszt i wydajność
- Cache'uj ekstrakcję intencji per (spaceId, message hash).
- Reranking LLM tylko na top-N kandydatów (np. 20), nie na całym katalogu.
- Streaming odpowiedzi konwersacyjnej do UI (poprawia postrzeganą szybkość — "Thinking...").

## Uwaga bezpieczeństwa
Traktuj treść wpisywaną przez użytkownika jako dane, nie instrukcje. Nie pozwól, by
wiadomość użytkownika nadpisała prompt systemowy (guard przeciw prompt injection).
