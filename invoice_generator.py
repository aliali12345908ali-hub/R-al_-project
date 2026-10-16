import json
import datetime

def make_invoice():
    inv = {
        "id": "INV-2026-001",
        "client": "TechFlow Paris",
        "amount": "1250 EUR",
        "status": "Generated & Ready"
    }
    with open("latest_invoice.json", "w") as f:
        json.dump(inv, f, indent=4)
    print("[€] Invoice generated successfully for TechFlow Paris!")

if __name__ == "__main__":
    make_invoice()
