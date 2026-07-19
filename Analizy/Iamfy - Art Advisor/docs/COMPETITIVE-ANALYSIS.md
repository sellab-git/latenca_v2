# Analiza konkurencji — Fy! Art Advisor

## Co robią (zaobserwowane)
Konwersacyjny asystent osadzony w sklepie Shopify. Flow: ekran "wejścia do pokoju" →
opcjonalny quiz (3 pytania: rozmiar ściany, liczba prac, styl) LUB opis tekstowy →
generacja 3 "kuracji" z nazwą, ceną, opisem AI → wizualizacja obrazu w ramie na generycznej
ścianie → pas rekomendacji "For You" → shortlist i przejście do koszyka.
Identyfikacja sesji bez logowania (fingerprint). Stack: SvelteKit + Vite + Shopify.

## Ich mocne strony (do zachowania w naszej wersji)
- Niski próg wejścia dzięki językowi naturalnemu.
- Natychmiastowa ekstrakcja intencji (pokazują wykryty pokój/styl jako tagi).
- Wizualizacja w ramie + jednozdaniowy opis AI budują pewność zakupu.
- Bezstanowa sesja (fingerprint) = zero tarcia.
- Dopracowane copy i estetyka budujące nastrój.

## Ich słabości (NASZE SZANSE)
| Słabość Fy! | Nasza przewaga |
|---|---|
| Quiz płytki (3 pytania) | Głębszy, adaptacyjny brief: budżet, paleta wnętrza, oświetlenie, ramy |
| Wizualizacja = generyczny mockup | Prawdziwa wizualizacja na ZDJĘCIU pokoju użytkownika (inpainting) jako funkcja pierwszoklasowa |
| Brak uzasadnień rekomendacji | Transparentne "dlaczego to pasuje" przy każdej pracy |
| Brak nauki z odrzuceń | Pętla uczenia się z lajków/odrzuceń w obrębie sesji i profilu |
| Personalizacja tylko na sesję | Trwały StyleProfile (opcjonalny), wektorowe dopasowanie gustu |
| Brak funkcji społecznych | Współdzielenie projektu ściany do konsultacji |

## Wniosek strategiczny
Zachowujemy sprawdzony szkielet (czat + quiz → jeden silnik → wizualizacja → stan sesji),
ale wygrywamy na: (a) realnej wizualizacji w pokoju użytkownika, (b) transparentności rekomendacji,
(c) głębi personalizacji. To są trzy filary różnicujące.
