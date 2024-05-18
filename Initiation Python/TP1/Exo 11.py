import sys, os, re

nom_fichier = "bdd.txt"
re_operation = re.compile(r'([:+-])'
                        +r'([0-9]+\.[0-9]+)')
re_affichage = re.compile(r'^-+$')

try:                                #Traitement des Exceptions (Erreur)

    desc = open(nom_fichier, "r")   #Test de l'ouverture et de la disponibilité du fichier

except Exception as e:              #Sinon afficher les erreurs
    print(e.args)
    sys.exit(1)                     #Quitter le Programme

while 1:                            
    ligne = desc.readline()         #Lecture d'une seule ligne
    if not ligne:  
        break
    ligne.rstrip('\n')
    resultat = re_operation.search(ligne)
    if resultat:
        operateur = resultat.group(1)
        somme = resultat.group(2)
        if (operateur == ':'):
            solde = float(somme)
            print('Solde:', solde)
        if (operateur == '+'):
            solde += float(somme)
            print(ligne)
        if (operateur == '-'):
            solde -= float(somme)
            print(ligne)
    resultat = re_affichage.search(ligne)
    if resultat:
        print('=', solde)
desc.close()



