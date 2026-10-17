from flask import Flask, render_template_string
import sqlite3
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Omni-Verse Dashboard</title>
    <style>
        body { font-family: Tahoma, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }
        h1 { color: #38bdf8; text-align: center; }
        .card { background: #1e293b; padding: 15px; margin: 15px 0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .status { color: #4ade80; font-weight: bold; }
    </style>
</head>
<body>
    <h1>منظومة Omni-Verse - لوحة التحكم المركزية</h1>
    <div class="card">
        <h3>حالة النظام: <span class="status">يعمل بأقصى أولوية (Active)</span></h3>
        <p>المكونات المتصلة: البحث القانوني، الذكاء الاصطناعي للروبوتات، والجسر المركزي الموحد.</p>
    </div>
    <div class="card">
        <h3>آخر سجلات التنسيق المركزي:</h3>
        <ul>
            {% for log in logs %}
                <li>[{{ log[4] ]] - <b>{{ log[1] }}</b>: {{ log[2] }} (الحالة: {{ log[3] }})</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    db_path = "omniverse_central.db"
    logs = []
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM system_bridge_logs ORDER BY id DESC LIMIT 5")
        logs = cursor.fetchall()
        conn.close()
    return render_template_string(HTML_TEMPLATE, logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


