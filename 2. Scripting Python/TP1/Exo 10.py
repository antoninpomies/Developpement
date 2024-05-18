import sys
import re

re_separateurs = re.compile("[ \t]*=[ \t]*")
chemin_fichier = 'config.txt'

try:
    descripteur = open(chemin_fichier, "r") # le petit r correspond au mode lecture
except Exception as e:
    print(e.args)
    sys.exit(1)

dico_config = {}

while 1:
    ligne = descripteur.readline()
    if not ligne:
        break
    ligne = ligne.rstrip('\n')
    eclatement = re_separateurs.split(ligne)
    print(eclatement)
    cle = eclatement[0]
    valeur = eclatement[1]
    dico_config[cle] = valeur
descripteur.close()
print(dico_config)
print(dico_config['nom'], dico_config['adresse_ip'])
