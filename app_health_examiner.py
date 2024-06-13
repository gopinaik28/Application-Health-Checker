import requests
import time
from urllib.parse import urlparse

def check_app_health(url, expected_status_code=200, timeout=10):
    
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        end_time = time.time()
        response_time = end_time - start_time

        if response.status_code == expected_status_code:
            status = "up"
        else:
            status = "down"

        return {
            "status": status,
            "status_code": response.status_code,
            "response_time": response_time
        }
    except requests.exceptions.RequestException:
        return {
            "status": "down",
            "status_code": None,
            "response_time": None
        }

if __name__ == "__main__":
    url = input("Enter the URL of the application to check: ").strip()
    
    health_report = check_app_health(url)
    print(f"Application status: {health_report['status']}")
    print(f"HTTP status code: {health_report['status_code']}")
    if health_report['response_time'] is not None:
        print(f"Response time: {health_report['response_time']:.2f} seconds")
    else:
        print("Response time: N/A")
