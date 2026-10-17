import json
import datetime

def create_legal_invoice():
    invoice_data = {
        "invoice_number": "FA-2026-001",
        "operator": "Abdallah Ben Belgacem",
        "location": "Nice, France",
        "status": "Micro-entreprise Compliant",
        "client": "TechFlow Paris",
        "services": "AI OmniScale Automated Web Solutions",
        "amount_due": "1250.00 EUR",
        "vat_notice": "TVA non applicable, art. 293 B du CGI",
        "date": str(datetime.datetime.now())
    }
    with open("official_invoice_fr.json", "w") as f:
        json.dump(invoice_data, f, indent=4)
    print("[€] تم إصدار الفاتورة الفرنسية الرسمية المطابقة لقانون Micro-entreprise بنجاح تام!")

if __name__ == "__main__":
    create_legal_invoice()
