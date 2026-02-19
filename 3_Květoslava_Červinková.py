"""
Identifikační údaje o autorovi projektu:
    Jméno a příjmení: Květoslava Červinková
    tel.: 739 623 999
    e-mail: cervinkova.kveta@seznam.cz
"""
# importuje vestavěný modul "os"
import os

# vytvoří funkci, která bude převádět písmeno z batohu na odpovídající prioritu
def vypocitani_priority(pismeno):
    """
    Funkce pro vypocitani_priority
    
    :param pismeno: písmeno, u kterého chceme spočítat prioritu
    :return: vrací vypočítanou hodnotu
    """
    priorita = 0
    if "a" <= pismeno <= "z":
        priorita += ord(pismeno) - ord("a") + 1
    elif "A" <= pismeno <= "Z":
        priorita += ord(pismeno) - ord("A") + 27
    return priorita

# vytvoří funkci, která bude počítat výslednou prioritu podle množství výskytů
def vysledna_priorita(priorita, pocet_vyskytu):
    """
    Definice pro výpočet hodnoty vysledné priority v batohu
    
    :param priorita: Hodnota jakou má písmeno prioritu
    :param pocet_vyskytu: Hodnota kolikrát se písmeno v batohu vyskytuje
    :return: vrací vypočítanou hodnotu
    """
    vysledek = priorita * pocet_vyskytu
    return vysledek

# program načte částku ke složce s daty
cesta_slozky = os.path.dirname(__file__)
# program načte cestu ke vstupnímu souboru
cesta_souboru = os.path.join(cesta_slozky, "batohy_vstup.txt")

# program vypíše nadpisy a cestu ke složce a souboru
print("\nVyhledání společných věcí v každém batohu")
print("*" * 41)
print()

print(f"Cesta ke složce aktuálně spuštěnému programu:\n{cesta_slozky}\n")
print(f"Cesta ke vstupnímu souboru s popisem batohů:\n{cesta_souboru}\n")

print("Obsah batohů v první a ve druhé polovině (odděleno mezerou)")
print("*"* 59)
print()
# nastavení proměnných celkovy_soucet_piorit a seznam_spolecnych_predmetu
celkovy_soucet_priorit = 0
seznam_spolecnych_predmetu = []

# program otevře vstupní soubor "batohy_vstup.txt"
with open(cesta_souboru, "r") as vsechno:
    # program načte jednotlivé řádky a uloží jako seznam bez neviditelných znaků
    batohy = [line.strip() for line in vsechno.readlines()]

for prihradky in batohy:
    # program rozdělí přihrádky na dvě 
    pulka = len(prihradky) // 2
    prvni_prihradka = prihradky[:pulka]
    druha_prihradka = prihradky[pulka:]
    # program zjistí jaké písmeno se nachází v obou částech a přidá ho do seznamu_spolecnych_predmetu
    spolecne_pismeno = set(prvni_prihradka).intersection(druha_prihradka)
    spolecne_pismeno = list(spolecne_pismeno)[0]
    seznam_spolecnych_predmetu.append(spolecne_pismeno)
    
    # program spočítá, kolikrát se nalezený předmět v batohu vyskytuje a uloží výsledek do proměnné
    pocet_vyskytu = prihradky.count(spolecne_pismeno)

    # program zavová vytvořené funkce a vypočítá prioritu 
    priorita = vypocitani_priority(spolecne_pismeno)
    priorita_celek = vysledna_priorita(priorita, pocet_vyskytu)

    # program postupně sčítá všechny priority
    celkovy_soucet_priorit += priorita_celek
    
    #program vypíše první a druhou část bahotu oddělené mezerou
    print(f"{prvni_prihradka} {druha_prihradka}\n ")
    

print("\nZjištěné informace o batozích")
print("*" * 29)
print()

# program vypíše seznam_spolecnych_predmetu v každém batohu
print(f"Seznam společných položek v každém batohu: {seznam_spolecnych_predmetu}")

# program vypíše celkový součet priorit u všech batohů
print(f"\nCelkový součet priorit u všech batohů: {celkovy_soucet_priorit}\n")
