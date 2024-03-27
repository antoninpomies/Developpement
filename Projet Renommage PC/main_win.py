import ctypes
import os
import tkinter as tk
import sys
from tkinter import messagebox
from datetime import datetime

def rename_pc():
    # Récupération des valeurs des champs
    prefix = prefix_var.get()
    # Obtention de la date actuelle au format YYMM
    year_month = datetime.now().strftime('%y%m')
    name = name_entry.get()

    # Construction du nouveau nom
    new_name = f"{prefix}{year_month}-{name[:7]}".upper()

    # Vérification de la longueur du nom final
    if len(new_name) > 15:
        messagebox.showerror("Erreur", "Le nom final dépasse 15 caractères. Veuillez raccourcir le nom de la personne.")
        return

    # Demande des droits administrateur
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de demander les droits d'administrateur : {e}")
        return

    # Renommage du PC
    try:
        os.system(f"wmic computersystem where caption='%computername%' rename {new_name}")
        messagebox.showinfo("Succès", f"Le PC a été renommé en {new_name}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du renommage du PC : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Renommage de PC")

# Frame pour les champs de saisie
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Choix du préfixe
prefix_label = tk.Label(input_frame, text="Préfixe:")
prefix_label.grid(row=0, column=0)

prefix_var = tk.StringVar(value="POR")
prefix_option = tk.OptionMenu(input_frame, prefix_var, "POR", "UC")
prefix_option.grid(row=0, column=1)

# Nom de la personne
name_label = tk.Label(input_frame, text="Nom de la personne:")
name_label.grid(row=1, column=0)

name_entry = tk.Entry(input_frame)
name_entry.grid(row=1, column=1)

# Bouton de renommage
rename_button = tk.Button(root, text="Renommer PC", command=rename_pc)
rename_button.pack()

root.mainloop()
