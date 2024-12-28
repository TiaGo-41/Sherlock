import tkinter as tk
from tkinter import messagebox
import whois
import shodan
import folium
import piexif
from tkinter import filedialog
import webbrowser
import os

# Fonction pour effectuer une recherche WHOIS
def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return str(domain_info)
    except Exception as e:
        return f"Error: {e}"

# Fonction pour effectuer une recherche Shodan
def shodan_lookup(api_key, ip):
    api = shodan.Shodan(api_key)
    try:
        result = api.host(ip)
        return str(result)
    except shodan.APIError as e:
        return f"Error: {e}"

# Fonction pour extraire les coordonnées GPS des métadonnées EXIF de l'image
def get_image_coordinates(image_path):
    try:
        exif_dict = piexif.load(image_path)
        gps_data = exif_dict.get("GPS", None)
        
        if not gps_data:
            return None, "No GPS info found in EXIF data."

        # Extraire la latitude et longitude
        lat_degree = gps_data.get(piexif.GPSIFD.GPSLatitude)
        lat_ref = gps_data.get(piexif.GPSIFD.GPSLatitudeRef)
        lon_degree = gps_data.get(piexif.GPSIFD.GPSLongitude)
        lon_ref = gps_data.get(piexif.GPSIFD.GPSLongitudeRef)

        if lat_degree and lon_degree:
            # Convertir les valeurs en degrés décimaux
            lat = lat_degree[0][0] / lat_degree[0][1] + lat_degree[1][0] / (lat_degree[1][1] * 60) + lat_degree[2][0] / (lat_degree[2][1] * 3600)
            lon = lon_degree[0][0] / lon_degree[0][1] + lon_degree[1][0] / (lon_degree[1][1] * 60) + lon_degree[2][0] / (lon_degree[2][1] * 3600)

            # Appliquer la direction (N/S pour latitude, E/W pour longitude)
            if lat_ref == 'S':
                lat = -lat
            if lon_ref == 'W':
                lon = -lon

            return (lat, lon), None
        else:
            return None, "GPS coordinates not found."
    except Exception as e:
        return None, str(e)

# Fonction pour afficher la carte avec Folium
def show_map(lat, lon):
    # Créer une carte centrée sur les coordonnées GPS
    map_ = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon]).add_to(map_)
    
    # Sauvegarder la carte dans un fichier HTML
    map_file = "map.html"
    map_.save(map_file)
    
    # Ouvrir le fichier HTML dans le navigateur par défaut
    webbrowser.open(f'file://{os.path.realpath(map_file)}')

# Fonction pour traiter la recherche WHOIS
def on_whois_search():
    domain = entry_whois_domain.get()
    if domain:
        result = whois_lookup(domain)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Input Error", "Please enter a domain to search.")

# Fonction pour traiter la recherche Shodan
def on_shodan_search():
    api_key = entry_shodan_api.get()
    ip = entry_shodan_ip.get()
    if api_key and ip:
        result = shodan_lookup(api_key, ip)
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, result)
    else:
        messagebox.showwarning("Input Error", "Please enter both Shodan API key and IP address.")

# Fonction pour traiter l'extraction des coordonnées GPS et l'affichage sur une carte
def on_metadata_search():
    image_path = entry_image_path.get()
    if image_path:
        coordinates, error = get_image_coordinates(image_path)
        if coordinates:
            text_result.delete(1.0, tk.END)
            text_result.insert(tk.END, f"Coordinates: {coordinates[0]}, {coordinates[1]}")
            show_map(coordinates[0], coordinates[1])
        else:
            messagebox.showwarning("Error", error)
    else:
        messagebox.showwarning("Input Error", "Please enter the image file path.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("OSINT Forensic Tool")
root.geometry("600x600")

# Titre
label_title = tk.Label(root, text="OSINT Forensic Tool", font=("Arial", 16))
label_title.pack(pady=10)

# Rechercher WHOIS
frame_whois = tk.Frame(root)
frame_whois.pack(pady=10)

label_whois = tk.Label(frame_whois, text="Enter domain for WHOIS lookup:")
label_whois.grid(row=0, column=0, padx=5)

entry_whois_domain = tk.Entry(frame_whois, width=40)
entry_whois_domain.grid(row=0, column=1, padx=5)

button_whois = tk.Button(frame_whois, text="Search WHOIS", command=on_whois_search)
button_whois.grid(row=0, column=2, padx=5)

# Rechercher Shodan
frame_shodan = tk.Frame(root)
frame_shodan.pack(pady=10)

label_shodan_api = tk.Label(frame_shodan, text="Enter Shodan API key:")
label_shodan_api.grid(row=0, column=0, padx=5)

entry_shodan_api = tk.Entry(frame_shodan, width=40)
entry_shodan_api.grid(row=0, column=1, padx=5)

label_shodan_ip = tk.Label(frame_shodan, text="Enter IP address for Shodan lookup:")
label_shodan_ip.grid(row=1, column=0, padx=5)

entry_shodan_ip = tk.Entry(frame_shodan, width=40)
entry_shodan_ip.grid(row=1, column=1, padx=5)

button_shodan = tk.Button(frame_shodan, text="Search Shodan", command=on_shodan_search)
button_shodan.grid(row=2, column=1, pady=5)

# Rechercher les métadonnées de l'image
frame_image = tk.Frame(root)
frame_image.pack(pady=10)

label_image = tk.Label(frame_image, text="Enter image path for metadata extraction:")
label_image.grid(row=0, column=0, padx=5)

entry_image_path = tk.Entry(frame_image, width=40)
entry_image_path.grid(row=0, column=1, padx=5)

button_image = tk.Button(frame_image, text="Extract Metadata", command=on_metadata_search)
button_image.grid(row=0, column=2, padx=5)

# Zone pour afficher les résultats
label_result = tk.Label(root, text="Results:")
label_result.pack(pady=10)

text_result = tk.Text(root, height=15, width=70)
text_result.pack(pady=10)

# Lancer l'interface
root.mainloop()
