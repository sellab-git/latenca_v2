# BRIEF dla ChatGPT — pressure-test intencji użytkowników i flow

> Do wklejenia/wysłania ChatGPT jako senior reviewer. Repo jest publiczne: **https://github.com/sellab-git/latenca_v2** (folder `docs/`). Jeśli możesz przeglądać sieć — przeczytaj pliki z sekcji 2. Jeśli nie — Artur wklei je obok tego briefu.

---

## 1. Twoja rola i zasady gry

Jesteś **senior product reviewer / sparing-partnerem** dla Latenki. Masz być **krytyczny i uczciwy**, nie potakiwać. Twoje zadanie: pressure-test mapy intencji użytkowników i zaproponowanego zwinięcia do flow — znaleźć dziury, błędne granice, złą kolejność i pułapki over-buildu.

Twarde zasady, w których się poruszasz (nie podważaj ich, chyba że wskazujesz realny konflikt):
- **Zespół = 1 osoba niebędąca programistą (Artur) + AI (Claude).** Wszystko musi być **solo-buildowalne**. Skala benchmarku: mały biznes ($2k–30k/mies.), nie Displate/Saatchi.
- **Latenca sprzedaje TYLKO fizyczne druki** (Gelato POD; ramy/materiały opcjonalne). **Bez plików cyfrowych** (D-036).
- **Doradca AI PROPONUJE, użytkownik OGLĄDA / akceptuje / wymienia — nigdy nie przeciąga i nie układa sam** (D-033). To nie jest edytor/canvas.
- **Kuracja to tożsamość; AI to źródło, nie tożsamość.** „Sprzedajemy pewność decyzji, nie same obrazy."
- Doradca to **drzwi frontowe, nigdy bramka** — kup-od-ręki zawsze dostępne (D-022).
- **Jedna sesja, bez profilu per-klient** (D-024) — to obecna blokada; jeśli uważasz, że trzeba ją poluzować dla powrotów, powiedz wprost.
- **Największe realne ryzyko biznesu to dystrybucja/CAC, nie konwersja.** CAC ~$55–120 vs ~$40 zysku/zamówienie → pojedyncza sprzedaż na zimnym ruchu jest stratna; **kolejna sztuka w tej samej paczce ~€0,29** → zestawy dramatycznie poprawiają ekonomię.
- ⛔ **Nie używaj analogii do „cmentarza startupów AI-projektujących-wnętrza" (Modsy itp.).** To były usługi z ludźmi; my jesteśmy AI-run. Ta analogia jest u nas zbanowana — nie wnoś jej.

---

## 2. Co przeczytać (repo `docs/`)

