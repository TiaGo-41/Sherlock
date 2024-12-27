import os
import json
from PIL import Image
from PIL.ExifTags import TAGS
import folium
import webbrowser
from tkinter import Tk, filedialog, messagebox, Button, Label


# Fonction pour extraire toutes les données EXIF de l'image
def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()

    # Si l'image contient des données EXIF
    if exif_data:
        exif_info = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            exif_info[tag_name] = value
        return exif_info
    return None

# Convertir les coordonnées EXIF en degrés décimaux
def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

# Afficher la carte dans le navigateur à partir des coordonnées GPS
def show_map(latitude, longitude):
    # Créer une carte avec Folium
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=12)
    folium.Marker([latitude, longitude], popup="Coordonnées GPS").add_to(map_obj)
    
    # Sauvegarder la carte dans un fichier HTML
    map_file = "map.html"
    map_obj.save(map_file)
    
    # Ouvrir la carte dans le navigateur
    webbrowser.open(f"file://{os.path.realpath(map_file)}")

# Fonction pour enregistrer les données EXIF dans un fichier JSON
def save_exif_to_json(exif_data, filename="exif_data.json"):
    with open(filename, 'w') as json_file:
        json.dump(exif_data, json_file, indent=4)
    messagebox.showinfo("Succès", f"Les données EXIF ont été sauvegardées dans {filename}")

# Fonction qui s'exécute lorsque l'utilisateur choisit une image
def select_image():
    file_path = filedialog.askopenfilename(title="Choisir une image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if file_path:
        exif_data = get_exif_data(file_path)
        
        if exif_data:
            # Enregistrer les données EXIF dans un fichier JSON
            save_exif_to_json(exif_data)
            
            # Vérifier si les coordonnées GPS existent
            gps_info = exif_data.get("GPSInfo")
            if gps_info:
                latitude = gps_info.get(2)
                longitude = gps_info.get(4)
                if latitude and longitude:
                    lat_ref = gps_info.get(3, '')
                    lon_ref = gps_info.get(1, '')
                    latitude = convert_to_degrees(latitude)
                    longitude = convert_to_degrees(longitude)
                    if lat_ref != 'N':
                        latitude = -latitude
                    if lon_ref != 'E':
                        longitude = -longitude
                    show_map(latitude, longitude)
                else:
                    messagebox.showwarning("GPS", "Les coordonnées GPS ne sont pas disponibles dans cette image.")
            else:
                messagebox.showinfo("Aucune information GPS", "Aucune donnée GPS trouvée dans cette image.")
        else:
            messagebox.showerror("Erreur", "Aucune donnée EXIF trouvée dans cette image.")
    else:
        messagebox.showwarning("Avertissement", "Aucune image sélectionnée.")

# Créer l'interface graphique avec Tkinter
def create_gui():
    root = Tk()
    root.title("Pic2Map - Localiser l'image et enregistrer EXIF")
    
    # Taille de la fenêtre
    root.geometry("400x200")

    # Ajouter un label
    label = Label(root, text="Choisissez une image pour extraire toutes les données EXIF", pady=20)
    label.pack()

    # Ajouter un bouton pour choisir une image
    select_button = Button(root, text="Choisir une image", command=select_image, padx=20, pady=10)
    select_button.pack()

    # Lancer la boucle principale Tkinter
    root.mainloop()

if __name__ == "__main__":
    create_gui()
