#programme permettant de lire le scan arp et de le faire corresponde a un fichier OUI

#import des bibliothèques
import sys, re

#déclaration des variables
scan_arp = r"arp-scan_output.txt"
oui = r"oui.txt"
re_addr = re.compile("([0-9]+.[0-9]+.[0-9]+.[0-9]+)[^0-9A-F]+([0-9A-F]+:[0-9A-F]+:[0-9A-F]+)")
re_oui = re.compile("([0-9A-F]+:[0-9A-F]+:[0-9A-F]+)[^0-9a-zA-Z]+(.*)")
mac_arp = ""
mac_oui = ""

#ouverture du fichier scan-arp avec arrêt du programme en cas d'erreur
try :
    f_scan_arp = open(scan_arp, "r")
except Exception as e :
    print(e.args)
    sys.exit(1)

#boucle infinie de parcours de du fichier scan-arp
while 1 :
    ligne_arp = f_scan_arp.readline()
    #sortie de boucle si la ligne n'existe pas
    if not ligne_arp :
        break
    ligne_arp = ligne_arp.rstrip('\n')
    #recherche des champs IP et addresse MAC a l'aide d'une expression régulière
    mac_arp = re_addr.search(ligne_arp)
    #ouverture du fichier oui.txt pour mettre en correspondance les adresse MAC du scan-arp, avec arrêt du programme en cas d'erreur d'ouverture
    try:
        f_oui = open(oui, 'r')
    except Exception as e :
        print(e.args)
        sys.exit(1)
    #boucle infinie de parcours du fichier oui.txt
    while 1 :
        ligne_oui = f_oui.readline()
        #sortie de boucle si la ligne n'existe pas
        if not ligne_oui :
            f_oui.close()
            break
        ligne_oui = ligne_oui.rstrip('\n')
        #recherche des champs addresse MAC et nom de constructeur a l'aide d'une expression régulière
        mac_oui = re_oui.search(ligne_oui)
        #recherche de correspondance entre l'addresse MAC du scan-arp et de l'adresse MAC du constructeur
        if mac_oui.group(1) == mac_arp.group(2) :
            print(mac_arp.group(1), '\t', mac_arp.group(2), '\t', mac_oui.group(2))
            f_oui.close()
            break

#fermeture des fichiers
f_scan_arp.close()

