import urllib.request
import json
import sys
import os

def check_urls():
    # قائمة روابط للاختبار (يمكن للعميل تعديلها بحرية)
    targets = [
        "https://www.google.com",
        "https://github.com",
        "https://www.python.org",
        "https://httpbin.org/status/500"
    ]
    
    results = []
    print(f"🔍 [Advanced URL Checker] Starting batch analysis for {len(targets)} targets...\n")
    
    for target_url in targets:
        print(f"-> Checking: {target_url}")
        try:
            req = urllib.request.Request(
                target_url, 
                headers={'User-Agent': 'Mozilla/5.0 (Termux; Python Utility)'}
            )
            with urllib.request.urlopen(req, timeout=5) as response:
                status_code = response.getcode()
                results.append({
                    "url": target_url,
                    "status_code": status_code,
                    "status": "ONLINE & ACCESSIBLE"
                })
        except Exception as e:
            results.append({
                "url": target_url,
                "error": str(e),
                "status": "ERROR OR UNREACHABLE"
            })
            
    # حفظ النتائج في تقرير JSON حقيقي
    report_file = "scan_report.json"
    with open(report_file, "w") as f:
        json.dump(results, f, indent=4)
        
    print(f"\n✨ [Advanced URL Checker] Batch scan completed successfully!")
    print(f"📁 Report saved locally to: {report_file}")
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    check_urls()
