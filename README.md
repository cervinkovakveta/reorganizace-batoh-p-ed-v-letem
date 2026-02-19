# reorganizace-batohu-pred-vyletem
Tento program řeší logickou úlohu rozdělení obsahu batohů do dvou sekcí a hledání společných prvků s následným výpočtem jejich priority.

Součásti projektu
 Hlavní skript programu.
 `batohy_vstup.txt` - Vstupní data (seznam položek v batozích). Program očekává, že tento soubor bude ve stejném adresáři.


Použití modulu `os` zajišťuje, že skript najde vstupní soubor bez ohledu na to, v jaké složce je spuštěn (`os.path.dirname(__file__)`).
Efektivní hledání průniku dvou částí řetězce pomocí `set().intersection()`.
Implementace vlastní logiky pro převod ASCII hodnot písmen (a-z, A-Z) na číselné priority.

