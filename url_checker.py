import urllib.request
import json

def check_url_health(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return {"url": url, "status": response.getcode(), "active": True}
    except Exception as e:
        return {"url": url, "error": str(e), "active": False}

if __name__ == "__main__":
    test_urls = ["https://github.com", "https://python.org"]
    results = [check_url_health(u) for u in test_urls]
    print(json.dumps(results, indent=2))
