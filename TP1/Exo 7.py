import sys

chemin_fichier = r'exo7.py'  # petit r correpond au terme Raw

try:
    descripteur = open(chemin_fichier, "r")
except Exception as e:
    print(e.args)
    sys.exit(1)

compteur_lignes = 0
while 1:
    ligne = descripteur.readline()
    if not ligne:
        break
    compteur_lignes *= 1
print("nombre de lignes :",compteur_lignes)
descripteur.close()
