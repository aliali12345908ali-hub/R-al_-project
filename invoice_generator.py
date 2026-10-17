import json
import datetime

def generate_real_bank_invoice():
    invoice_data = {
        "invoice_number": "FA-2026-001",
        "beneficiary": "MR ABDALLAH BEN BELGACEM",
        "domiciliation": "FPE Charenton, 1 Place des Marseillais, 94220 Charenton Le Pont",
        "iban": "FR76 1659 8000 0140 0014 2630 322",
        "bic_swift": "FPELFR21XXX",
        "status": "Micro-entreprise Compliant",
        "vat_notice": "TVA non applicable, art. 293 B du CGI",
        "services": "Autonomous AI Cyber-Agency & High-Ticket Whale Solutions",
        "amount_due": "5000.00 EUR",
        "date": str(datetime.datetime.now())
    }
    
    with open("official_invoice_with_rib.json", "w") as f:
        json.dump(invoice_data, f, indent=4)
        
    print("[💶🏦] تم دمج حسابك البنكي الفرنسي الحقيقي (RIB/IBAN) مع الفاتورة الرسمية بنجاح تام!")

if __name__ == "__main__":
    generate_real_bank_invoice()
