import json

def generate():
    try:
        with open("leads_db.json", "r") as f:
            leads = json.load(f)
        for l in leads:
            print(f"[AI] Proposal ready for: {l['client']} -> {l['url']}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    generate()
