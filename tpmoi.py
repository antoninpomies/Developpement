#Commande : python3 "/Users/antoninpomies/Documents/Ecole/B3/Developpement/monFichier" "hello guys" "c'est la fin" "3"

import os, sys

repertoire = sys.argv[1]
text1 = sys.argv[2]
finfichier = sys.argv[3]
repets = sys.argv[4]

listedesreps = os.listdir(repertoire)

for i, element in enumerate(listedesreps):
        print(f"{i}. {element}")




