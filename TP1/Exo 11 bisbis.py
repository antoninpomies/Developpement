import sys
import re

re_adresse_ip = re.compile('^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*\[(.*)\][^"]+"([^"]+)"[^0-9]*([0-9]+)') # ^ permet de sélectionner une expression au début du texte
chemin_fichier = 'access.log'

try:
    descripteur = open(chemin_fichier, "r") # le petit r correspond au mode lecture
except Exception as e:
    print(e.args)
    sys.exit(1)
dico_access = {}
while 1:
    ligne = descripteur.readline()
    if not ligne:
        break
    ligne = ligne.rstrip('\n')
    resultat = re_adresse_ip.search(ligne)
    if resultat:
        adresse_ip = resultat.group(1)
        date = resultat.group(2)
        requete = resultat.group(3)
        erreur = resultat.group(4)
        print('adresse ip:', adresse_ip)
        print('date :', date)
        print('requete :', requete)
        print('erreur :', erreur)
descripteur.close()