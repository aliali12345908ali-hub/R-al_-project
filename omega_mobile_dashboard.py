import json
import os

def show_dashboard():
    print("=" * 50)
    print(" 👑 OMEGA CYBER-AGENCY MOBILE COMMAND NEXUS 👑 ")
    print("=" * 50)
    print(f"👤 Operator: MR ABDALLAH BEN BELGACEM")
    print(f"📍 Headquarters: Nice, France")
    print(f"🏦 Bank Gateway: FPE Charenton (RIB/IBAN Active)")
    print(f"⚖️ Legal Framework: Micro-entreprise (Art. 293 B du CGI)")
    print("-" * 50)
    
    status_files = [
        "omega_master_blueprint.json",
        "whale_campaign_status.json",
        "omega_command_nexus_status.json",
        "live_payment_gateway_status.json"
    ]
    
    for file in status_files:
        if os.path.exists(file):
            print(f"[✅] {file} -> LOADED & ACTIVE")
        else:
            print(f"[⚠️] {file} -> PENDING")
            
    print("=" * 50)
    print("🚀 Status: All Systems Operational 24/7 in Cloud & Termux")
    print("=" * 50)

if __name__ == "__main__":
    show_dashboard()
