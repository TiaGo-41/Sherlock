import tkinter as tk
from tkinter import messagebox
import requests

# Fonction pour récupérer les informations du véhicule
def get_vehicle_info():
    plate_number = plate_entry.get()
    if not plate_number:
        messagebox.showerror("Erreur", "Veuillez entrer une plaque d'immatriculation.")
        return

    # API fictive (remplacez par une vraie API autorisée)
    api_url = "https://api-exemple.com/vehicle-info"
    api_key = "votre_api_key"  # Remplacez par votre clé API si nécessaire

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    params = {"plate": plate_number}

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            messagebox.showerror("Erreur", f"Erreur : {data['error']}")
        else:
            result_text.set(f"Marque : {data['brand']}\n"
                            f"Modèle : {data['model']}\n"
                            f"Année : {data['year']}\n"
                            f"Propriétaire : {data.get('owner', 'Non disponible')}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Erreur", f"Erreur lors de la requête : {e}")

# Création de l'interface graphique
root = tk.Tk()
root.title("Informations sur le véhicule")

# Widgets de l'interface
tk.Label(root, text="Entrez la plaque d'immatriculation :").grid(row=0, column=0, padx=10, pady=10)
plate_entry = tk.Entry(root)
plate_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Rechercher", command=get_vehicle_info).grid(row=1, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", anchor="w")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Lancement de l'application
root.mainloop()
