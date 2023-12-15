import argparse                     # Gestion des arguments du script
import re                           # Gestion des expressions régulières du script
import tkinter as tk                # Gestion de l'interface graphique
from tkinter import ttk, filedialog # Gestion de l'interface graphique
import webbrowser                   # Gestion de l'ouverture de l'adresse IP dans le navigateur

def afficherLogs(logs, maxLignes=10): # Fonction pour afficher les logs dans une interface Tkinter

    fenetre = tk.Tk() # Création de la fenêtre principale (Mainloop)
    fenetre.title("Logs Web")

    # Champ de saisie pour le chemin du fichier
    champFichier = tk.Entry(fenetre, width=50)
    champFichier.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='w')

    # Bouton pour changer de fichier
    boutonChangerFichier = tk.Button(fenetre, text="Changer de fichier", command=lambda: chargerFichier(champFichier, vueLogs))
    boutonChangerFichier.grid(row=0, column=2, padx=10, pady=10, sticky='e')

    # Treeview pour afficher les logs
    vueLogs = ttk.Treeview(fenetre, columns=('@IP', 'Horodatage', 'Requete', 'Status', 'Taille', 'Origine de la Requete', 'User Agent', 'Ouverture IP'))
    # Configurer les en-têtes des colonnes
    vueLogs.heading('@IP', text='@IP')
    vueLogs.heading('Horodatage', text='Horodatage')
    vueLogs.heading('Requete', text='Requete')
    vueLogs.heading('Status', text='Status')
    vueLogs.heading('Taille', text='Taille')
    vueLogs.heading('Origine de la Requete', text='Origine de la Requete')
    vueLogs.heading('User Agent', text='User Agent')
    vueLogs.heading('Ouverture IP', text='Ouverture IP')

    # Configurer les colonnes
    vueLogs.column('@IP', anchor=tk.W, width=100)
    vueLogs.column('Horodatage', anchor=tk.W, width=150)
    vueLogs.column('Requete', anchor=tk.W, width=200)
    vueLogs.column('Status', anchor=tk.W, width=50)
    vueLogs.column('Taille', anchor=tk.W, width=80)  # Ajuster la largeur de la colonne 'Taille'
    vueLogs.column('Origine de la Requete', anchor=tk.W, width=150)
    vueLogs.column('User Agent', anchor=tk.W, width=150)
    vueLogs.column('Ouverture IP', anchor=tk.W, width=80)  # Ajuster la largeur de la colonne 'Ouverture IP'

    vueLogs.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    fenetre.grid_columnconfigure(0, weight=1) # S'occupe du changement de taille des onglets

    # Configurer la hauteur du widget Treeview en fonction de la taille de la fenêtre
    hauteurVueLogs = min(len(logs), maxLignes)  # Ajuster le nombre de lignes affichées
    vueLogs.configure(height=hauteurVueLogs)

    # Ajouter les lignes avec la coloration et le bouton 'Ouverture IP'
    for index, log in enumerate(logs[:hauteurVueLogs], 1):
        ip, horodatage, requete, codeStatut, taille, origineRequete, userAgent = log

        # Définir la couleur en fonction du code de statut
        if codeStatut == '200':
            tag = 'vert'
        else:
            tag = 'orange'

        # Ajouter la ligne avec la couleur
        vueLogs.insert('', 'end', values=(ip, horodatage, requete, codeStatut, taille, origineRequete, userAgent, 'Ouverture'), tags=(tag, 'bouton'))

    # Ajout d'un bouton dans la colonne 'Taille' pour trier
    vueLogs.heading('Taille', text='Taille', command=lambda: trierLogsParTaille(vueLogs))

    # Ajouter les tags pour la coloration
    vueLogs.tag_configure('vert', background='green')
    vueLogs.tag_configure('orange', background='orange')

    # Ajouter un événement de clic sur le bouton 'Ouverture IP'
    vueLogs.tag_bind('bouton', '<ButtonRelease-1>', lambda event, vueLogs=vueLogs: ouvrirIp(event, vueLogs))

    # Démarrer la boucle principale Tkinter
    fenetre.mainloop()

# Fonction pour ouvrir le navigateur avec l'adresse IP
def ouvrirIp(event, vueLogs):
    # Récupérer l'élément sur lequel le clic a eu lieu
    item = vueLogs.focus()

    # Vérifier si le clic était sur la colonne 'Ouverture IP'
    if vueLogs.identify_column(event.x) == '#8':  # 'Ouverture IP' est la colonne n°8
        # Récupérer l'adresse IP de la ligne
        ip = vueLogs.item(item, 'values')[0]

        # Ouvrir le navigateur avec l'adresse IP
        webbrowser.open(f'http://{ip}')

# Fonction pour charger un nouveau fichier de logs
def chargerFichier(champ, vueLogs):
    # Boîte de dialogue pour choisir un fichier
    cheminFichier = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    # Effacer le champ de saisie actuel
    champ.delete(0, tk.END)
    # Insérer le chemin du nouveau fichier dans le champ de saisie
    champ.insert(0, cheminFichier)

    # Vérifier si un fichier a été choisi
    if cheminFichier:
        with open(cheminFichier, 'r') as fichier:
            contenu = fichier.read()
            logsGeneriques = re.findall(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"', contenu)

            # Effacer l'affichage actuel
            for enfant in vueLogs.get_children():
                vueLogs.delete(enfant)

            # Ajouter les nouveaux logs avec le bouton 'Ouverture IP'
            for log in logsGeneriques:
                ip, horodatage, requete, codeStatut, taille, origineRequete, userAgent = log
                vueLogs.insert('', 'end', values=(ip, horodatage, requete, codeStatut, taille, origineRequete, userAgent, 'Ouverture'), tags=('vert' if codeStatut == '200' else 'orange', 'bouton'))

# Fonction pour trier les logs par taille
def trierLogsParTaille(vueLogs):
    # Trie des logs par taille de trames
    donnees = [(vueLogs.set(item, 'Taille'), item) for item in vueLogs.get_children('')]
    donnees.sort(key=lambda x: int(x[0]))
    for index, item in enumerate(donnees):
        vueLogs.move(item[1], '', index)

# Initialisation du parser
analyseur = argparse.ArgumentParser()

# Configuration de l'argument f
analyseur.add_argument('-f', '--fichier', help='Chemin du fichier à ouvrir et lire')

# Vérification des arguments
arguments = analyseur.parse_args()

# Vérification si l'argument -f est présent
if arguments.fichier:
    cheminFichierInitial = arguments.fichier
else:
    cheminFichierInitial = ""

# Ouverture du fichier en mode lecture grace au 'r'
with open(cheminFichierInitial, 'r') as fichier:

    contenu = fichier.read()

    # Expression régulière pour l'identification des logs
    motifLogGenerique = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')

    # Recherche des logs d'un fichier grâce a la regex
    logsGeneriques = motifLogGenerique.findall(contenu)

    # Affichage dans la fenetre
    if logsGeneriques:
        afficherLogs(logsGeneriques)
    else:
        print('Aucune trame de logs web trouvée dans le fichier.')
