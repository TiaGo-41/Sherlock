import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os

def load_file():
    filepath = "doc\doc.txt"
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                text_area.delete("1.0", tk.END)  # Efface le contenu actuel de la zone de texte
                text_area.insert(tk.END, content)  # Insère le contenu du fichier
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de lire le fichier:\n{e}")
    else:
        messagebox.showwarning("Fichier introuvable", f"Le fichier {filepath} n'existe pas.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Info-Aide")
root.geometry("600x400")

# Créer une zone de texte avec barre de défilement
text_area = ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Créer un bouton pour charger le fichier
load_button = tk.Button(root, text="Charger le fichier", command=load_file)
load_button.pack(pady=10)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
