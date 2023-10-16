import sys
import re

re_separateur = re.compile("[ \t]+")
chemin_fichier = 'carnet_adresse.txt'

try:
    descripteur = open(chemin_fichier, "r") # le petit r correspond au mode lecture
except Exception as e:
    print(e.args)
    sys.exit(1)
while 1:
    ligne = descripteur.readline()
    if not ligne:
        break
    eclatement = re_separateur.split(ligne)
    print(eclatement)
descripteur.close()