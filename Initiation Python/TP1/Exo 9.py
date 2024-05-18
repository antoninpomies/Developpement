#!/usr/bin/python3

import sys

chemin_fichier = 'carnet_adresse.txt'

try:
    descripteur = open(chemin_fichier, "a") # le petit a correspond a ajout
except Exception as e:
    print(e.args)
    sys.exit(1)

nom = input("nom :")
prenom = input("prenom :")
adresse = input("adresse :")

# méthode par concaténation
# attention ne marche pas pour des chainews de caracteres
ligne = nom + ' : ' + prenom + ' : ' + adresse + ' : ' + '\n'

# méthode de substitution
# indiquer le type %s -> chaine, %d -> entier, etc
ligne = '%s : %s : %s\n' % (nom,prenom,adresse)

descripteur.write(ligne)
descripteur.close()