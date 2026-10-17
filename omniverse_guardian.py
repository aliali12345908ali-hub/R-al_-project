import os
import time
import subprocess
import sqlite3
from datetime import datetime

TARGET_SCREENS = {
    "legal_core": "python3 legal_engine.py",
    "robotics_core": "python3 ai_robotics_engine.py",
    "master_bridge": "python3 omniverse_master_bridge.py",
    "web_dashboard": "python3 omniverse_web_dashboard.py"
}

def check_and_heal():
    print(f"[*] [{datetime.now()}] Omni-Verse Guardian: Checking system health...")
    
    # جلب الجلسات النشطة حالياً
    active_screens = subprocess.check_output(['screen', '-ls']).decode('utf-8')
    
    for screen_name, command in TARGET_SCREENS.items():
        if screen_name not in active_screens:
            print(f"[!] Alert: {screen_name} is down! Restarting with high priority...")
            # إعادة تشغيل الجلسة في الخلفية
            subprocess.run(['screen', '-d', '-m', '-S', screen_name, 'bash', '-c', f'cd ~/ad_astra_omniverse/real_project && {command}'])
            
            # إعادة ضبط الأولوية تلقائياً
            time.sleep(1)
            pids = subprocess.check_output(['pgrep', '-f', screen_name]).decode('utf-8').split()
            if pids:
                pid = pids[0].strip()
                subprocess.run(['renice', '-n', '-10', '-p', pid])
                print(f"[✓] {screen_name} healed and prioritized (PID: {pid}).")

if __name__ == "__main__":
    while True:
        check_and_heal()
        time.sleep(30) # فحص الحالة كل 30 ثانية


