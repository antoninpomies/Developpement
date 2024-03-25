import subprocess
import tkinter as tk
from tkinter import messagebox

def rename_pc():
    # Récupération des valeurs des champs
    prefix = prefix_var.get()
    year_month = year_month_var.get()
    name = name_entry.get()

    # Construction du nouveau nom
    new_name = f"{prefix}{year_month}-{name[:7]}".upper()

    # Vérification de la longueur du nom final
    if len(new_name) > 15:
        messagebox.showerror("Erreur", "Le nom final dépasse 15 caractères. Veuillez raccourcir le nom de la personne.")
        return

    # Renommage du PC
    try:
        subprocess.run(["sudo", "scutil", "--set", "ComputerName", new_name])
        subprocess.run(["sudo", "scutil", "--set", "LocalHostName", new_name])
        subprocess.run(["sudo", "scutil", "--set", "HostName", new_name])
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

# Année et mois
year_month_label = tk.Label(input_frame, text="Année-Mois (AAMM):")
year_month_label.grid(row=1, column=0)

year_month_var = tk.StringVar()
year_month_entry = tk.Entry(input_frame, textvariable=year_month_var)
year_month_entry.grid(row=1, column=1)

# Nom de la personne
name_label = tk.Label(input_frame, text="Nom de la personne:")
name_label.grid(row=2, column=0)

name_entry = tk.Entry(input_frame)
name_entry.grid(row=2, column=1)

# Bouton de renommage
rename_button = tk.Button(root, text="Renommer PC", command=rename_pc)
rename_button.pack()

root.mainloop()
