import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import datetime

class RenommerPCApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Renommer PC")
        self.geometry("400x300")

        self.label1 = tk.Label(self, text="Sélectionnez le type de PC:")
        self.label1.pack(pady=10)

        self.pc_type_var = tk.StringVar()
        self.pc_type_var.set("Sélectionnez...")
        self.pc_type_combobox = ttk.Combobox(self, textvariable=self.pc_type_var, values=["PC Portable (PORT)", "Unité Centrale (UC)"])
        self.pc_type_combobox.pack(pady=5)

        self.nom_label = tk.Label(self, text="Nom du PC:")
        self.nom_entry = tk.Entry(self)
        self.nom_label.pack(pady=5)
        self.nom_entry.pack(pady=5)

        self.valider_button = tk.Button(self, text="Renommer", command=self.renommer_pc)
        self.valider_button.pack(pady=10)

    def renommer_pc(self):
        nom = self.nom_entry.get().strip()
        pc_type = self.pc_type_var.get()

        if not nom:
            messagebox.showerror("Erreur", "Veuillez entrer un nom pour le PC.")
            return

        if pc_type == "Sélectionnez...":
            messagebox.showerror("Erreur", "Veuillez sélectionner un type de PC.")
            return

        prefixe = "PORT" if pc_type == "PC Portable (PORT)" else "UC"
        date_format = datetime.datetime.now().strftime("%m%y")
        nouveau_nom = f"{prefixe}-{date_format}-{nom}"

        try:
            # Appel de PowerShell avec les privilèges administratifs
            subprocess.run(["powershell.exe", "-Command", f"Rename-Computer -NewName {nouveau_nom} -Force"], shell=True, check=True)
            messagebox.showinfo("Succès", f"Le PC a été renommé en '{nouveau_nom}'")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    app = RenommerPCApp()
    app.mainloop()
