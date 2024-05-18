#======Troisième Exo======
import random
chiffreAleatoire = random.randint(1, 10)
compteur = 0
while 1:
    valeur = input("Entrez votre proposistion : ")
    compteur += 1
    if (int(valeur) == int(chiffreAleatoire)):
        print("Bravo ! ", end="")
        print("Vous avez réussi en %d essais"%compteur)
        break
    if (int(valeur) > int(chiffreAleatoire)):
        print("Chiffre trop grand")
    else:
        print("Chiffre trop petit")