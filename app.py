import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

# Fonction pour vérifier les identifiants dans la base de données SQLite
def check_credentials(username, password):
    conn = sqlite3.connect('users.bd')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Fonction qui sera appelée lorsque le bouton "Se connecter" est cliqué
def on_login():
    username = entry_username.get()
    password = entry_password.get()

    # Vérification des identifiants
    if check_credentials(username, password):
        # Si les identifiants sont corrects, afficher un message de succès
        messagebox.showinfo("Connexion réussie", "Bienvenue !")
        
        # Lancer un autre fichier Python (remplacez 'autre_fichier.py' par le fichier que vous voulez exécuter)
        subprocess.run(['python', 'sherlock DEBT.py'])
    else:
        # Si les identifiants sont incorrects, afficher un message d'erreur
        messagebox.showerror("Erreur", "Identifiants incorrects. Essayez à nouveau.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Page de Connexion")

# Créer les labels et les champs de texte
label_username = tk.Label(root, text="Nom d'utilisateur")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Mot de passe")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Créer le bouton de connexion
button_login = tk.Button(root, text="Se connecter", command=on_login)
button_login.pack(pady=20)

# Lancer l'interface graphique
root.mainloop()
