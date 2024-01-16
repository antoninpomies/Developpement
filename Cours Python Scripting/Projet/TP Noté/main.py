import paramiko

ip = input("IP de la Machine : ")
po = input("Port de la Machine : [22]")
id = input("Identifiant de connection : [debian]")
mdp = input("Mot de passe : [debian]")
cheminFicHost = input("Chemin du fichier sur la machine : [/home/debian/fic.txt]")
cheminFic = input("Répertoire où enregistrer le fichier : [Sur le Bureau]")

# Valeurs par défaut
if po == "":
    po = 22
if id == "":
    id = "debian"
if mdp == "":
    mdp = "debian"
if cheminFicHost == "":
    cheminFicHost = "/home/debian/fic.txt"
if cheminFic == "": 
    cheminFic = "/Users/antoninpomies/Desktop/fic.txt"

try:
    # Connexion SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Coonexion avec MDP
    ssh.connect(ip, username=id, password=mdp, port=po)

    # Traitement du module SCP
    scp = ssh.open_sftp()
    scp.get(cheminFicHost, cheminFic)

    # Fermeture des connexions
    scp.close()
    ssh.close()
except Exception as e:
    print(e)
    print("Erreur de connexion")