# Latenca — status strategiczny

> Stan na 2026-07-19. Ten dokument mówi, **gdzie jesteśmy z myśleniem** o biznesie — nie o kodzie.
> Zasada: każde twierdzenie oznaczone jako ZWERYFIKOWANE (źródło) albo ZAŁOŻENIE (do sprawdzenia).

---

## Czym jest Latenca

Kurowana marka sztuki generowanej przez AI, sprzedawanej jako **fizyczne druki** (print-on-demand przez Gelato) + pliki cyfrowe. Nie marketplace, nie generator — **marka**. Prototyp (8 ekranów) jest gotowy i ładny; biznes pod nim — dopiero się klaruje.

**Uczciwy stan:** nic nie wystartowało. To faza przed-budową. Piękny prototyp to najłatwiejsza część i już ją mamy. Brakuje najtrudniejszej — patrz „Największa dziura" niżej.

---

## Co ZDECYDOWANE (i ma pod sobą dowody)

1. **Kurowana marka, nie otwarty marketplace.** (zdecydowane 2026-07-07). Dowody z późniejszych badań tylko to wzmocniły: Mixtiles i Desenio nie mają zewnętrznych artystów; prawo autorskie i tak wymaga człowieka przy każdej pracy; trzy rundy badań o artystach *osłabiły* historię o podaży, nie wzmocniły.

2. **Sprzedawać „całe ściany", nie pojedyncze obrazki.** ZWERYFIKOWANE dwiema drogami:
   - Matematyka Gelato: kolejny druk w tej samej paczce kosztuje **~€0,29 wysyłki**. Klienta pozyskujesz raz — na zamówienie, nie na sztukę.
   - Desenio (lider): **606 gotowych „gallery walls"** + osobne narzędzie do nich + szablony z wymiarami + darmowa wysyłka powyżej $69. Największa kurowana marka plakatowa w Europie robi dokładnie to.

3. **Celować w rynek USA, nie Europę.** ZWERYFIKOWANE (API Gelato). Ten sam produkt daje **~2× marżę** w USA: tańszy druk + brak unijnego VAT przy eksporcie. Szczegóły w [`02-koszty-i-scenariusze.md`](02-koszty-i-scenariusze.md).

4. **Duży format bije mały.** ZWERYFIKOWANE. Druk 70×100 kosztuje tylko €1,42 więcej niż 50×70, a można brać $30 więcej. Małe formaty (30×40) w Europie to pułapka (27% marży).

---

## Co WYCOFANE (tezy, które padły przy zderzeniu z dowodami — NIE wskrzeszać)

- ❌ **„Artyści AI są wypychani z platform, więc przyjdą do nas."** FAŁSZ. Etsy pozwala (z oznaczeniem), Zazzle pozwala, Adobe Stock pozwala, Society6 pozwala z ludzkim wkładem, Displate milczy. Tylko Shutterstock banuje (i to stock, nie druk). Podaży nie opieramy na tej tezie.
- ❌ **„Ludzka kuratela jest niezajęta."** FAŁSZ. Society6 ma prawdziwy zespół kuratorów (do 30 dni review).
- ❌ **„Platformy po cichu biorą prawa do trenowania AI na pracach."** NIEPOTWIERDZONE. Displate nie bierze żadnych praw licencyjnych.
- ❌ **andyokay jako wzór dla jednoosobowej firmy.** FAŁSZ. 226 artystów, marka charytatywna, start z gotową publicznością (prasa, WWF, ONZ **przed** startem). Nie do skopiowania w pojedynkę.
- ❌ **„AI daje nam przewagę kosztową/tempową nad Desenio."** WYCOFANE (2026-07-19). AI oszczędza ~$2 licencji na produkcie za $59 (szum), a tempo produkcji jest bezwartościowe, skoro rynek wycenia wielki katalog na ~zero (patrz niżej).

---

## Dwa realne wyróżniki, które przetrwały

