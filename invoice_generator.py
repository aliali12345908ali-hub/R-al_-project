import json
import datetime

def create_invoice(client_name, amount_eur):
    invoice = {
        "invoice_id": "INV-2026-001",
        "client": client_name,
        "amount": f"{amount_eur} EUR",
        "framework": "Micro-entreprise France",
        "date": str(datetime.datetime.now()),
        "status": "Pending Payment"
    }
    with open("latest_invoice.json", "w") as f:
        json.dump(invoice, f, indent=4)
    print(f"[€] تم إصدار الفوعة الرسمية بقيمة {amount_eur} يورو للعميل {client_name} بنجاح!")

if __name__ == "__main__":
    create_invoice("TechFlow Paris", 1250)
