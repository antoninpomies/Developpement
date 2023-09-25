#!/usr/bin/python3

import random

valeur_aleatoire = random.randint(1, 100)

compteur = 0
while 1:
    proposition = int(input("Quelle est votre proposition :"))
    compteur += 1
    # compteur = compteur + 1
    if (proposition == valeur_aleatoire):
        print("Bravo !!! Vous avez trouvé en %d essais"% compteur)
        break
    if (proposition > valeur_aleatoire):
        print("Proposition trop grande")
        continue
    print("Proposition trop petite")
