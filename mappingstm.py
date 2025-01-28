import networkx as nx
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class GraphCommonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Commons Clone")
        self.graph = nx.Graph()
        self.recent_file = None
        self.selected_node = None
        self.node_colors = {}
        self.edge_colors = {}

        self.create_menu()
        self.create_interface()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Nouveau", command=self.new_graph)
        file_menu.add_command(label="Ouvrir", command=self.load_graph)
        file_menu.add_command(label="Sauvegarder", command=self.save_graph)
        file_menu.add_command(label="Sauvegarder sous", command=self.save_graph_as)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)

        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        self.file_menu = file_menu

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Supprimer nœud/arête", command=self.delete_element)

        menu_bar.add_cascade(label="Éditer", menu=edit_menu)
        self.root.config(menu=menu_bar)

    def create_interface(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        left_frame = tk.Frame(main_frame, bg="#f8f9fa")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(left_frame, text="Gestion du graphe", font=("Arial", 14), bg="#f8f9fa").pack(pady=5)

        node_frame = tk.Frame(left_frame, bg="#f8f9fa")
        node_frame.pack(pady=10)

        tk.Label(node_frame, text="ID du nœud", bg="#f8f9fa").grid(row=0, column=0)
        self.node_id_entry = tk.Entry(node_frame)
        self.node_id_entry.grid(row=0, column=1)

        tk.Label(node_frame, text="Étiquette du nœud", bg="#f8f9fa").grid(row=1, column=0)
        self.node_label_entry = tk.Entry(node_frame)
        self.node_label_entry.grid(row=1, column=1)

        tk.Button(node_frame, text="Ajouter un nœud", command=self.add_node).grid(row=2, columnspan=2, pady=5)

        edge_frame = tk.Frame(left_frame, bg="#f8f9fa")
        edge_frame.pack(pady=10)

        tk.Label(edge_frame, text="Source", bg="#f8f9fa").grid(row=0, column=0)
        self.edge_source_entry = tk.Entry(edge_frame)
        self.edge_source_entry.grid(row=0, column=1)

        tk.Label(edge_frame, text="Cible", bg="#f8f9fa").grid(row=1, column=0)
        self.edge_target_entry = tk.Entry(edge_frame)
        self.edge_target_entry.grid(row=1, column=1)

        tk.Button(edge_frame, text="Ajouter une arête", command=self.add_edge).grid(row=2, columnspan=2, pady=5)

        color_frame = tk.Frame(left_frame, bg="#f8f9fa")
        color_frame.pack(pady=10)

        tk.Button(color_frame, text="Changer couleur nœud", command=self.change_node_color).pack(pady=5)
        tk.Button(color_frame, text="Changer couleur arête", command=self.change_edge_color).pack(pady=5)

        tk.Button(left_frame, text="Mettre à jour l'affichage", command=self.update_canvas).pack(pady=10)

        self.canvas_frame = tk.Frame(main_frame, bg="#ffffff")
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.mpl_connect("button_press_event", self.on_canvas_click)
        self.update_canvas()

    def new_graph(self):
        self.graph = nx.Graph()
        self.node_colors = {}
        self.edge_colors = {}
        self.recent_file = None
        self.root.title("Graph Commons Clone - Nouveau")
        self.update_canvas()

    def save_graph(self):
        if self.recent_file:
            self.save_graph_to_file(self.recent_file)
        else:
            self.save_graph_as()

    def save_graph_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Fichiers JSON", "*.json")])
        if file_path:
            self.save_graph_to_file(file_path)

    def save_graph_to_file(self, file_path):
        data = {
            "graph": nx.readwrite.json_graph.node_link_data(self.graph),
            "node_colors": self.node_colors,
            "edge_colors": self.edge_colors,
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        self.recent_file = file_path
        self.root.title(f"Graph Commons Clone - {os.path.basename(file_path)}")
        messagebox.showinfo("Sauvegarde", f"Graphe sauvegardé dans {file_path}.")

    def load_graph(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                data = json.load(f)
            self.graph = nx.readwrite.json_graph.node_link_graph(data["graph"])
            self.node_colors = data.get("node_colors", {})
            self.edge_colors = data.get("edge_colors", {})
            self.recent_file = file_path
            self.root.title(f"Graph Commons Clone - {os.path.basename(file_path)}")
            self.update_canvas()
            messagebox.showinfo("Chargement", f"Graphe chargé depuis {file_path}.")

    def add_node(self):
        node_id = self.node_id_entry.get()
        label = self.node_label_entry.get()
        if node_id:
            self.graph.add_node(node_id, label=label)
            self.node_colors[node_id] = "lightblue"
            self.update_canvas()
            messagebox.showinfo("Nœud ajouté", f"Nœud '{node_id}' ajouté.")
        else:
            messagebox.showwarning("Erreur", "L'ID du nœud est requis.")

    def add_edge(self):
        source = self.edge_source_entry.get()
        target = self.edge_target_entry.get()
        if source and target:
            self.graph.add_edge(source, target)
            self.edge_colors[(source, target)] = "black"
            self.update_canvas()
            messagebox.showinfo("Arête ajoutée", f"Arête entre '{source}' et '{target}' ajoutée.")
        else:
            messagebox.showwarning("Erreur", "Les IDs source et cible sont requis.")

    def delete_element(self):
        if self.selected_node:
            self.graph.remove_node(self.selected_node)
            self.node_colors.pop(self.selected_node, None)
            self.selected_node = None
            self.update_canvas()
        else:
            messagebox.showinfo("Info", "Cliquez sur un élément à supprimer.")

    def change_node_color(self):
        if self.selected_node:
            color = colorchooser.askcolor(title="Choisir une couleur pour le nœud")[1]
            if color:
                self.node_colors[self.selected_node] = color
                self.update_canvas()
        else:
            messagebox.showinfo("Info", "Sélectionnez un nœud pour changer sa couleur.")

    def change_edge_color(self):
        messagebox.showinfo("Info", "Cliquez sur une arête pour changer sa couleur.")
        # Implémentation requise pour la sélection d'une arête avec le clic et modification de couleur

    def on_canvas_click(self, event):
        pos = nx.spring_layout(self.graph)
        for node, (x, y) in pos.items():
            if abs(event.xdata - x) < 0.1 and abs(event.ydata - y) < 0.1:
                self.selected_node = node
                messagebox.showinfo("Nœud sélectionné", f"Nœud sélectionné : {node}")
                return

    def update_canvas(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'label')

        node_colors = [self.node_colors.get(node, "lightblue") for node in self.graph.nodes()]
        edge_colors = [self.edge_colors.get(edge, "black") for edge in self.graph.edges()]

        nx.draw(
            self.graph, pos, ax=self.ax, with_labels=True, labels=labels,
            node_size=500, node_color=node_colors, font_size=10, edge_color=edge_colors
        )
        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = GraphCommonsApp(root)
    root.mainloop()
