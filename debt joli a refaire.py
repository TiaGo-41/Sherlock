from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import os
import webbrowser
from tkinter import messagebox

# Configuration de l'application principale
Sherlock_DEBT = Tk()
Sherlock_DEBT.title("Sherlock DEBT")
Sherlock_DEBT.config(background="#3A3A3A")
Sherlock_DEBT.iconbitmap("PLlogo.ico")
Sherlock_DEBT.geometry("1200x600")  # Définir la taille de la fenêtre

# Fonction d'ouverture de la fenêtre SALVAC
def open_SALVAC():
    open_SALVAC = Tk()
    open_SALVAC.title("SALVAC")
    open_SALVAC.config(background="#3A3A84")
    open_SALVAC.geometry("400x200")
    open_SALVAC.mainloop()

# Utilisation de CustomTkinter pour les boutons
ctk.set_appearance_mode("dark")  # Mode sombre pour l'application
ctk.set_default_color_theme("dark-blue")

# Création des boutons avec CustomTkinter
Bouton_exit = ctk.CTkButton(Sherlock_DEBT, text="Stop-Code", command=quit, width=120, height=40)
Bouton_exit.grid(row=0, column=1, padx=10, pady=10)

Bouton_SALVAC = ctk.CTkButton(Sherlock_DEBT, text="SALVAC", command=open_SALVAC, width=120, height=40)
Bouton_SALVAC.grid(row=0, column=2, padx=10, pady=10)

Bouton_QQOQCP = ctk.CTkButton(Sherlock_DEBT, text="QQOQCP", width=120, height=40)
Bouton_QQOQCP.grid(row=0, column=3, padx=10, pady=10)

Bouton_WIKIDIC = ctk.CTkButton(Sherlock_DEBT, text="WIKIDIC", width=120, height=40)
Bouton_WIKIDIC.grid(row=0, column=4, padx=10, pady=10)

Bouton_PERSC = ctk.CTkButton(Sherlock_DEBT, text="PERSC", width=120, height=40)
Bouton_PERSC.grid(row=0, column=5, padx=10, pady=10)

Bouton_briefing = ctk.CTkButton(Sherlock_DEBT, text="briefing", width=120, height=40)
Bouton_briefing.grid(row=0, column=6, padx=10, pady=10)

Bouton_allertes = ctk.CTkButton(Sherlock_DEBT, text="allertes", width=120, height=40)
Bouton_allertes.grid(row=0, column=7, padx=10, pady=10)

Bouton_UNITÉE = ctk.CTkButton(Sherlock_DEBT, text="UNITÉE", width=120, height=40)
Bouton_UNITÉE.grid(row=0, column=8, padx=10, pady=10)

Bouton_Fichier = ctk.CTkButton(Sherlock_DEBT, text="Fichier", width=120, height=40)
Bouton_Fichier.grid(row=0, column=9, padx=10, pady=10)

Bouton_Vocal_stt = ctk.CTkButton(Sherlock_DEBT, text="Vocal_stt", width=120, height=40)
Bouton_Vocal_stt.grid(row=1, column=1, padx=10, pady=10)

Bouton_MARINS_Cannal = ctk.CTkButton(Sherlock_DEBT, text="MARINS Cannal", width=120, height=40)
Bouton_MARINS_Cannal.grid(row=1, column=2, padx=10, pady=10)

Bouton_CADASTRE = ctk.CTkButton(Sherlock_DEBT, text="CADASTRE", width=120, height=40)
Bouton_CADASTRE.grid(row=1, column=3, padx=10, pady=10)

Bouton_WMN = ctk.CTkButton(Sherlock_DEBT, text="WMN", width=120, height=40)
Bouton_WMN.grid(row=1, column=4, padx=10, pady=10)

# Ajout d'un label pour le titre avec une police stylisée
label_title = ctk.CTkLabel(Sherlock_DEBT, text="Sherlock DEBT", font=("Arial", 24, "bold"), text_color="white")
label_title.grid(row=0, column=0, padx=20, pady=20)

# Mise en page améliorée
Sherlock_DEBT.grid_rowconfigure(0, weight=1)
Sherlock_DEBT.grid_columnconfigure([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], weight=1)

Sherlock_DEBT.mainloop()
