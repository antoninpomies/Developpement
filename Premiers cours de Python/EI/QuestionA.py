import sys, re

nomFichier = "arp-scan-output.txt"
nomFichier2 = "oui.txt"
reOui = re.compile(r'([\w]+\:[\w]+\:[\w]+)')


try:

    descArp = open(nomFichier, "r")
    descOui = open(nomFichier2, "r")

except Exception as e:
    print(e.args)
    sys.exit(0)

while 1:
    ligneArp = descArp.readline()
    
    if not ligneArp:
        break
    
    ouiMac = reOui.search(ligneArp)
    oui = ouiMac.group(1)
    print(oui)

#Je n'ai pas eu le temps de finir mais je devais dupliquer le code pour 
# lire le second fichier et grâce a un if comparer les résultat et afficher 
# le résultat sous le bon format
descArp.close()
descOui.close()






    

