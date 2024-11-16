## Feladat: Koncertjegyek kombinációinak számlálása

Adott egy `n` egész szám, amelyet egy kocka dobásával el kell érni különböző kombinációkkal. A cél az, hogy meghatározzuk, hányféleképpen lehet az `n` összértéket elérni úgy, hogy a kockával 1 és 6 közötti számokat dobunk egy vagy több alkalommal.

Minden lehetséges kombináció esetén a kockadobások eredményeinek összege pontosan `n` legyen.

### Bemenet

- Az első és egyetlen sorban egy egész szám található, `n` (1 ≤ n ≤ 10^6), amely a célszámot jelöli, amelyet el kell érnünk.

### Kimenet

- Egyetlen egész számot kell kiírni: annak a módjait, hogy hányféleképpen lehet elérni az `n` értéket a leírt kockadobásokkal, modulo 10^9+7.

### Példa

#### Bemenet:

3

#### Kimenet:

4

### Magyarázat

Ha `n = 3`, akkor az `n` összértéket az alábbi módokon érhetjük el:

- 1 + 1 + 1
- 1 + 2
- 2 + 1
- 3

Ez összesen 4 különböző módot jelent az összeg elérésére, ezért a kimenet `4`.

### Megjegyzés

A megoldás során dinamikus programozást és memoizálást érdemes alkalmazni a hatékony megoldáshoz. A `10^9+7` modult használjuk minden számoláskor, hogy az eredmény nagy `n` esetén is kezelhető maradjon.
