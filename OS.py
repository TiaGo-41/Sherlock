import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from subprocess import Popen
import threading
import requests

def open_calculator():
    """Open a simple calculator."""
    calc_win = tk.Toplevel(root)
    calc_win.title("Calculatrice")
    calc_win.geometry("300x400")
    calc_win.configure(bg="#2e2e2e")

    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur de calcul : {e}")

    entry = tk.Entry(calc_win, font=("Arial", 16), bg="#1e1e1e", fg="white", insertbackground="white")
    entry.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    buttons_frame = tk.Frame(calc_win, bg="#2e2e2e")
    buttons_frame.pack(fill=tk.BOTH, expand=True)

    buttons = [
        "7", "8", "9", "+",
        "4", "5", "6", "-",
        "1", "2", "3", "*",
        "C", "0", "=", "/"
    ]

    def button_click(button):
        if button == "C":
            entry.delete(0, tk.END)
        elif button == "=":
            calculate()
        else:
            entry.insert(tk.END, button)

    for i, button in enumerate(buttons):
        tk.Button(buttons_frame, text=button, font=("Arial", 14), bg="#3e3e3e", fg="white", command=lambda b=button: button_click(b)).grid(row=i//4, column=i%4, sticky="nsew", padx=2, pady=2)

    for i in range(4):
        buttons_frame.grid_columnconfigure(i, weight=1)
        buttons_frame.grid_rowconfigure(i, weight=1)

def open_browser():
    """Open a simple browser."""
    browser_win = tk.Toplevel(root)
    browser_win.title("Navigateur Web")
    browser_win.geometry("800x600")
    browser_win.configure(bg="#1e1e1e")

    # URL bar
    url_frame = tk.Frame(browser_win, bg="#1e1e1e")
    url_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    url_bar = tk.Entry(url_frame, font=("Arial", 14), bg="#3e3e3e", fg="white", insertbackground="white")
    url_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

    # Browser display area
    browser_display = tk.Text(browser_win, wrap=tk.WORD, bg="#1e1e1e", fg="white", font=("Arial", 12), state=tk.DISABLED)
    browser_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    loading_label = tk.Label(browser_win, text="", bg="#1e1e1e", fg="white", font=("Arial", 12))
    loading_label.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

    def load_page():
        query = url_bar.get()
        if not query.startswith("http://") and not query.startswith("https://"):
            query = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        def fetch_content():
            loading_label.config(text="Chargement en cours...")
            try:
                response = requests.get(query, timeout=10)
                response.raise_for_status()
                content = response.text
                browser_display.config(state=tk.NORMAL)
                browser_display.delete(1.0, tk.END)
                browser_display.insert(tk.END, content)
                browser_display.config(state=tk.DISABLED)
            except Exception as e:
                browser_display.config(state=tk.NORMAL)
                browser_display.delete(1.0, tk.END)
                browser_display.insert(tk.END, f"Erreur : {e}")
                browser_display.config(state=tk.DISABLED)
            finally:
                loading_label.config(text="")

        threading.Thread(target=fetch_content, daemon=True).start()

    # Search button
    load_button = tk.Button(url_frame, text="Aller", command=load_page, bg="#3e3e3e", fg="white")
    load_button.pack(side=tk.RIGHT, padx=5, pady=5)

def quit_app():
    """Quit the application."""
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Mini OS")
root.geometry("800x600")
root.resizable(False, False)

# Set the desktop background
background_image = tk.PhotoImage(file="fde.png")  # Replace with your image path
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Taskbar
taskbar = tk.Frame(root, bg="#2e2e2e", height=40)
taskbar.pack(side=tk.BOTTOM, fill=tk.X)

# Taskbar buttons
btn_calc = tk.Button(taskbar, text="Calculatrice", command=open_calculator, bg="#3e3e3e", fg="white")
btn_calc.pack(side=tk.LEFT, padx=5, pady=5)

btn_browser = tk.Button(taskbar, text="Navigateur", command=open_browser, bg="#3e3e3e", fg="white")
btn_browser.pack(side=tk.LEFT, padx=5, pady=5)

btn_exit = tk.Button(taskbar, text="Quitter", command=quit_app, bg="#b22222", fg="white")
btn_exit.pack(side=tk.RIGHT, padx=5, pady=5)

# Main loop
root.mainloop()
