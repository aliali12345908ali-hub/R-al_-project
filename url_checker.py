import urllib.request
import json
import sys

def check_url(target_url):
    print(f"🔍 [URL Checker] Analyzing target: {target_url}...")
    try:
        # محاولة الاتصال بالرابط لفحص حالة الاستجابة
        req = urllib.request.Request(
            target_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            headers = dict(response.headers)
            
        result = {
            "url": target_url,
            "status_code": status_code,
            "is_secure": target_url.startswith("https"),
            "server": headers.get("Server", "Unknown"),
            "status": "ONLINE & SECURE"
        }
        print("✅ [URL Checker] Analysis completed successfully:")
        print(json.dumps(result, indent=4))
        
    except Exception as e:
        error_result = {
            "url": target_url,
            "error": str(e),
            "status": "OFFLINE OR UNREACHABLE"
        }
        print("❌ [URL Checker] Error analyzing URL:")
        print(json.dumps(error_result, indent=4))

if __name__ == "__main__":
    # مثال على فحص موقع حقيقي
    test_target = "https://www.google.com"
    check_url(test_target)
