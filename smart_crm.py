import json
import os

def analyze_and_suggest():
    if not os.path.exists("clients_db.json"):
        print("لا توجد قاعدة بيانات عملاء حالياً.")
        return
        
    with open("clients_db.json", "r") as f:
        clients = json.load(f)
        
    print(f"--- تقرير النظام الذكي للعملاء ({len(clients)} عميل مسجل) ---")
    for idx, client in enumerate(clients, 1):
        print(f"\n{idx}. العميل: {client['client']}")
        print(f"   - المنصة: {client['platform']}")
        print(f"   - الحالة الحالية: {client['status']}")
        print(f"   - اقتراح الذكاء الاصطناعي: متابعة العميل بإرسال دراسة جدوى أو تدقيق مجاني إضافي لرفع نسبة التحويل.")

if __name__ == "__main__":
    analyze_and_suggest()
