# Latenca — Specyfikacja (dokument roboczy)

> ⚠️ **Wersja robocza — będzie się zmieniać.** Ten dokument to jedno miejsce prawdy o decyzjach produktowych, architekturze i modelu cenowym. Nie jest zamknięty. Aktualizujemy go w miarę pracy.
>
> Ostatnia aktualizacja: **2026-07-10** · Faza: pre-launch, prototyp → budowa w Next.js
> Kod/pola: nazwy po angielsku (staną się kodem). Reszta po polsku (dla Artura).

---

## 0. Legenda statusów

- ✅ **DECYZJA** — ustalone, budujemy tak
- 🔬 **ZWERYFIKOWANE** — potwierdzone researchem 2026 (źródła w sekcji 9)
- 🟡 **DO DECYZJI** — otwarte, wymaga wyboru (sekcja 8)
- ⛔ **NIE TERAZ** — świadomie odłożone (sekcja 7)

---

## 1. Czym jest Latenca

✅ **Bohater produktu = BUILDER ŚCIANY.** Tożsamość to nie „sklep ze sztuką" ani „druk zdjęć", tylko **komponowanie własnej ściany (zestawu) z kafelków** — a źródło grafiki jest wymiennym paliwem. Jedno zdanie: *„Latenca zamienia dowolny obraz w ścianę, z której jesteś dumny."* Kategoria = ściana, nie źródło.
- **Dlaczego to rdzeń (🔬 3 niezależne raporty 2026):** (a) tożsamość żyje w mechanice+celu, nie w źródle (wzorzec Canva/Mixtiles/Displate) → rozbraja ryzyko „za dużo opcji = brak tożsamości"; (b) ściana = kilka sztuk = wysoki koszyk (jedyny sposób, by płatny CAC się spinał); (c) **realna wolna przestrzeń** — POD-y sprzedają pojedynczo, Mixtiles oddziela gotowe zestawy od custom kafelków, Displate bez AI, generatory bez kuracji; builder ściany z dowolnych asetów jako GŁÓWNA cecha jest niezajęty.
- **Zasada:** builder projektowany **agnostycznie wobec źródła** od dnia 1 (jeden szew `ArtworkSource` = obraz gotowy do druku + metadane + status praw). Każde źródło = adapter. Kafelki NIGDY nie są menu 3 obietnic na stronie głównej — źródło to pod-wybór *w kafelku* („wypełnij ten slot" → z kolekcji / wgraj / wygeneruj).

✅ **Kurowana marka premium** (jak każde paliwo wpływa) — nie otwarty firehose. Kuracja albo zostajemy Redbubble; AI to ŹRÓDŁO, nigdy tożsamość.

### 1a. Sekwencja źródeł (szwy vs silniki — wizja w szwach, silniki na dowodach)
Rollout fazowy (Artur, 2026-07-07 — awans na DOWODACH, nie na czasie; każda faza odblokowuje następną):
- **FAZA 0 — „Pode mnie" (operator) = pierwszy build (~4-6 tyg.):** builder ściany (bohater) + **operator (Artur) dodaje własne grafiki** i sam testuje pełny flow → przepuszcza prawdziwe zamówienie (ściana → kasa → Gelato → dostawa) + Stripe. Podgląd „w pokoju" **2D** (~1-2 tyg., różnicownik). **Nie renderujemy ściany do druku** — każdy kafelek = osobny druk Gelato; ściana = podgląd. *Dowód: maszyna działa end-to-end.* Architektura: model danych + szew `ArtworkSource` + „artysta" jako byt + logika bramki stawiane JUŻ TU (tanie) → Artur = pierwszy „artysta" w systemie; kolejne fazy to wpuszczanie następnych, nie przepisywanie.
- **FAZA 1 — Zaproszeni artyści:** garstka ręcznie wybranych, upload ręczny/prosty. *Dowód: cudza kurowana sztuka się sprzedaje + podaż działa.*
- **FAZA 2 — Otwarcie z limitami (gated self-serve):** otwarta rejestracja + drabina zaufania (10→20→50) + bramka AI + ręczna pierwsza partia + Studio + wypłaty (sekcje 2-4). *Dowód: gated self-serve skaluje bez utraty jakości.*
- **FAZA 3+ — Nowe źródła/narzędzia w służbie „zbuduj swoją ścianę":** własne zdjęcia klienta (upload → kadr → kafelek; *to zmienia model biznesowy*; najsilniejszy hak = pamięć, najniższe ryzyko prawne), potem generowanie AI (najgorszy profil prawny/marżowy — lub nigdy), kolejne narzędzia.
- ⛔ Poza sekwencją, za szwem: prawdziwe AR, multi-provider druku, agent-commerce plumbing.
- ⛔ **Prawdziwe AR** (telefon → Twoja ściana) = pułapka (iOS Safari słabo, 4-8 tyg. + wieczne łatanie). Za szwem, tylko jeśli dane pokażą porzucanie na „czy zmieści się na ścianie".
- **Mocne presety układów** (siatka/salon/rząd) — ściana wygląda dobrze zanim klient cokolwiek ruszy (zabija paraliż wyboru = realny zabójca konwersji).
- **Pobranie pliku = akcja na kafelku** („weź też jako plik"), nie osobny produkt.

### 1b. Builder ściany — model działania (MOBILE-FIRST; 🔬 4 raporty 2026: teardown + best-practice tech + 2× adwersaryjny mobile)
Rynek: sklepy prowadzą PRESETAMI; freeform+wymiary tylko w planerach co NIE sprzedają. Mixtiles (lider kategorii) NIE robi freeform-drag → tap-kafelek → „Swap Position". Adwersaryjna weryfikacja mobile-first ZMIENIŁA plan — pierwotny był „desktopowym edytorem canvas w mobilnym przebraniu". Poprawiony poniżej.

**PARADYGMAT = PROWADZONY PRZEPŁYW (step-flow), NIE płótno do przeciągania** (🔬 Baymard: multi-step z paskiem postępu bije gęstą jedną powierzchnię przy złożonej konfiguracji, do +35% konwersji). Model 5 kroków (slot-filling):
1. **Wybierz układ** — 1 z 4 presetów (siatka/salon/rząd/półka), wstępnie wypełniony. (Pusta ściana = tryb zaawansowany; blank-canvas-paralysis udokumentowany.) KEEP.
2. **Rozmiar** — jeden ekran PO wyborze układu: preset ściany („nad kanapą ~150cm") lub JEDNO pole; podgląd proporcjonalny + **plakietka skali** („pokazane w 8% rzeczywistej"). ⚠️ ZMIANA: nie dwa pola liczbowe na wejściu, nie dosłowna skala 1:1 (na 390px = znaczek pocztowy, góra ściany poza zasięgiem kciuka).
3. **Wypełniaj sloty pojedynczo** — dotknij slotu → **dolny arkusz** (katalog kurowany → dotknij grafiki → wraca); ramka+passe-partout jako rząd chipów; rozmiar = **chipy realnych rozmiarów druku** (NIE suwak — i tak stałe SKU); kolejność = **Swap Position**; równe odstępy **liczone automatycznie z presetu** (bez roboty usera).
4. **Zobacz u siebie** — moment pewności skali + emocjonalne domknięcie. v1 = **wgraj zdjęcie swojej ściany (2D composite, tanie)**; AR „na Twojej ścianie" = szybki następny silnik (WebAR), NIE v1 (drogie/kruche na iOS — godzimy sprzeczność raportów: potrzeba skali realna, implementacja v1 tania).
5. **Cała ściana → koszyk** — 1 klik, ROZBIJALNE na sztuki (druk per-kafelek + „weź też plik"); PDF z instrukcją zawieszania po zakupie. KEEP.

⛔ **FREEFORM-DRAG kafelków = NIE domyślnie** (🔬 NN/g: touch-drag multi-obiekt = pułapka; Gmail go usunął; Mixtiles nigdy nie miał). Tylko za jawnym trybem „Custom" z pinch-zoom — furtka dla zaawansowanych, nigdy ścieżka wejścia.
**Reguły mobile:** akcje w dolnej 1/3 ekranu; cele ≥44px; jedna decyzja na ekran; góra ściany = strefa nieosiągalna kciukiem.

TECH (best 2026 / ready 2035; adwersaryjnie POTWIERDZONE): **DOM+CSS w React, NIE canvas** (≤30 kafelków = 16× zapasu do progu ~500 węzłów, gdzie canvas ma sens) — 2 TWARDE WARUNKI: (a) ruch/drag przez `transform:translate()`, NIGDY `top/left`; (b) `touch-action:none` na kafelku + Pointer Events + `setPointerCapture` + `will-change:transform` tylko na aktywnie-przeciąganym. **PWA** (nie natywna apka — złe koszty solo 2-3×; nie zwykłe responsive — upgrade prawie darmowy: instalacja na ekranie, offline, aparat do „zdjęcia ściany"); natywna dopiero gdyby AR/push-iOS/App-Store tego wymusiły. **OBRAZKI (prawdziwe ryzyko OOM na tanim telefonie, nie rysowanie):** miniatury pod rozmiar kafelka via `srcset`/`sizes`, WebP (AVIF tylko z `<picture>` fallbackiem — drogi dekod na tanim Android), `loading=lazy`; pełna rozdzielczość TYLKO serwerowo do druku. Druk = render SERWEROWY ze schematu, jeden job/kafelek (nie zrzut ekranu). Dodać: `dvh`/`svh`, `env(safe-area-inset-*)`, container queries; haptyka TYLKO Android (iOS brak `vibrate`); View Transitions + Web Share jako polish.
DANE (renderer wymienny, SCHEMAT to aktyw): `{schemaVersion, unit:"mm", wall:{widthMm,heightMm}, layoutPreset, tiles:[{xMm,yMm,widthMm,heightMm,frame,artworkRef,rotationDeg,z}]}` — mm nie piksele, artworkRef ID nie osadzony obraz, NIGDY wewnętrzny JSON biblioteki; px=mm×scale (pochodne), druk pochodny per-tile.
ZAPIS/SHARE (backend, NIE prototyp; UI flow już zaprojektowany w Builder2): **Save** = utrwalenie schematu w DB (per-user gdy zalogowany; anon guest = localStorage/cookie z migracją do konta przy logowaniu). **Share** = krótki publiczny URL `latenca.com/w/{id}` → read-only render schematu z opcją „edytuj kopię" i „dodaj do koszyka" (haczyk wzrostowy: udostępniona ściana sprzedaje). Realne linki + trwałość = zadanie build-time; w prototypie tylko toast-stub, nic nie zapisuje.
**Dostępność od dnia 1** = równoległa lista kafelków w DOM z ARIA+klawiaturą, ten sam stan („dwa widoki, jeden model").
3 pułapki: freeform-drag/canvas jako domyślny zamiast step-flow · zapis pikseli-lub-JSON-biblioteki · dostępność później.

**Dlaczego tak (🔬):** dwaj zwycięzcy w kategorii to kurowane marki — Mixtiles (~$250M, nigdy nie otworzył podaży) i Displate (~$264M, marka najpierw, artyści później). Otwarte marketplace'y (Society6, Redbubble) umierają. W świecie zalanym grafiką AI **kuracja to jedyna fosa, która przeżywa** — i jest sprzeczna z otwartym uploadem (wpuszczając każdego, sam stajesz się zalewem, który miałeś filtrować).

### 1c. Warstwy customizacji — „na szynach", nie pusty prompt (✅ teza zablokowana 2026-07-10)

**Drugi filar produktu obok kuracji.** Wyróżnik vs generyczne generatory (Midjourney/Ideogram) = **wchodzisz od arcydzieła, nie od pustej kartki.** Generyczne narzędzia mają „pusty prompt" (efekt losowy, nie pod druk). My dajemy kurowaną grafikę gotową pod duży druk + **ograniczone warstwy zmian, które ZAWSZE dają dobry efekt** (szit nie ma jak powstać, bo nie ma takiej opcji w UI). Kuracja zostaje nienaruszona, bo klient porusza się tylko po zaprojektowanych szynach.

**Kluczowy wniosek (rozbraja pierwotny strach o koszty AI):** większość warstw **NIE potrzebuje AI** — to klasyczna obróbka obrazu / typografia. Zero kosztu za użycie, natychmiast, nie da się zepsuć, zero ryzyka prawnego (przekształcamy już-sprawdzone dzieło artysty, nie tworzymy nowej treści). AI zostaje TYLKO dla najcięższej warstwy (podmiana tematu / „Twój pupil w stylu"), gdzie klient ma wysoką intencję → koszt generacji się zwraca.

| Warstwa | Technologia | Koszt/użycie | Ryzyko | Faza |
|---|---|---|---|---|
| Tonacja/kolory, kadr, format, rozmiar, oprawa, zestaw na ścianę | Obróbka obrazu (nie AI) | **0** | żadne | wcześnie (tanie) |
| Napis / treść na grafice | Typografia (nie AI) | **0** | tekst usera → filtr | wcześnie |
| Twój pupil / temat w kurowanym stylu | AI, ograniczone (bounded) | koszt generacji | jakość + moderacja | silnik #2 (⛔ nie v1) |

**Dwie rzeczy do zaprojektowania z głową:**
1. **Napis = mina smaku.** Motywacyjny cytat na pięknym zachodzie = dokładnie ten „szit", którego unikamy. Szyny też mają mieć gust: **kurowane fonty, kurowane miejsca, tylko wybrane grafiki pozwalają na tekst.**
2. **Artysta decyduje, które warstwy są dozwolone na jego pracy** (kolory/kadr — domyślnie; tekst/podmiana tematu — artysta włącza sam). Chroni prawa artysty **i** jest argumentem rekrutacyjnym („zostajesz szefem swojego dzieła") → przyciąga tych dobrych, na których nam zależy. Model danych: flaga per-ARTWORK `allowed_customizations[]`.

**Reconcyliacja z sekcją 7 (⛔ generator AI odłożony):** warstwy nie-AI (kolor/kadr/tekst) to NIE jest „generator AI" — to obróbka obrazu, może wejść wcześnie i tania. Odłożona zostaje tylko ciężka warstwa generatywna (podmiana tematu / pupil) = silnik #2 z sekcji 1a fazy 3+.

**Dlaczego tak (🔬):** dwaj zwycięzcy w kategorii to kurowane marki — Mixtiles (~$250M, nigdy nie otworzył podaży) i Displate (~$264M, marka najpierw, artyści później). Otwarte marketplace'y (Society6, Redbubble) umierają. W świecie zalanym grafiką AI **kuracja to jedyna fosa, która przeżywa** — i jest sprzeczna z otwartym uploadem (wpuszczając każdego, sam stajesz się zalewem, który miałeś filtrować).

**Sprzedajemy dwie rzeczy z każdej grafiki:**
1. **Plik cyfrowy do pobrania** (marża ~100%, odzyskuje koszt reklamy)
2. **Druk na życzenie** (POD przez Gelato — plakat/płótno/ramka)

Oraz **zestawy/ściany** (kilka grafik razem) — silnik wysokiego koszyka (🔬: pojedynczy druk na płatnym ruchu nie spina się finansowo; zarabiają pliki + zestawy).

### 1d. Katalog wariantów generowany przez system + discovery (✅ 2026-07-10)

Skończona przestrzeń szyn (1c) → system wylicza z KAŻDEGO kurowanego oryginału zestaw wariantów **z góry, jako PRZEPISY nie pliki**, indeksuje je do wyszukiwania i renderuje na żądanie. Jedno dzieło = wiele znajdowalnych wariantów, **bez user-uploadów, bez bieżni moderacji** (ufamy przekształceniu + oryginał sprawdzony raz). To rozwiązuje discovery i rozbudowę katalogu z jednego uploadu — i jest LEPSZE niż warianty robione przez klientów (te łamały kurację; patrz odrzucony model niżej).

**DWIE OSIE MNOŻĄ SIĘ OSOBNO — nie mylić (to sedno):**

| | Oś WYGLĄDU (DERIVATIVE) | Oś PRZEDMIOTU (SKU) |
|---|---|---|
| Co zmienia | **obraz** (tonacja/kadr/układ-tekstu) | **przedmiot** (materiał/rozmiar/rama/mata) |
| Widoczny/indeksowany? | **TAK** — człowiek to widzi w wyszukiwaniu | **NIE** — liczony wzorem przy wyborze |
| Ile na dzieło | **~24** (6 tonacji × 4 kadry) | **~5 400** (×5 mat ×3 rozm ×5 ram ×3 mata) |
| Render | na żądanie + cache (tylko oglądane) | brak — kompozyt na żywo w podglądzie |
| Reguła projektowa | **SKĄPO i kurowane** (nadmiar = cienkość, efekt Redbubble) | **HOJNIE** (darmowe, wirtualne, oczekiwane w druku) |

⚠️ **„1000 wariantów DO POKAZANIA" = błąd** (zabija premium). **„1000+ SKU do kupienia" = OK** (wirtualne, liczone wzorem, nietrzymane).

**Co trzymamy z jednego dzieła:** na zawsze — master (hi-res) + przepisy (wiersze DB). Render+cache — do 24 wersji tonacja×kadr, TYLKO oglądane. Nigdy — SKU (wzór) + kompozyty ramy/maty (składane na żywo w podglądzie; ten sam obraz, inna oprawa). Tekst = enumerujemy UKŁAD (font×miejsce), **słowa dokleja klient prywatnie** → zero tekstu użytkownika publicznie → zero moderacji/ryzyka prawnego na tej warstwie.

**Discovery (żeby warianty NIE zalały katalogu):**
- **Przeglądanie** (grid, home) = kurowane **ORYGINAŁY**, jeden bohater na dzieło. Premium zostaje.
- **Wyszukiwanie/filtry** = świadome wariantów (znajdą „ciepła kwadratowa z miejscem na napis"), ale **zwijają wyniki po roocie** (bez 24 recolotów w rzędzie).
- Wynik-wariant → otwiera **zjednoczoną stronę dzieła** (patrz 1e) z parametrami już nałożonymi. **Strona dzieła JEST rendererem wariantu.**
- SEO z cienkich stron = **BONUS, nie fundament** (Google karze doorway pages; AI Overviews tną organik). Trwała wartość = discovery wewnętrzne + wektorowe (pgvector).

**Ważność PER dzieło (kuracja pod automatem):** nie każdy wariant pasuje (16:9 utnie kompozycję, Noir zabija niektóre). ARTWORK niesie `allowed_tones[]`, `allowed_crops[]`, `allow_text` — artysta lub system-z-kontrolą wyłącza warianty psujące dzieło. **Auto-generujemy tylko to, co wygląda dobrze.**

**Rozliczenie i lineage:** każdy DERIVATIVE → **root ARTIST zawsze płaci** (wariant to pochodna, nie nowe dzieło). Provenance: każdy wariant linkuje do roota („oparte na oryginale Arii Veli"). Model danych: sekcja 3.

**Pierwszy zestaw parametrów (v1 — punkt startu do dopracowania):**
- **Tonacje (6):** Oryginał · Ciepła · Chłodna · Mono · Sepia · Noir
- **Kadry (4):** 3:4 · 1:1 · 4:5 · 16:9
- **Układ tekstu (9):** font {Elegant/serif · Odręczny · Modern} × miejsce {dół · środek · góra}; słowa prywatne
- **Przedmiot:** materiał {Poster · Płótno · Metal · Akryl · Drewno} · rozmiar {30×40 · 50×70 · 70×100} · rama {Brak · Biała · Czarna · Naturalna · Ciemna} · passe-partout {Brak · 3 · 6 cm}
- 🟡 **Do dopracowania:** ostateczna lista tonacji/kadrów, progi jakości per-piece, czy kadry mają auto-focal-crop (by nie ucinać kompozycji), czy tonacje robić per-styl (inne dla foto vs abstrakcja).

**⛔ ODRZUCONE — publiczne warianty robione przez klientów (TikTok-sound model):** kuszące (katalog rośnie sam, root zawsze płaci), ale łamie fosę kuracji (każdy klient publikuje = firehose jak Redbubble), rodzi bieżnię moderacji, i przy produkcji fizycznej wchodzi w odpowiedzialność producenta (ta odłożona w sekcji 7). Zamiast tego: **system generuje warianty z kurowanych oryginałów** (powyżej). Kupujący personalizuje **prywatnie**; publiczne warianty tworzy tylko **kurowany twórca** (awans po drabinie zaufania z sekcji 2). Dwie role: kupujący (prywatnie, nieograniczony) vs twórca (publicznie, przez bramkę, zarabia).

**Reconcyliacja:** DERIVATIVE (oś wyglądu) ≠ PRODUCT/VARIANT (oś przedmiotu/SKU, sekcja 3). Warianty wyglądu = przekształcenia obrazu (nie „generator AI" z sekcji 7); ciężka warstwa AI (pupil) zostaje odłożona jako silnik #2.

### 1e. Zjednoczona strona dzieła — dwie osie, jeden podgląd, jedna linia koszyka (✅ 2026-07-10)

Product (jak zrobione) i Personalizacja (jak wygląda) to **nie dwie strony — dwie osie jednej decyzji.** Jedna strona dzieła:
- **Domyślnie: kup jak jest** — dzieło już piękne i pod druk; widać wybór przedmiotu (format/materiał/rozmiar/rama/mata). 80% tak kupi.
- **„Uczyń ją swoją"** = opcjonalna warstwa (tonacja/kadr/napis/pupil), zwinięta domyślnie. Opcja, nie bramka — nie przytłacza.
- **Podgląd = miejsce spotkania obu osi:** ten sam kadr pokazuje NARAZ Twój obraz (tonacja/napis) × ramę (kolor) × passe-partout (szerokość). Finalny efekt, nie pół prawdy.
- **Jeden koszyk, jedna linia** niosąca obie osie. Cena liczona na żywo (rozmiar×materiał + rama; cyfrowy = flat).
- Format cyfrowy vs druk = oś przedmiotu; personalizacja działa niezależnie (możesz spersonalizować i plik, i wydruk) — dowód, że osie są prostopadłe.
- Prototyp: `scratchpad/latenca-artwork-unified-v1.html` (zrzuty w `research/builder-refs/unified-*.jpeg`). Wcześniejsze studia personalizacji: v1 (jasny), v2 (ciemny „AI-tool"), v3 (natywny Latenca) — też w scratchpad.

---

## 2. Onboarding artystów — drabina zaufania

✅ **Rejestracja otwarta**, ale konto rodzi się z limitem i poziomem zaufania. Kran przykręcony na start, system gotowy na wielu.

### Drabina limitów (progresywne zaufanie)
| Poziom | Limit uploadu | Awans |
|---|---|---|
| Nowy | **10 grafik** | pierwsza partia zawsze przez Admina |
| Zaufany 1 | **+20** | gdy poprzednie były dobre |
| Zaufany 2 | **+50** | gdy poprzednie były dobre |
| … | rośnie | itd. |

### Bramka jakości (dwie warstwy)
1. **Automat AI** sprawdza każdą grafikę: jakość/rozdzielczość, znaki towarowe i logo, wizerunki osób, treści niedozwolone/NSFW, zgodność z prawem, dopasowanie do „house look".
2. **Człowiek (Admin)** — **pierwsza partia 10 grafik zawsze ręcznie**, nawet jeśli AI dało zielone światło (siatka bezpieczeństwa na błędy AI). Kolejne partie: automat prowadzi + wyrywkowe kontrole.

### Wyniki
- ✅ **OK** → grafiki idą na sprzedaż na profilu artysty
- ✏️ **Poprawki** → wracają **z konkretnym powodem** (co i dlaczego)
- ❌ **Śmieć** → „dziękujemy, nie przyjmujemy" → konto zablokowane do dalszego uploadu

**Uwaga (żeby nie przeinżynierować):** automat AI **startuje prosto** (wywołanie modelu moderacji + reguły). Mały wolumen + ręczna pierwsza partia trzymają ryzyko nisko. Mądrzeje z czasem.

---

## 3. Model danych

> Zasada nadrzędna: **grafika ≠ produkt do kupienia ≠ zamówienie.** To jedyna dyscyplina, którą trzeba zrobić dobrze od dnia 1 (retrofit = przepisanie całości).

### Byty (encje)
- **ARTIST** — konto, `status`, `trust_tier`, `upload_limit`, `revenue_share%`, dane do wypłaty. Pełnoprawny byt od początku (system gotowy na tysiące).
- **ARTWORK** — sama grafika: `source_image` (master hi-res), opis, tagi, `artist_id`, `moderation_status`, `allowed_tones[]`, `allowed_crops[]`, `allow_text`. **Bez ceny** — to tylko treść.
- **DERIVATIVE (wariant WYGLĄDU)** — pochodna ARTWORK po osi wyglądu: `parent_artwork_id`, `root_artist_id` (**zawsze płaci**), parametry `{tone, crop, text_layout}`, `visibility`, `is_system_generated`, embedding do wyszukiwania. **Przepis, nie plik** — render na żądanie + cache. Generowany z góry przez system z kurowanych oryginałów (sekcja 1d). ⚠️ **To NIE to samo co PRODUCT/VARIANT** — DERIVATIVE zmienia OBRAZ (~24/dzieło, widoczny), VARIANT opakowuje go w fizyczny przedmiot (~5400/dzieło, wirtualny).
- **PRODUCT / VARIANT (SKU, oś PRZEDMIOTU)** — grafika (lub jej derivative) staje się kupowalna: `(artwork|derivative) × {size, material, mat, frame, FILE|PRINT}` + **cena liczona wzorem**. Wirtualne — nie trzymamy w tabeli, liczymy przy wyborze. Jedna grafika → tysiące konfiguracji.
- **SET / WALL** — pakietuje N grafik, sprzedaje się jako jeden produkt.
- **ORDER + ORDER_LINE** — przy zakupie **zamrażamy kopię** (tytuł, konfiguracja, cena). Późniejsze zmiany nie psują historii.
- **MODERATION_REVIEW** — wynik AI + decyzja Admina + powód (podpięte pod ARTWORK).
- **PAYOUT** — okres + suma + status (podpięte pod ARTIST); gotowe pod Stripe Connect.

### Bramka (gdzie siedzi kuracja)
Na **ARTIST** (`status`, `trust_tier`, `upload_limit`) i na **ARTWORK** (`moderation_status`). Panel Admina = akceptuj/popraw/odrzuć + limity.

*(Diagram struktury: patrz widget „latenca_data_model" w historii czatu.)*

---

## 4. Model cenowy

🔬 Zweryfikowany researchem (Redbubble/Society6/Zazzle/Fine Art America + matematyka gross-up + Gelato/Printful + VAT UE).

### Formuła (jedna dla druku i pliku)
```
Cena netto = (koszt_Gelato + nasze_koszty_stałe)
             ÷ (1 − nasza_marża% − %_artysty − prowizja_płatności%)
```
- **Licznik** = tylko koszty kwotowe: koszt Gelato (druk) lub ~0 (plik) + stała alokacja (hosting/AI/rezerwa na zwroty).
- **Mianownik** = wszystkie procenty (nasza marża + artysta + ~3% prowizji). ⚠️ Prowizja MUSI być w mianowniku (to % od ceny końcowej, nie od kosztu).

### Przykład (druk)
Koszt Gelato 40 + koszty stałe 5 = 45 zł · marża 25% · artysta 30% · prowizja 3%
→ 45 ÷ (1 − 0,25 − 0,30 − 0,03) = 45 ÷ 0,42 = **107,14 zł netto** → zaokrąglić w górę (np. 109) → sprawdzić, czy nad podłogą marży.
Artysta zmienia % w panelu (np. na 40%) → cena rośnie (45 ÷ 0,32 = 140,63), **nasza marża i koszty nietknięte**.

### Trzy zabezpieczenia (must-have)
1. **Limit % artysty** (np. max 40%) — wzór dąży do nieskończoności przy 100%.
2. **Podłoga marży** — minimalny nasz zysk netto, poniżej którego cena nie schodzi.
3. **% artysty liczony od NETTO** (przed VAT) — bo VAT różni się per kraj/typ; od brutto płaciłby artyście inaczej w różnych krajach.

### Zmienny koszt Gelato (🔬 norma branżowa)
Nie liczymy ceny „na żywo" (skakałaby → utrata zaufania). **Zapisujemy cenę + job odświeżający** (tydzień/miesiąc) pobiera aktualny koszt z Gelato Price API i **przecenia tylko produkty poniżej podłogi marży**; bufor absorbuje małe wahania.

### VAT i waluty (🔬)
- Trzymamy **jedną cenę netto**, VAT doklejamy na kasie wg kraju kupującego i typu produktu.
- **Plik cyfrowy** = stawka kraju kupującego (OSS; poniżej progu €10k — stawka krajowa). **Druk** = Union OSS, lub IOSS + próg €150 jeśli Gelato wysyła spoza UE. ⚠️ Od 1.07.2026 UE dokłada ~€3/paczkę na tanie importy — **potwierdzić z księgowym**.
- Waluty: **sztywne cenniki per waluta z końcówkami .99**, nie przeliczanie live.

### Plik cyfrowy
Wyceniany **wartością, nie kosztem** (koszt ≈ 0): ~**15–30% ceny druku** („drukujesz sam"). Ten sam podział % działa identycznie. Licencje (osobista vs komercyjna ~5–10×) = dźwignia cenowa na przyszłość.

### Wypłaty
✅ Na start **ręcznie, zbiorczo** (np. 10. każdego miesiąca, suma za poprzedni okres). Pola gotowe pod Stripe Connect, automat później.

---

## 5. Architektura i stack

🔬 Zweryfikowane: 6 niezależnych badań.

- ✅ **Custom Next.js + Supabase (Postgres) + Stripe + Tailwind/shadcn.** Dla produktu opartego na treści i integracjach (nie na silniku sklepu) — obroniony 2026→2035. Gotowa platforma (Shopify/Medusa) *obniżyłaby* trwałość, narzucając model, który nie pasuje.
- **Trwały rdzeń = Postgres + model danych, który posiadamy, + Stripe.** Next.js/Supabase to wymienna „skóra".
- **Zaskoczenie (🔬):** najbardziej „zaklejający" jest sam Next.js (wiąże kod z frameworkiem+Vercel), nie Supabase. Ubezpieczenie: logika biznesowa w zwykłych modułach TS, Supabase traktowany jak hostowany Postgres.
- **Trzy zmienne za cienką granicą** (podmiana = konfiguracja, nie przebudowa): **Gelato** (druk — łatwo dołożyć Prodigi pod premium canvas), **model AI** (przez agregator typu fal.ai — modele zmieniają się co ~rok), **CDN obrazków** (trzymamy klucze plików, nie gotowe URL-e).
- **Gotowe pod AI-native (tanio, teraz):** czysty ustrukturyzowany feed produktów + stałe ID/URL-e → prawie darmowa gotowość na wyszukiwanie AI/wizualne i agentowe zakupy (ACP/UCP/MCP). `pgvector` w Postgresie ogarnia wyszukiwanie semantyczne/wizualne natywnie.

---

## 6. Reguła nadrzędna: SZWY vs SILNIKI (nie przeinżynierować)

🔬 #1 przyczyna śmierci startupów = budowanie pod skalę/funkcje przed klientami (74%).
- **Szew** = cienka nazwana granica + czysty model danych. Tani teraz, drogi później → rysujemy od dnia zero (Gelato, `ArtworkSource`, model AI, CDN, płatności).
- **Silnik** = ciężka maszyneria za szwem. Drogi teraz, tani później → budujemy dopiero, gdy dane zza jego szwu powiedzą „warto".
- **Reguła trójki:** brak abstrakcji, dopóki wzorzec nie pojawi się 3. raz.
- **Nudny stack**, jeden Postgres na wszystko.
- Jedyna „przyszłościowa" abstrakcja warta dnia 1: rozdzielenie grafika↔produkt↔zamówienie + zamrażanie zamówień.

### Inwarianty 2035 (trzymane od dnia zero, za darmo — w szwach i modelu danych)
1. **Graf klienta + dane first-party = jedyny trwały aktyw.** Wszystko pisze do niego (lista mailowa + maile transakcyjne od PIERWSZEGO zamówienia).
2. **Produkcja, grafika, AI = wynajęte utilities za szwami**, nie rdzeń.
3. **Prywatność jako cecha produktu**, nie compliance: „nie trenujemy na Twoich danych", przetwarzanie efemeryczne. Krytyczne od momentu, gdy dotkniemy zdjęć osobistych (silnik #2).
4. **Firma mała i zlewarowana z założenia** („kilka osób + agenci", nie skalowanie etatami).
5. **Produkt fizyczny/trwały/kurowany** — kontrpozycja do świata zalanego pikselami; deficytem jest autentyczność, nie kolejne piksele.

---

## 7. ⛔ Czego NIE budujemy teraz

- **Generator AI** (typu Mixtiles Pet Portraits) — treadmill, nie fosa; prawnie: nie posiadamy wygenerowanych obrazów jako prawo autorskie, uploady = największe ryzyko. Później, jako lejek. Zaszyć tylko tanie stuby (tabela `generation_jobs`, kolumna `pgvector`, interfejs `lib/imagegen` bez hardkodowania modelu).
- **Pełna automatyzacja self-serve** — auto-wypłaty Stripe Connect na skalę, auto-moderacja bez człowieka, otwarta rejestracja bez bramki. Bramka + ręczna pierwsza partia zostają; automat dochodzi przy wolumenie.
- **Osobna wyszukiwarka (Algolia/Typesense)** — Postgres FTS + pgvector wystarczą długo za start.
- **Multi-vendor plumbing, CQRS, mikroserwisy, multi-tenancy.**

---

## 8. 🟡 Otwarte pytania / do decyzji

- **Liczby do cennika:** nasza marża %, wysokość stałej alokacji kosztów na sztukę, dokładny limit % artysty, podłoga marży.
- **Wycena zestawów/ścian** — suma sztuk czy rabat pakietowy? (naturalny kolejny temat, łączy się z cennikiem)
- **Kto ustala cenę bazową druku** — dom (my) narzuca cennik rozmiarów/materiałów; artysta steruje tylko swoim %? (proponowane: tak)
- **Domyślny % artysty** — start 30% (✅ ustalone), do potwierdzenia widełki min/max.
- **Panel artysty** — co dokładnie widzi i kontroluje (grafiki, %, statystyki, wypłaty).
- **Discovery** — wyszukiwanie, „więcej podobnych", feed. Kiedy i jak.
- **Marketing/ruch** — 🔬 nie liczyć na SEO (AI Overviews tną organik); plan: płatny social + email/SMS + rozpoznawalność marki.
- **VAT** — potwierdzić progi i zmianę €3/paczkę 2026 z księgowym przed startem.
- **Otwieranie podaży** — invite-only → aplikacja z jurorowaniem → (może nigdy w pełni otwarte). Późniejsze decyzje.

---

## 9. Źródła i co zweryfikowane vs założone

Zrzuty z researchu (teardown Mixtiles ekran-po-ekranie + mockupy buildera) → folder `research/` w tym katalogu. Pełny log wniosków + źródła (URL-e) z ~12 raportów badawczych: pamięć projektu asystenta (`latenca-mixtiles-strategy-research.md`, przeładowywana co sesję) — do wyeksportowania tutaj na życzenie.

**Zweryfikowane (niezależne, potwierdzone):** przychody Mixtiles/Displate, upadek Society6/Redbubble, orzeczenia US Copyright Office (AI-grafiki nieobjęte prawem autorskim), matematyka gross-up, norma cache+resync dla POD, VAT OSS/IOSS UE, drabina modeli cenowych POD.

**Założone / do potwierdzenia:** dokładne tabele kosztów Gelato (za loginem — znane tylko poglądowe $7→$25), progi VAT €10k i opłata €3/paczkę 2026 (źródła wtórne — sprawdzić dyrektywę EC), „liczenie od netto" (wyprowadzone z zachowania Stripe/Gumroad/Etsy), proporcja plik-vs-druk 4–10× (wzorzec rynkowy, nie reguła).

**Nie zweryfikowane bezpośrednio:** jakość/cena/szybkość live generacji AI Mixtiles, ich apka mobilna, ich wewnętrzny stack, finanse poza prasą.
