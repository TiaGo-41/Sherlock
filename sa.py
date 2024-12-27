#import sqlite3

# Connexion à la base de données SQLite (si elle n'existe pas, elle sera créée)
conn = sqlite3.connect('users.bd')
cursor = conn.cursor()

# Création de la table 'users' (si elle n'existe pas)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Ajout d'un utilisateur (vous pouvez modifier ces valeurs)
cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
''', ('admin', 'password123'))  # Utilisateur "admin" avec mot de passe "password123"

# Sauvegarder les changements et fermer la connexion
conn.commit()
conn.close()
