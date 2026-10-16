import json

def scan_leads():
    print("[*] Scan started...")
    leads = [
        {"client": "TechFlow Paris", "url": "https://techflow-example.fr", "status": "Ready"},
        {"client": "Nice Web Solutions", "url": "https://niceweb-example.com", "status": "Ready"}
    ]
    with open("leads_db.json", "w") as f:
        json.dump(leads, f, indent=4)
    print("[+] Leads saved successfully.")

if __name__ == "__main__":
    scan_leads()
