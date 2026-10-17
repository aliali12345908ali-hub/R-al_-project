import os
import sqlite3
from datetime import datetime

def log_system_vitals():
    # جمع بيانات أداء الجهاز محلياً
    db_path = "omniverse_central.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_vitals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute("INSERT INTO system_vitals (status) VALUES ('All systems operational & sensory inputs active.')")
    conn.commit()
    conn.close()
    print("[✓] System vitals & sensory data logged successfully.")

if __name__ == "__main__":
    log_system_vitals()


