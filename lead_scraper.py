import json

def scan_leads():
    print("[*] جاري تشغيل مسح الاستخبارات للعملاء المستهدفين (Nice, Paris, Global)...")
    sample_leads = [
        {"client": "TechFlow Paris", "url": "https://techflow-example.fr", "status": "Ready for Audit"},
        {"client": "Nice Web Solutions", "url": "https://niceweb-example.com", "status": "Ready for Audit"}
    ]
    with open("leads_db.json", "w") as f:
        json.dump(sample_leads, f, indent=4)
    print("[+] تم رصد واستخراج العملاء بنجاح وحفظهم في leads_db.json")

if __name__ == "__main__":
    scan_leads()
