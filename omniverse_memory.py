import sqlite3
import os

def init_memory():
    db_path = "omniverse_vector_memory.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS long_term_memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("[✓] Omni-Verse Long-Term Memory Initialized Successfully.")

if __name__ == "__main__":
    init_memory()


