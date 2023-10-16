import sys

chemin_fichier = "carnet_adress.txt"

try:
    descripteur = open(chemin_fichier, "a")
except Exception as e:
    print(e.args)
    sys.exit(1)

nom = input("Saisissez Votre Nom : ")
prenom = input("Saissisez Votre Prenom : ")
adress = input("Saissisez Votre Addresse : ")

ligne = nom + ':' + prenom + ':' + adress + '\n'

descripteur.write(ligne)
descripteur.close()