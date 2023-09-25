#!/usr/bin/python3
import sys
import subprocess
# resultat = subprocess.run('ls *.py',shell=True,stdout=subprocess.PIPE)
resultat = subprocess.run('curl ipinfo.io 2> /dev/null',shell=True,stdout=subprocess.PIPE)
liste_fichiers = resultat.stdout.splitlines()
print (liste_fichiers)

