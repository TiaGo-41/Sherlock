import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

# Initialisation de la base de données
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

# Création de la table si elle n'existe pas
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
""")
conn.commit()

# Fonctions pour le bloc-notes
def load_notes():
    cursor.execute("SELECT id, title FROM notes")
    notes = cursor.fetchall()
    notes_listbox.delete(0, tk.END)
    for note in notes:
        notes_listbox.insert(tk.END, f"{note[0]}: {note[1]}")

def save_note():
    title = title_entry.get()
    content = text_area.get("1.0", tk.END).strip()
    if title and content:
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        load_notes()
        messagebox.showinfo("Succès", "La note a été sauvegardée.")
    else:
        messagebox.showwarning("Erreur", "Le titre et le contenu sont obligatoires.")

def view_note():
    try:
        selected_item = notes_listbox.get(notes_listbox.curselection())
        note_id = int(selected_item.split(":")[0])
        cursor.execute("SELECT title, content FROM notes WHERE id = ?", (note_id,))
        note = cursor.fetchone()
        title_entry.delete(0, tk.END)
        title_entry.insert(0, note[0])
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", note[1])
    except Exception as e:
        messagebox.showerror("Erreur", "Veuillez sélectionner une note valide.")

def delete_note():
    try:
        selected_item = notes_listbox.get(notes_listbox.curselection())
        note_id = int(selected_item.split(":")[0])
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        load_notes()
        title_entry.delete(0, tk.END)
        text_area.delete("1.0", tk.END)
        messagebox.showinfo("Succès", "La note a été supprimée.")
    except Exception as e:
        messagebox.showerror("Erreur", "Veuillez sélectionner une note valide.")

# Interface utilisateur
root = tk.Tk()
root.title("Bloc-notes")

frame = tk.Frame(root)
frame.pack(pady=10)

title_label = tk.Label(frame, text="Titre :")
title_label.grid(row=0, column=0, padx=5, pady=5)

title_entry = tk.Entry(frame, width=40)
title_entry.grid(row=0, column=1, padx=5, pady=5)

text_area = tk.Text(frame, width=50, height=20)
text_area.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

buttons_frame = tk.Frame(frame)
buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

save_button = tk.Button(buttons_frame, text="Sauvegarder", command=save_note)
save_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(buttons_frame, text="Voir", command=view_note)
view_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(buttons_frame, text="Supprimer", command=delete_note)
delete_button.grid(row=0, column=2, padx=5)

notes_listbox = tk.Listbox(root, width=50, height=15)
notes_listbox.pack(pady=10)

load_notes()

root.mainloop()

# Ferme la connexion à la base de données
conn.close()
