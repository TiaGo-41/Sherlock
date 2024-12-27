import tkinter as tk
from tkinter import ttk  # Importation correcte de ttk
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3

# Fonction pour récupérer tous les utilisateurs de la base de données
def get_users():
    conn = sqlite3.connect('users.bd')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

# Fonction pour ajouter un utilisateur
def add_user(username, password):
    conn = sqlite3.connect('users.bd')
    cursor = conn.cursor()
    
    # Vérifier si l'utilisateur existe déjà
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        conn.close()
        return False  # L'utilisateur existe déjà
    
    # Ajouter un nouvel utilisateur
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return True  # Utilisateur ajouté avec succès

# Fonction pour supprimer un utilisateur
def delete_user(username):
    conn = sqlite3.connect('users.bd')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

# Fonction pour modifier le mot de passe ou l'identifiant
def modify_user(old_username, new_username, new_password):
    conn = sqlite3.connect('users.bd')
    cursor = conn.cursor()
    
    # Vérifier si le nouveau nom d'utilisateur existe déjà
    cursor.execute('SELECT * FROM users WHERE username = ?', (new_username,))
    if cursor.fetchone() and old_username != new_username:
        conn.close()
        return False  # Le nouveau nom d'utilisateur existe déjà
    
    # Mettre à jour l'utilisateur
    cursor.execute('UPDATE users SET username = ?, password = ? WHERE username = ?', (new_username, new_password, old_username))
    conn.commit()
    conn.close()
    return True  # Utilisateur modifié avec succès

# Fonction pour mettre à jour le tableau des utilisateurs affiché
def update_user_table():
    # Vider le tableau existant
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Récupérer les utilisateurs depuis la base de données
    users = get_users()
    
    # Insérer chaque utilisateur dans le tableau
    for user in users:
        treeview.insert("", "end", values=(user[1], user[2]))  # user[1] -> username, user[2] -> password

# Fonction pour ajouter un utilisateur via un formulaire
def on_add_user():
    username = simpledialog.askstring("Nom d'utilisateur", "Entrez le nom d'utilisateur:")
    password = simpledialog.askstring("Mot de passe", "Entrez le mot de passe:", show="*")
    
    if username and password:
        if add_user(username, password):
            messagebox.showinfo("Succès", "Utilisateur ajouté avec succès.")
            update_user_table()  # Mettre à jour le tableau après ajout
        else:
            messagebox.showerror("Erreur", "Un utilisateur avec ce nom existe déjà.")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

# Fonction pour supprimer un utilisateur
def on_delete_user():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Aucun utilisateur sélectionné", "Veuillez sélectionner un utilisateur à supprimer.")
        return
    
    username = treeview.item(selected_item)['values'][0]
    confirm = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer l'utilisateur '{username}' ?")
    
    if confirm:
        delete_user(username)
        messagebox.showinfo("Succès", "Utilisateur supprimé avec succès.")
        update_user_table()  # Mettre à jour le tableau après suppression

# Fonction pour modifier un utilisateur
def on_modify_user():
    selected_item = treeview.selection()
    if not selected_item:
        messagebox.showwarning("Aucun utilisateur sélectionné", "Veuillez sélectionner un utilisateur à modifier.")
        return
    
    old_username = treeview.item(selected_item)['values'][0]
    new_username = simpledialog.askstring("Nom d'utilisateur", f"Entrez le nouveau nom d'utilisateur pour '{old_username}':")
    new_password = simpledialog.askstring("Mot de passe", f"Entrez le nouveau mot de passe pour '{old_username}':", show="*")
    
    if new_username and new_password:
        if modify_user(old_username, new_username, new_password):
            messagebox.showinfo("Succès", "Utilisateur modifié avec succès.")
            update_user_table()  # Mettre à jour le tableau après modification
        else:
            messagebox.showerror("Erreur", "Un utilisateur avec ce nouveau nom existe déjà.")
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de comptes")

# Créer un tableau pour afficher les utilisateurs (affiche Nom d'utilisateur + Mot de passe)
columns = ("Username", "Password")
treeview = ttk.Treeview(root, columns=columns, show="headings")
treeview.heading("Username", text="Nom d'utilisateur")
treeview.heading("Password", text="Mot de passe")
treeview.pack(pady=20)

# Ajouter les boutons pour gérer les utilisateurs
button_add = tk.Button(root, text="Ajouter un utilisateur", command=on_add_user)
button_add.pack(side="left", padx=10)

button_delete = tk.Button(root, text="Supprimer l'utilisateur", command=on_delete_user)
button_delete.pack(side="left", padx=10)

button_modify = tk.Button(root, text="Modifier l'utilisateur", command=on_modify_user)
button_modify.pack(side="left", padx=10)

# Charger les utilisateurs au démarrage
update_user_table()

# Lancer l'interface graphique
root.mainloop()
