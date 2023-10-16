import sys

chemin_fichier = "Exo 1.py"

try:
    descripteur = open(chemin_fichier, "r")
except Exception as e:
    print(e.args)
    sys.exit(1)

while 1:
    ligne = descripteur.readline()
    if not ligne:  
        break
    else:
        compteur_lignes =+ 1
    print = ('nombre de lignes : ', compteur_lignes)
descripteur.close()
