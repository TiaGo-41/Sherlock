import requests
import argparse
import json
from datetime import datetime
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox

class OSINTFramework:
    def __init__(self):
        self.results = {}

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

    def save_results(self, output_file):
        try:
            with open(output_file, 'w') as file:
                json.dump(self.results, file, indent=4)
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")

    def display_results(self):
        print("\nCollected Results:")
        for key, value in self.results.items():
            print(f"{key.upper()}: {json.dumps(value, indent=4)}")

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

        if domain:
            osint.collect_whois(domain)

        if ip:
            osint.collect_ip_info(ip)

        if username:
            osint.collect_social_media(username)

        if output_file:
            osint.save_results(output_file)
            messagebox.showinfo("Success", f"Results saved to {output_file}")

    root = Tk()
    root.title("OSINT Framework")

    Label(root, text="Domain:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    domain_var = StringVar()
    Entry(root, textvariable=domain_var).grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="IP Address:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    ip_var = StringVar()
    Entry(root, textvariable=ip_var).grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="Social Media Username:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    username_var = StringVar()
    Entry(root, textvariable=username_var).grid(row=2, column=1, padx=10, pady=5)

    Button(root, text="Run Analysis", command=run_analysis).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description="OSINT Framework in Python")
    parser.add_argument("--gui", action="store_true", help="Launch the GUI interface")
    parser.add_argument("--domain", help="Domain name to analyze")
    parser.add_argument("--ip", help="IP address to analyze")
    parser.add_argument("--username", help="Social media username to analyze")
    parser.add_argument("--output", help="File to save the results (JSON format)", default=f"osint_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    args = parser.parse_args()

    # If no arguments are passed, launch the GUI by default
    if len(vars(args)) == 1 or args.gui:  # len(vars(args)) == 1 checks if no arguments except --gui
        gui_interface()
        return

    # CLI functionality
    osint = OSINTFramework()

    if args.domain:
        osint.collect_whois(args.domain)

    if args.ip:
        osint.collect_ip_info(args.ip)

    if args.username:
        osint.collect_social_media(args.username)

    osint.display_results()

    if args.output:
        osint.save_results(args.output)

if __name__ == "__main__":
    main()
