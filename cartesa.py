import folium
import tkinter as tk
import webbrowser
import tempfile

def generate_map():
    # Créer la carte centrée sur Paris
    latitude = 48.8566
    longitude = 2.3522
    m = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Ajouter un marqueur à Paris
    folium.Marker([latitude, longitude], popup="Paris").add_to(m)

    # Utiliser un fichier temporaire pour stocker la carte
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
    m.save(temp_file.name)
    
    return temp_file.name

def open_map():
    # Générer la carte et obtenir son chemin temporaire
    map_file = generate_map()

    # Ouvrir la carte dans le navigateur par défaut
    webbrowser.open(f"file://{map_file}")

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Carte OpenStreetMap")

# Ajouter un bouton pour ouvrir la carte OSM dans le navigateur
open_button = tk.Button(root, text="Ouvrir la carte OSM", command=open_map)
open_button.pack(pady=20)

# Lancer la fenêtre Tkinter
root.mainloop()
