from tkinter import *
import customtkinter as ctk

Menu_window = Tk()
Menu_window.title("Menu")
#Menu_window.geometry("500*350")
#Menu_window.minsize(350,175)
#Menu_window.maxsize(350,175)
Menu_window.config(background="#007082")
Menu_frame = Frame(Menu_window,width=310,height=135,bg="yellow")
Menu_frame.pack(expand=YES)

#Login_bouton=Button(Menu_frame,text="Identification",Font=("Arial",20),bg="white",fg="black",width=8, height=3)
#Login_bouton.grid(row=0,column=0)
bouton_identification=Button(Menu_frame , text="ID" , bg="white" , fg="black", width=8 , height=3)#, command=  comande=print="cc"
bouton_identification.pack(expand=YES)
bouton_identification.grid(row=0 , column=1)

l1= Label(text="teyugdeyfgd" , bg="purple")
l1.pack(pady=105)



Menu_window.mainloop()
