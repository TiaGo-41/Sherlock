import requests
import argparse
import json
import sys
import time
from datetime import datetime
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox, Scrollbar, Text, ttk
from tkinter import messagebox


class OSINTFramework:
    def __init__(self):
        self.results = {}
        self.start_time = None

    def collect_whois(self, domain):
        print(f"Collecting WHOIS information for: {domain}")
        try:
            self.results['whois'] = {
                "domain": domain,
                "registrar": "Example Registrar",
                "creation_date": "2023-01-01",
                "expiry_date": "2024-01-01",
                "status": "active"
            }
        except Exception as e:
            print(f"Error collecting WHOIS data: {e}")

    def collect_ip_info(self, ip):
        print(f"Collecting IP information for: {ip}")
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            if response.status_code == 200:
                self.results['ip_info'] = response.json()
            else:
                print(f"Error fetching IP information: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def collect_social_media(self, username):
        print(f"Collecting social media information for: {username}")
        try:
            self.results['social_media'] = {
                "twitter": f"https://twitter.com/{username}",
                "github": f"https://github.com/{username}",
                "linkedin": f"https://www.linkedin.com/in/{username}",
                "instagram": f"https://www.instagram.com/{username}/"
            }
        except Exception as e:
            print(f"Error collecting social media data: {e}")

    def collect_whatsmyname(self, username):
        print(f"Collecting information from WhatsMyName for: {username}")
        try:
            # Sending a POST request to WhatsMyName with the username.
            response = requests.post("https://whatsmyname.app/api/namecheck", data={"name": username})
            if response.status_code == 200:
                self.results['whatsmyname'] = response.json()
            else:
                print(f"Error fetching data from WhatsMyName: HTTP {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

    def save_results(self, output_file):
        try:
            with open(output_file, 'w') as file:
                json.dump(self.results, file, indent=4)
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")

    def display_results_gui(self, root, start_time):
        # Create a new window to display results
        result_window = Tk()
        result_window.title("OSINT Results")
        result_window.geometry("700x600")

        # Adding a label to show time and number of results
        total_time = time.time() - start_time
        num_results = sum(1 for key in self.results if self.results[key])

        status_label = Label(result_window, text=f"Time taken: {total_time:.2f}s | Results found: {num_results}", font=("Arial", 12))
        status_label.pack(pady=10)

        # Frame to hold the data
        result_frame = ttk.Frame(result_window, padding="10")
        result_frame.pack(fill="both", expand=True)

        # Adding a scrollable area for each category
        scroll = Scrollbar(result_frame)
        scroll.pack(side="right", fill="y")

        text_box = Text(result_frame, wrap="word", height=20, width=80, yscrollcommand=scroll.set)
        text_box.pack(padx=10, pady=10)

        # Display each category (WHOIS, IP, Social Media, WhatsMyName)
        for category, data in self.results.items():
            text_box.insert("end", f"\n\n{category.upper()}:\n")
            if isinstance(data, dict):
                for key, value in data.items():
                    text_box.insert("end", f"  {key}: {value}\n")
            else:
                text_box.insert("end", f"  {data}\n")

        scroll.config(command=text_box.yview)

        result_window.mainloop()


def gui_interface():
    def run_analysis():
        domain = domain_var.get()
        ip = ip_var.get()
        username = username_var.get()
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

        if not (domain or ip or username):
            messagebox.showwarning("Input Error", "Please provide at least one input (domain, IP, or username).")
            return

        osint = OSINTFramework()
        osint.start_time = time.time()

        if domain:
            osint.collect_whois(domain)

        if ip:
            osint.collect_ip_info(ip)

        if username:
            osint.collect_social_media(username)
            osint.collect_whatsmyname(username)

        # Update the status bar with the time taken and number of results
        elapsed_time = time.time() - osint.start_time
        status_var.set(f"Time taken: {elapsed_time:.2f}s | Results found: {len(osint.results)}")

        if output_file:
            osint.save_results(output_file)
            messagebox.showinfo("Success", f"Results saved to {output_file}")

        # After collecting all data, display the results in a new window
        osint.display_results_gui(root, osint.start_time)

    # Creating the main window
    root = Tk()
    root.title("OSINT Framework")
    root.geometry("400x350")
    root.config(bg="#f4f4f4")

    # Adding a frame for better layout management
    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky="nsew")

    # Adding labels, entries, and buttons with improved layout
    ttk.Label(frame, text="Domain:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    domain_var = StringVar()
    ttk.Entry(frame, textvariable=domain_var, width=30).grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(frame, text="IP Address:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    ip_var = StringVar()
    ttk.Entry(frame, textvariable=ip_var, width=30).grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(frame, text="Social Media Username:", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    username_var = StringVar()
    ttk.Entry(frame, textvariable=username_var, width=30).grid(row=2, column=1, padx=10, pady=10)

    ttk.Button(frame, text="Run Analysis", command=run_analysis, style="TButton").grid(row=3, column=0, columnspan=2, pady=20)

    # Adding a status bar at the bottom
    status_var = StringVar()
    status_label = Label(root, textvariable=status_var, font=("Arial", 10), relief="sunken", anchor="w")
    status_label.grid(row=1, column=0, sticky="ew")

    # Adding a style for the button
    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 12))

    # Running the GUI event loop
    root.mainloop()


def main():
    import sys  # Pour vérifier les arguments passés

    # Si aucun argument n'est fourni, lance la GUI
    if len(sys.argv) == 1:
        gui_interface()
        return

    # Si des arguments sont passés, utilise argparse pour le mode CLI
    parser = argparse.ArgumentParser(description="OSINT Framework in Python")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI interface")
    parser.add_argument("--domain", help="Domain name to analyze")
    parser.add_argument("--ip", help="IP address to analyze")
    parser.add_argument("--username", help="Social media username to analyze")
    parser.add_argument("--output", help="File to save the results (JSON format)", default=f"osint_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    args = parser.parse_args()

    if args.gui:
        gui_interface()
        return

    # Mode CLI
    osint = OSINTFramework()
    if args.domain:
        osint.collect_whois(args.domain)
    if args.ip:
        osint.collect_ip_info(args.ip)
    if args.username:
        osint.collect_social_media(args.username)
        osint.collect_whatsmyname(args.username)

    osint.display_results_gui(None, time.time())

    if args.output:
        osint.save_results(args.output)


if __name__ == "__main__":
    main()
