import sys, subprocess
resultat = subprocess.run('ls -F',shell=True,stdout=subprocess.PIPE)
liste_fichiers = resultat.stdout.splitlines()
#print (liste_fichiers)

liste_rep = []
liste_exe = []
liste_fic = []

for i in liste_fichiers:
    nomfichier = i.decode('utf-8')
    if nomfichier[-1] == '/':
        liste_rep.append(i)
    elif nomfichier[-1] == '*':
        liste_exe.append(i)
    else:
        liste_fic.append(i)

print("Liste Répertoires : \n", liste_rep)
print("Liste Executables : \n", liste_exe)
print("Liste Fichiers : \n", liste_fic)