1. **`USER-INTENTS.md`** — SYNTEZA: framework 6 osi, model 9 faz, zwinięcie 178 scenariuszy do **13 flow** (ze statusem: mamy / częściowe / luka), 10 sygnałów przekrojowych, 7 forków. **To jest główny przedmiot Twojej recenzji.**
2. **`USER-INTENTS-CATALOG.md`** — pełne **178 scenariuszy** w 6 wymiarach (referencja: kto · dlaczego · czego szuka · co wnosi · jednostka · faza-po-fazie · gdzie się psuje).
3. **`VISION.md`** i **`PRODUCT_BIBLE.md`** — czym jest Latenca; rdzeń = „ściana/zestaw", nie pojedyncze dzieło; ekonomia druku/zestawów.
4. **`DECISIONS.md`** — zablokowane decyzje D-001…D-046 (m.in. D-023 MVP=jedna grafika, D-033 wielo-grafika = „the one structural gap", D-034/D-046 doradca wbudowany w produkt, D-038 landing=katalog).
5. **`PROJECT_STATUS.md`** — bieżący stan (co zbudowane: landing + produkt-z-doradcą „model D" na jednej grafice + koszyk to następny ekran).

**Stan obecnej budowy w jednym zdaniu:** landing = katalog; strona produktu ma wbudowanego doradcę (model D) działającego na JEDNEJ grafice (dobierz/zamień jedną pracę, skonfiguruj materiał/rozmiar/ramę, do koszyka); MVP = pojedyncza grafika; wielo-grafikowe ściany = świadoma, zapisana luka.

---

## 3. Co dokładnie chcemy USTALIĆ (Twoje deliverable)

Odpowiedz na to konkretnie i z uzasadnieniem. Cytuj numer flow / D-decyzji / scenariusza, gdy się odnosisz.

**A. Kompletność.** Czy 178 scenariuszy + 13 flow pokrywa realną przestrzeń? **Czego brakuje** — jakich intencji, potrzeb, ścieżek nieudanych, typów klienta lub faz nie widzimy? (Szczególnie: czy pominęliśmy coś częstego lub coś tanio-obsługiwalnego o dużym wpływie.)

**B. Poprawność zwinięcia.** Czy podział na **13 flow** ma dobre granice? Które **scalić**, które **rozbić**? Czy któryś „flow" to tak naprawdę dwa różne produkty (np. B2B)?

**C. SEDNO — zestawy (flow 4).** To jest nasz nr 1 fork. Przy zasadzie „AI proponuje, Ty oglądasz, nigdy nie układasz":
- Czy i JAK wprowadzić wielo-grafikowe zestawy **bez budowania edytora/canvasu**?
- Jak to wygląda **faza-po-fazie** (od wejścia do koszyka) dla: pary, tryptyku, gallery wall 3–5, „dobierz do posiadanego"?
- Czy „zestaw = jeden kuratorowany produkt-aranżacja, który akceptujesz/wymieniasz" to dobra forma, czy jest lepsza?
- Jak to godzi się z ekonomią (AOV vs CAC) i z solo-buildowalnością w makiecie (udawane AI)?

**D. Priorytetyzacja MVP.** Który **podzbiór flow** to MVP dla solo-foundera? Oceń każdy z 13 flow z 4 stron: (1) realność/częstość, (2) solo-buildowalność + czy da się „udać AI" w makiecie teraz, (3) ekonomia (czy prowadzi do AOV bijącego CAC), (4) tożsamość marki. **Co świadomie ciąć/odłożyć** i dlaczego.

**E. Ryzyka i pułapki.** Gdzie ta mapa prowadzi do **over-buildu** (budowa przed walidacją)? Gdzie jest największe ryzyko produktowe? Co jest **tanie a wysokiego wpływu** (quick win), a co **drogie a niepewne**?

**F. Sekwencja budowy.** Konkretna, uszeregowana kolejność: co budujemy jako pierwsze, drugie, trzecie — i dlaczego w tej kolejności.

**G. Architektura „nie zablokuj się".** Co musimy założyć **JUŻ teraz** w modelu danych/flow (nawet jeśli budujemy tylko makiety), żeby później nie trzeba było przepisywać? Np.: czy „ściana/zestaw" musi być obiektem od początku? Czy konto/pamięć zamówień (dla powrotów, flow 10) trzeba przewidzieć teraz? Czy „projekt ściany" to pierwszorzędny obiekt?

---

## 4. Format odpowiedzi (żebyśmy mogli to wrzucić do repo)

Zwięźle, opiniotwórczo, uszeregowane:
1. **Braki** — lista brakujących intencji/flow/faz (z krótkim uzasadnieniem każdej).
2. **Werdykt o 13 flow** — które trzymają, które scalić/rozbić.
3. **Rekomendacja SETY** — forma + flow faza-po-fazie + ekonomia.
4. **Zestaw flow na MVP + kolejność** — z uzasadnieniem per flow (4 strony z pkt D).
5. **Top 5 ryzyk** — i po jednym ruchu ograniczającym każde.
6. **Pytania zwrotne do nas** — czego potrzebujesz od Artura, żeby doprecyzować.

---

## 5. Czego NIE rób

- Nie przeprojektowuj **wizualnego UI** (kolory/layout) — to jest zrobione i zablokowane.
- Nie otwieraj na nowo zablokowanych decyzji D-xxx, **chyba że** wskazujesz realny konflikt — wtedy nazwij go wprost.
- Nie proponuj jako MVP **ciężkiej wielo-ekranowej podróży** (wgraj zdjęcie ściany → animacja analizy → osobny ekran profilu stylu) ani rzeczy wymagających **prawdziwego modelu AI/vision** — to jest ryzyko, którego unikamy; jeśli coś tego wymaga, oznacz to jako „v2, wymaga realnego AI".
- Żadnych analogii do Modsy / „cmentarza AI-designerów".
- Zawsze kotwicz się w **solo-buildowalnej rzeczywistości** — jeśli coś wymaga zespołu/kapitału, powiedz to wprost.
