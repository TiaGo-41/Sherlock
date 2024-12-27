import requests
import argparse
import json
from datetime import datetime

class OSINTFramework:
    def __init__(self):
        self.results = {}

    def collect_whois(self, domain):
        print(f"Collecting WHOIS information for: {domain}")
        # Exemple de collecte WHOIS (utilisez une API tierce comme whoisxmlapi ou des bibliothèques comme python-whois)
        try:
            # Replace with actual WHOIS API or library usage
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

def main():
    parser = argparse.ArgumentParser(description="OSINT Framework in Python")
    parser.add_argument("--domain", help="Domain name to analyze")
    parser.add_argument("--ip", help="IP address to analyze")
    parser.add_argument("--username", help="Social media username to analyze")
    parser.add_argument("--output", help="File to save the results (JSON format)", default=f"osint_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    args = parser.parse_args()

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
