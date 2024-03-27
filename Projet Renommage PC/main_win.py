import tkinter as tk
from tkinter import messagebox
import subprocess
import datetime

class RenommerPCApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Renommer PC")
        self.geometry("400x300")

        self.label1 = tk.Label(self, text="Sélectionnez les informations:")
        self.label1.pack(pady=10)

        self.portable_var = tk.BooleanVar()
        self.uc_var = tk.BooleanVar()
        self.nom_entry = tk.Entry(self)
        self.portable_checkbox = tk.Checkbutton(self, text="PC Portable (PORT)", variable=self.portable_var)
        self.uc_checkbox = tk.Checkbutton(self, text="Unité Centrale (UC)", variable=self.uc_var)
        self.nom_label = tk.Label(self, text="Nom du PC:")
        self.valider_button = tk.Button(self, text="Renommer", command=self.renommer_pc)

        self.nom_entry.pack(pady=5)
        self.portable_checkbox.pack()
        self.uc_checkbox.pack()
        self.nom_label.pack(pady=5)
        self.valider_button.pack(pady=10)

    def renommer_pc(self):
        nom = self.nom_entry.get().strip()
        if not nom:
            messagebox.showerror("Erreur", "Veuillez entrer un nom pour le PC.")
            return

        if not (self.portable_var.get() or self.uc_var.get()):
            messagebox.showerror("Erreur", "Veuillez sélectionner au moins un type de PC.")
            return

        prefixe = "PORT" if self.portable_var.get() else "UC"
        date_format = datetime.datetime.now().strftime("%m%y")
        nouveau_nom = f"{prefixe}{date_format}{nom}"

        try:
            # Appel de PowerShell avec les privilèges administratifs
            subprocess.run(["powershell.exe", "-Command", f"Rename-Computer -NewName {nouveau_nom} -Force"], shell=True, check=True)
            messagebox.showinfo("Succès", f"Le PC a été renommé en '{nouveau_nom}'")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    app = RenommerPCApp()
    app.mainloop()
