import urllib.request
import json
import sys

BASE_URL = "http://127.0.0.1:5000/api"

def test_predict_text():
    url = f"{BASE_URL}/predict/text"
    data = {"text": "This is a spam message with lots of links."}
    req = urllib.request.Request(url, 
                                 data=json.dumps(data).encode('utf-8'), 
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            result = json.load(response)
            print(f"Predict Text Result: {result}")
    except Exception as e:
        print(f"Predict Text Failed: {e}")

def test_results_endpoint():
    try:
        with urllib.request.urlopen(f"{BASE_URL}/results") as response:
            result = json.load(response)
            print(f"Results Endpoint: {result}")
    except Exception as e:
        print(f"Results Endpoint Failed: {e}")

if __name__ == "__main__":
    print("Running Verification Tests...")
    test_predict_text()
    test_results_endpoint()
