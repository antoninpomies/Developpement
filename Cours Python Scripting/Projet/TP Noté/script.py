import subprocess
import os

# Informations de connection
ip = input("IP de la Machine : ")
port = input("Port de la Machine : [22]")
cheminFicHost = input("Chemin du fichier sur la machine : ")
cheminFic = input("Répertoire où enregistrer le fichier : ")
id = input("Identifiant de connection : [debian]")
mdp = input("Mot de passe : [debian]")

# Default Values
if port == "":
    port = 22
if id == "":
    id = "debian"
if mdp == "":
    mdp = "debian"

# Lancement de la commande
subprocess.call(["scp", id+"@"+ip+":"+cheminFicHost, cheminFic])