from tkinter import *
import customtkinter as ctk

Menu_window = Tk()
Menu_window.title("Error")
#Menu_window.geometry("500*350")
#Menu_window.minsize(350,175)
#Menu_window.maxsize(350,175)
Menu_window.config(background="#007082")

Menu_frame = Frame(Menu_window,width=310,height=135,bg="yellow")
Menu_frame.pack(expand=YES)

bouton_identification=Button(Menu_frame , text="RSA-OTP" , width=8 , height=3)#, command=  comande=print="cc"
bouton_identification.pack(expand=YES)
bouton_identification.grid(row=0 , column=1)

Menu_window.mainloop()
