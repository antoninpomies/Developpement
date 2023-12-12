import sys
repertoire, text1, finfichier, repets = sys.argv[1:5]
with open(repertoire, "a") as fichier:
    fichier.write((text1 + "\n") * int(repets) + "\n" + finfichier + "\n")
import sys