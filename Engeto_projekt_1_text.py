"""
Projekt_1.py: První projekt do Engeto Online Python Akadeie

author: Jiří Mlčkovský
email: jiri.mlckovsky.obchod@obchod.cz
discord:nemám založený profil na discordu
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# vypsání všech uživatelů

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# zadaní uživatelského jmená a hesla

username = str(input("Please enter a username:"))
password = str(input("Please enter a password:"))
cara = "-" * 40
# ověření přihlášení uživatele a hesla
if users.get(username) == password:
    print (cara,f"Welcome to the app, {username}.","We have 3 text to be analyzed.", cara, sep ="\n")

else: # při zadání neplátných údajů program upozorní uživatele a ukončí ho
    print (f"Unregistered user, terminating the program...")
    quit("Closing program.")

# program nechá uživatele vybrat mezi 3 texty (listu), uložené v proměnné TEXT

vyber_textu = int(input("Enter a number btw. 1 and 3 to selected:")) # zadání vstupu uživatele

if int(vyber_textu) <= 3 and int(vyber_textu) >=1:                             # volba do 3
    print(cara)
else:
    print(cara, "Wrong number", sep="\n")

# rozdělení stringu v textu s indexací od konce, ve výběru textu jsem si dal, aby to bylo do 3 a tady si zvolím číslo
zvolene_cislo = TEXTS[int(vyber_textu) - 1].split()


# všechna slova pro zvolený text
pocet_slov = []

for slova in zvolene_cislo:
    cisty_text = slova.replace(".,", " ")   # nahradím si . a , mezerou jinak jsem chtěl použít metodu strip, ale to mi vrací divné hodnoty jiné, než ktré jsou v 5 lekci v ukázce
    pocet_slov.append(cisty_text)
print(f"There are {len(pocet_slov)} words in the selected text.")

# Vybrat slová které začínájí velkým písmenem.

prvni_velka = []

for slova in zvolene_cislo:
    if slova.istitle():
        prvni_velka.append(slova)
print(f"There are {len(prvni_velka)} titlacse words.")

# Slova v textu celé velkými písmeny

vsechna_velka = []

for slova in zvolene_cislo:
    if slova.isupper():
        vsechna_velka.append(slova)
print(f"There are {len(vsechna_velka)} uppercase words.")

# Slova v textu zaínající malým písmenem

mala_slova = []
for slova in zvolene_cislo:
    if slova.islower():
        mala_slova.append(slova)
print(f"There are {len(mala_slova)} lowercase words.")

# čísla v textu

text_cisla = []
for slova in zvolene_cislo:
   if slova.isnumeric():
       text_cisla.append(slova)
print(f"There are {len(text_cisla)} numeric strings")

# součet čísel v textu

cisla_soucet = 0
for slova in zvolene_cislo:
    if slova.isnumeric():
        cisla_soucet += int(slova)

print(f"The sum of all numbers {cisla_soucet}")

# vypsaní slopcového grafu  četnost různých délek v textu.

print(cara)
print ("LEN|", "OCCURENCES".center(30), "|NR.")
print(cara)

# projde a seřádi délky a četnost slov v textu

delka_slov = {}

for slova in zvolene_cislo:
    if len(slova) not in delka_slov.keys():
        delka_slov[len(slova)] = 1
    else:
        delka_slov[len(slova)] = delka_slov[len(slova)] + 1

for delka in sorted (delka_slov.keys()):   # seřazení
    pocet_opakovani = delka_slov[delka]
   # cele to vytiskne
    print(f"{delka:>3} | {'*' * pocet_opakovani:^15} |{pocet_opakovani:>15}",
            sep="n")


























