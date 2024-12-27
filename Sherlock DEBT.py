#importation des modules complaimentaires et des labeles.
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import os
import webbrowser
from tkinter import ttk
from tkinter import messagebox
import subprocess

#customisation et debut de la boucle.
Sherlock_DEBT = Tk()
Sherlock_DEBT.title("Sherlock DEBT")
Sherlock_DEBT.config(background="#3A3A3A")
Sherlock_DEBT.iconbitmap("PLlogo.ico")

def open_SALVAC () :

    open_SALVAC = Tk()
    open_SALVAC.title("SALVAC")
    open_SALVAC.config(background="#3A3A84")

    open_SALVAC.mainloop()


#importation des bouton
Bouton_exit=Button(text="Stop-Code", command=quit)
Bouton_exit.pack
Bouton_exit.grid(row=0 , column=1)

Bouton_SALVAC=Button(text="SALVAC")#, comand=open_SALVAC    1
Bouton_SALVAC.pack
Bouton_SALVAC.grid(row=0 , column=2)

Bouton_QQOQCP=Button(text="QQOQCP")
Bouton_QQOQCP.pack
Bouton_QQOQCP.grid(row=0 , column=3)

Bouton_WIKIDIC=Button(text="WIKIDIC")
Bouton_WIKIDIC.pack
Bouton_WIKIDIC.grid(row=0 , column=4)

#Création du bouton PERSC
Bouton_PERSC=Button(text="PERSC")
Bouton_PERSC.pack
Bouton_PERSC.grid(row=0 , column=5)

Bouton_briefing=Button(text="briefing")
Bouton_briefing.pack
Bouton_briefing.grid(row=0, column=6)

Bouton_allertes=Button(text="allertes")
Bouton_allertes.pack
Bouton_allertes.grid(row=0, column=6)

Bouton_UNITÉE=Button(text="UNITÉE")
Bouton_UNITÉE.pack
Bouton_UNITÉE.grid(row=0, column=7)
Bouton_Fichier=Button(text="Fichier")
Bouton_Fichier.pack
Bouton_Fichier.grid(row=0, column=8)

Bouton_Vocal_stt=Button(text="Vocal_stt")
Bouton_Vocal_stt.pack
Bouton_Vocal_stt.grid(row=0, column=9)

Bouton_MARINS_Cannal=Button(text="MARINS Cannal")
Bouton_MARINS_Cannal.pack
Bouton_MARINS_Cannal.grid(row=0, column=10)

Bouton_CADASTRE=Button(text="CADASTRE")
Bouton_CADASTRE.pack
Bouton_CADASTRE.grid(row=0, column=11)

def ouvrir_osint():
    # Remplacez 'mon_script.py' par le chemin de votre fichier Python
    subprocess.run(['python', 'osint.py'])

Bouton_OSINT=Button(text="OSINT", command=ouvrir_osint)
Bouton_OSINT.pack
Bouton_OSINT.grid(row=0, column=12)

# Vocal stt
#MARINS Cannal
#CADASTRE


#first=tkinter.Sherlock_DEBT
#first.add_radiobutton(text="clic-me")






Sherlock_DEBT.mainloop()