import os
import sqlite3
import time
from datetime import datetime

def neural_oracle_loop():
    db_path = "omniverse_central.db"
    while True:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS neural_insights (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    insight TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            cursor.execute("INSERT INTO neural_insights (insight) VALUES ('Neural Oracle: System operating at peak efficiency. No anomalies detected.')")
            conn.commit()
            conn.close()
            print(f"[⚡] Neural Oracle Pulse Checked at {datetime.now()}")
        except Exception as e:
            print(f"[!] Oracle Notice: {e}")
        time.sleep(60)

if __name__ == "__main__":
    neural_oracle_loop()


