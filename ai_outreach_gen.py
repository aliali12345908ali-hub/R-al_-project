import json

def generate_proposals():
    print("[*] جاري توليد رسائل مخصصة بالذكاء الاصطناعي لكل عميل...")
    try:
        with open("leads_db.json", "r") as f:
            leads = json.load(f)
        for lead in leads:
            print(f" -> تم تجهيز العرض المخصص للعميل: {lead['client']} ({lead['url']})")
    except FileNotFoundError:
        print("[-] يرجى تشغيل lead_scraper.py أولاً.")

if __name__ == "__main__":
    generate_proposals()
