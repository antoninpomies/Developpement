import sys

chemin_fichier = "carnet_adress.txt"

try:
    descripteur = open(chemin_fichier, "a")
except Exception as e:
    print(e.args)
    sys.exit(1)

nom = input("Nom : ")
prenom = input("Prenom : ")
adress = input("Addresse : ")

#Methode par concaténation seulement avec des strings
ligne = nom + ':' + prenom + ':' + adress + '\n'
#Methode par substitution %s = chaine %d = entier
ligne = '%s : %s : %s\n' % (nom, prenom, adress)

descripteur.write(ligne)
descripteur.close()