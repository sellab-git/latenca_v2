# MERGE-STRATEGY — jak Displate wpina się w produkt „best of best 2026"

Cel: opisać, co z modelu Displate warto przenieść do naszego systemu wall-art i jak
połączyć to z wcześniej przeanalizowanymi filarami (Fy! = Art Advisor, Mixtiles =
personalizacja/wall-preview, Ideogram = generacja AI). Displate wnosi tu przede
wszystkim **marketplace twórców + fizyczny produkt premium + mechaniki e-commerce**.

> Uwaga licencyjna: Displate opiera się mocno na licencjonowanym IP (gaming, anime,
> filmy). My tego NIE kopiujemy. Bierzemy **mechanikę i architekturę**, nie treści
> ani nazw kolekcji. Własny katalog budujemy z twórców + generacji AI + domeny publicznej.

## Co bierzemy od Displate (wzorce, nie kopie)
- **Konfigurator produktu jako serce PDP**: wykończenie (mat/połysk/tekstura),
  rozmiar (S/M/L/XL, w tym warianty wieloelementowe), rama/oprawa — z żywym podglądem
  i natychmiastową zmianą ceny.
- **Marketplace twórców**: profile artystów, weryfikacja („Verified Creator"),
  podział przychodu, kuratorowane kolekcje. To skalowalne źródło podaży treści.
- **Mechaniki commerce**: rabaty ilościowe („taniej od 2 szt."), odliczanie promocji,
  zgodność z Omnibus (przekreślona „najniższa cena z 30 dni"), dowód społeczny
  (Trustpilot, liczba recenzji, „officially licensed / X artworks").
- **System hangingu jako USP**: prosty, „bez wiercenia" montaż jako element narracji
  produktu i differentiator — u nas odpowiednik: własny standard oprawy/montażu.
- **Eksploracja katalogu**: filtry po kategorii/fandomie, „bestselling", karty
  produktu z szybkim podglądem wariantów.

## Czego NIE bierzemy
- Licencjonowanego IP i nazw kolekcji (Marvel, Elden Ring, One Piece itd.).
- Konkretnych tekstów, grafik, brandingu i identyfikacji Displate.
- 1:1 struktury URL/nazewnictwa — inspirujemy się, nie klonujemy.

## Mapa filarów w połączonym produkcie
| Filar | Rola w „best of best 2026" | Źródło wzorca |
|------|------------------------------|----------------|
| Art Advisor | Dobór dzieła do wnętrza/gustu (quiz, room-match) | Fy! |
| Wall Preview / Personalizacja | Podgląd na ścianie, kadr, układ galerii | Mixtiles |
| Generacja AI | Tworzenie unikatowych grafik na życzenie | Ideogram |
| Marketplace + Produkt fizyczny | Podaż twórców, konfigurator, fulfillment | Displate |

## Synergia
- Generacja (Ideogram) zasila marketplace i custom (nowa podaż treści).
- Advisor (Fy!) kieruje ruch do konkretnych dzieł i wariantów produktu, zamiast
  zostawiać użytkownika z pustym katalogiem — rekomendacja → PDP z gotowym wariantem.
- Wall Preview (Mixtiles) domyka decyzję zakupową: użytkownik widzi dzieło z
  marketplace / z generacji AI na własnej ścianie przed zakupem.
- Marketplace + konfigurator (Displate) zamienia „obraz na ekranie" w realny,
  premium produkt fizyczny z jasnym cennikiem wariantów i mechaniką up-sellu.
- Pętla wartości: Advisor przyciąga → AI/twórcy dostarczają unikatową treść →
  Preview przekonuje → Konfigurator + commerce konwertują → recenzje i profile
  twórców budują dowód społeczny, który znów zasila Advisor.

## Wspólne komponenty do zbudowania raz (reużywalne)
- **Product Configurator** (wariant/wykończenie/rozmiar/rama + cena na żywo).
- **Wall Preview Engine** (podgląd dzieła w kontekście ściany/pokoju).
- **Recommendation/Advisor Service** (dobór treści do użytkownika i wnętrza).
- **Generation Service** (kolejka, style, prawa do treści wygenerowanej).
- **Creator Marketplace** (profile, weryfikacja, payout, kuratorowanie).
- **Commerce Core** (koszyk, rabaty ilościowe, promocje, Omnibus, checkout).
- **Trust Layer** (recenzje, oceny, oznaczenia jakości/pochodzenia).

## Priorytet integracji (co najpierw)
1. Commerce Core + Product Configurator (bez tego nie ma sprzedaży).
2. Wall Preview + Advisor (podnoszą konwersję na istniejącym katalogu).
3. Generation Service (różnicujący, ale wymaga zarządzania prawami).
4. Creator Marketplace (skalowanie podaży — etap wzrostu).

## Ryzyka i jak je adresujemy
- **Prawa do treści (AI + twórcy)**: jasne warunki licencyjne przy generacji i
  onboardingu twórców; brak licencjonowanego IP bez umowy.
- **Jakość fulfillmentu produktu fizycznego**: to najtrudniejszy operacyjnie element
  modelu Displate — pilotaż z jednym dostawcą druku/oprawy przed skalowaniem.
- **Zgodność cenowa (Omnibus/promocje)**: mechanika „najniższa cena z 30 dni" i
  odliczania musi być poprawnie liczona po stronie backendu, nie tylko UI.
- **Przeciążenie UX**: cztery filary naraz mogą przytłoczyć — Advisor jako „warstwa
  prowadząca", która ukrywa złożoność.

## Sygnał sukcesu integracji
Użytkownik wchodzi bez pomysłu, Advisor proponuje dzieło (z katalogu, twórcy lub
generacji), widzi je na swojej ścianie, konfiguruje wariant premium i kupuje — w
jednym, spójnym przepływie, bez przeskakiwania między „osobnymi produktami".
