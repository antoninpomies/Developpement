import argparse                     # Gestion des arguments du script
import re                           # Gestion des expressions régulières du script
import tkinter as tk                # Gestion de l'interface graphique
from tkinter import ttk, filedialog # Gestion de l'interface graphique
import webbrowser                   # Gestion de l'ouverture de l'adresse IP dans le navigateur

def affichageLogs(logs, max_rows=10): # Fonction d'affichage des logs
    window = tk.Tk()
    window.title("Logs Web")

    file_entry = tk.Entry(window, width=50) # Champ de saisie pour le chemin du fichier
    file_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='w')

    change_file_button = tk.Button(window, text="Changer de fichier", command=lambda: load_file(file_entry, tree)) # Bouton pour changer de fichier
    change_file_button.grid(row=0, column=2, padx=10, pady=10, sticky='e')

    tree = ttk.Treeview(window, columns=('IP', 'Timestamp', 'Request', 'Status', 'Size', 'Referrer', 'User Agent', 'Open IP')) # Affichage des logs dans une vue treeview
    tree.heading('IP', text='IP')
    tree.heading('Timestamp', text='Timestamp')
    tree.heading('Request', text='Request')
    tree.heading('Status', text='Status')
    tree.heading('Size', text='Size')
    tree.heading('Referrer', text='Referer')
    tree.heading('User Agent', text='User Agent')
    tree.heading('Open IP', text='Open IP')

    tree.column('IP', anchor=tk.W, width=100)
    tree.column('Timestamp', anchor=tk.W, width=150)
    tree.column('Request', anchor=tk.W, width=200)
    tree.column('Status', anchor=tk.W, width=50)
    tree.column('Size', anchor=tk.W, width=80)  
    tree.column('Referrer', anchor=tk.W, width=150)
    tree.column('User Agent', anchor=tk.W, width=150)
    tree.column('Open IP', anchor=tk.W, width=80)  

    tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    window.grid_columnconfigure(0, weight=1) # Configurer le redimensionnement des colonnes avec la fenêtre

    tree_height = min(len(logs), max_rows)  # Ajuster le nombre de lignes affichées
    tree.configure(height=tree_height)

    for index, log in enumerate(logs[:tree_height], 1): # Ajouter les lignes avec la coloration et le bouton 'Open IP'
        ip, timestamp, request, status_code, size, referrer, user_agent = log

        
        if status_code == '200': # Définir la couleur en fonction du code de la requete
            tag = 'green'
        else:
            tag = 'orange'

        tree.insert('', 'end', values=(ip, timestamp, request, status_code, size, referrer, user_agent, 'Open'), tags=(tag, 'button')) # Ajouter la ligne avec la couleur

    tree.heading('Size', text='Size', command=lambda: sort_logs_by_size(tree)) # Bouton de tri par taille

    tree.tag_configure('green', background='green') # Configurer les tags pour la couleur
    tree.tag_configure('orange', background='orange')

    tree.tag_bind('button', '<ButtonRelease-1>', lambda event, tree=tree: OuvertureIP(event, tree)) # Ajout d'un bontoon pour ouvrir l'IP

    window.mainloop()

def OuvertureIP(event, tree): # Fonction d'ouverture de l'IP dans un naviguateur
    # Récupérer l'élément sur lequel le clic a eu lieu
    item = tree.focus()

    # Vérifier si le clic était sur la colonne 'Open IP'
    if tree.identify_column(event.x) == '#8':  # 'Open IP' est la colonne n°8
        # Récupérer l'adresse IP de la ligne
        ip = tree.item(item, 'values')[0]

        # Ouvrir le navigateur avec l'adresse IP
        webbrowser.open(f'http://{ip}')

def load_file(entry, tree):
    file_path = filedialog.askopenfilename(title="Sélectionner un fichier", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            generic_logs = re.findall(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"', content)

            # Effacer l'affichage actuel
            for child in tree.get_children():
                tree.delete(child)

            # Ajouter les nouveaux logs avec le bouton 'Open IP'
            for log in generic_logs:
                ip, timestamp, request, status_code, size, referrer, user_agent = log
                tree.insert('', 'end', values=(ip, timestamp, request, status_code, size, referrer, user_agent, 'Open'), tags=('green' if status_code == '200' else 'orange', 'button'))

def sort_logs_by_size(tree):
    # Trie les logs par taille (la colonne 'Size')
    data = [(tree.set(item, 'Size'), item) for item in tree.get_children('')]
    data.sort(key=lambda x: int(x[0]))
    for index, item in enumerate(data):
        tree.move(item[1], '', index)

# Création de l'objet ArgumentParser
parser = argparse.ArgumentParser()

# Ajout de l'argument -f pour spécifier le chemin du fichier
parser.add_argument('-f', '--file', help='Chemin du fichier à ouvrir et lire')

# Parsing des arguments de la ligne de commande
args = parser.parse_args()

# Vérification si l'argument -f est présent
if args.file:
    initial_file_path = args.file
else:
    initial_file_path = ""

# Ouverture du fichier en mode lecture
with open(initial_file_path, 'r') as file:
    # Lecture du contenu du fichier
    content = file.read()

    # Expression régulière pour rechercher des parties génériques d'une trame de log
    generic_log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')

    # Recherche des parties génériques des trames de logs web dans le contenu du fichier
    generic_logs = generic_log_pattern.findall(content)

    # Affichage des parties génériques des trames de logs web dans une fenêtre Tkinter
    if generic_logs:
        affichageLogs(generic_logs)
    else:
        print('Aucune trame de logs web trouvée dans le fichier.')
