import sys, subprocess
resultat = subprocess.run('ls *.py 2> /dev/null',shell=True,stdout=subprocess.PIPE)
#resultat = subprocess.run('curl ipinfo.io 2> /dev/null',shell=True,stdout=subprocess.PIPE)
liste_fichiers = resultat.stdout.splitlines()

#print(liste_fichiers)

for i in liste_fichiers:
    try:
        desc = open(i,'r')
    except Exception as e:
        print(e.args)
    ligne = desc.readline()
    print(ligne)
    desc.close()