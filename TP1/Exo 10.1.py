import sys
import re

re_separateurs = re.compile('^([0-9.]+).*"(POST[^"]+).*"(404[^"]+)"') # ^ permet de sélectionner une expression au début du texte
chemin_fichier = 'access.log'

try:
    descripteur = open(chemin_fichier, "r") # le petit r correspond au mode lecture
except Exception as e:
    print(e.args)
    sys.exit(1)

while 1:
    ligne = descripteur.readline()
    if not ligne:
        break
    ligne = ligne.rstrip('\n')
    resultat = re_separateurs.search(ligne)
    if resultat:
        #print(ligne)
        print("adresse ip :", resultat.group(1))
        print("requete :", resultat.group(2))
        print("code :", resultat.group(3))
descripteur.close() 
