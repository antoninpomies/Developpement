import sys

chemin_fichier = r'exo8.py'  # petit r correpond au terme Raw

try:
    entree = open(chemin_fichier, "r")
except Exception as e:
    print(e.args)
    sys.exit(1)

try:
    sortie = open(chemin_fichier+'.copy', "w")
except Exception as e:
    print(e.args)
    sys.exit(1)




while 1:
    ligne = entree.readline()
    if not ligne:
        break
    #écrire la première ligne
    sortie.write(ligne)
    #sauter une ligne
    ligne = entree.readline()
    if not ligne:
        break
entree.close()
sortie.close()