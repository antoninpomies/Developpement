import os,sys
repertoire = sys.argv[1]
text1 = sys.argv[2]
finfichier = sys.argv[3]
repets = sys.argv[4]

if len(sys.argv) < 5:
    print("Please provide all 4 arguments.")
    sys.exit(1)

repets = sys.argv[4] if len(sys.argv) >= 5 else "2"

fichier = open(repertoire, "a")
for i in range(int(repets)):
    fichier.write(text1 + "\n")
fichier.write("\n" + finfichier + "\n")  
fichier.close()