1. **Kontrola ceny przez artystę / brak wymuszonych przecen.** ZWERYFIKOWANE z regulaminów. Nikt tego nie daje: Society6 odebrał artystom kontrolę ceny (2025-03-18, zarobek 5–10% netto); Displate płaci stałą stawkę i sam ustala cenę; Saatchi i Artfinder wymuszają przeceny bez prawa odmowy (Artfinder dosłownie: *„we are unable to offer an opt out"*). **Mała platforma naprawia to jednym zdaniem w regulaminie.** — o ile w ogóle bierze zewnętrznych artystów.
2. **Prowieniencja.** Shutterstock (jedyny ban AI) podał własny powód: nie umie zweryfikować źródła modelu, więc nie może zapewnić, że artyści z danych treningowych dostali wynagrodzenie. To pisemne nazwanie luki, którą kurowana marka dokumentująca pochodzenie mogłaby zamknąć.

> Uwaga: oba wyróżniki dotyczą **artystów**. Jeśli Latenca robi katalog sama (model Mixtiles/Desenio), tracą znaczenie.

---

## Kierunki, które rozważono i ODRZUCONO (2026-07-19)

- **Marketplace plików do druku (setki artystów AI).** ODRZUCONE. Rynek już wycenił wielki katalog: na Etsy bundle **150 000+ grafik za $1,72**. Wielkość katalogu to nie atut — to koszt. Do tego pliki z samego promptu nie mają ochrony prawnej.
- **Publiczny katalog ze zdjęć użytkowników (model TikTok/„zdjęcia innych do druku").** ODRZUCONE (już wcześniej, research 2026-07-09): odpowiedzialność producenta + prawo biometryczne (RODO) na zdjęciach ludzi; nikt nie chce wieszać cudzych wakacji.
- **Czysty model Mixtiles (drukowanie własnych zdjęć klienta).** Mądra połowa (zabija ryzyko rozdzielczości, praw autorskich, zimnego startu), ale: Mixtiles już istnieje i jest duży; „bądź Mixtiles bez ich budżetu" nie ma wyróżnika; przestajesz być marką AI-art, stajesz się usługą druku zdjęć.

---

## Największa dziura (i prawdziwy powód, dla którego to jeszcze nie biznes)

**Dystrybucja.** Każdy, kogo badaliśmy, ma powód, dla którego ludzie o nim słyszą:
- Desenio — 108 000 recenzji i lata SEO
- andyokay — prasa, WWF, ONZ, galeria, charytatywność **przed** startem (pierwszy drop wyprzedał się w 24h, bo miał komu o nim powiedzieć)
- Sprzedawcy z Etsy — cudzy ruch platformy

Latenca ma piękny prototyp i **zero dystrybucji.** To jest cała różnica. Żaden research, personalizacja ani kuratela tego nie załatwi.

**Liczba, której nikt jeszcze nie ruszył — koszt pozyskania klienta (CAC):**

| | Marża | Realny CAC (zimny ruch) | Wynik |
|---|---|---|---|
| Pojedynczy $59 | ~$40 | ~$60–80 | **strata** |
| Zestaw 3× | ~$120 | ~$60–80 | +$40–60 |

Nieznana marka + zimny ruch + konwersja ~1% → ~$80 za klienta. Przy pojedynczych sprzedażach dokładasz do każdej. To zresztą zgadza się z wcześniejszym researchem: *„CAC jest zabójcą, nie generowanie"*.

---

## Pytanie, na które wszystko czeka

> **Do kogo umiesz dotrzeć taniej niż przez płatną reklamę?**

Jakaś grupa / społeczność / nisza, gdzie nie płacisz $80 za klienta. Jeśli odpowiedź brzmi „na razie do nikogo" — to też odpowiedź: znaczy, że **najpierw budujesz publiczność, potem sklep**, nie odwrotnie.

To jest teraz najważniejsze pytanie w projekcie. Nie „co sprzedajemy" i nie „jak wygląda strona".

---

## Otwarte decyzje (Artura)

1. **Dystrybucja** — do kogo docierasz taniej niż reklamą? (blokuje wszystko)
2. **Historia czy wolumen** — Desenio bierze $18–28 bez historii; andyokay $44–59 z historią. Twoje $59 wymaga powodu. Albo budujesz historię, albo schodzisz do $30–45 i grasz wolumenem.
3. **Marka czy self-katalog** — czy Latenca bierze zewnętrznych artystów, czy robi katalog sama (Mixtiles/Desenio nie biorą).
4. **Test wydruku za €25** — zamów jeden plakat 70×100 z grafiką AI, powieś, popatrz. Rozstrzyga największe ryzyko techniczne (czy AI w dużym formacie wygląda jak coś za $89) za cenę kolacji. ODŁOŻONE.
5. **Zestaw elementów personalizacji** — wisi od 2026-07-10 (patrz SPEC 1c–1e).
6. **Research kupujących** — zapowiedziany; ale to pytanie miękkie, którego desk-research nie rozstrzygnie. Prawdziwa odpowiedź wymaga wystawienia oferty, nie googlowania.
