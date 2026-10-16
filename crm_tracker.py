import json
import datetime

def log_client(client_name, status, platform):
    record = {
        "client": client_name,
        "status": status,
        "platform": platform,
        "date": str(datetime.datetime.now())
    }
    
    try:
        with open("clients_db.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
        
    data.append(record)
    
    with open("clients_db.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"تم تسجيل العميل {client_name} بنجاح!")

if __name__ == "__main__":
    # مثال تجريبي لتسجيل أول عميل مستهدف
    log_client("Global Startup Client", "Outreach Sent", "LinkedIn")
