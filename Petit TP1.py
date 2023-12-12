import os

def lister_repertoire(repertoire):
    print("Contenu du répertoire:")
    elements = os.listdir(repertoire)
    for i, element in enumerate(elements, start=1):
        print(f"{i}. {element}")

# Utilisation du script
repertoire = "/Users/antoninpomies/Documents/Ecole/B3/Developpement/"
lister_repertoire(repertoire)

