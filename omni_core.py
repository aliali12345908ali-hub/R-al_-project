import json
import os
import datetime

def system_status():
    print("==================================================")
    print("🌍 OMNISCALE AI GLOBAL FREELANCE ENGINE - ACTIVE")
    print("📍 Operator: Abdallah Ben Belgacem (Nice, France)")
    print("⚙️ Status: Fully Operational via Termux & GitHub")
    print("==================================================")
    
    # فحص الملفات الأساسية في المشروع
    components = ["crm_tracker.py", "smart_crm.py", "clients_db.json"]
    for comp in components:
        exists = os.path.exists(comp)
        print(f" - [{('OK' if exists else 'MISSING')}] Component: {comp}")

if __name__ == "__main__":
    system_status()
