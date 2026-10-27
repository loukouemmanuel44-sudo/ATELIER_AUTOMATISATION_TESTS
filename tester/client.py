import time
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_endpoint(self, path, timeout=3):
        start_time = time.time()
        try:
            response = requests.get(f"{self.base_url}{path}", timeout=timeout)
            latency = (time.time() - start_time) * 1000  # en millisecondes
            return {
                "status_code": response.status_code,
                "latency_ms": latency,
                "headers": response.headers,
                "json": response.json() if response.content else None,
                "error": None
            }
        except requests.exceptions.RequestException as e:
            latency = (time.time() - start_time) * 1000
            return {
                "status_code": None,
                "latency_ms": latency,
                "headers": {},
                "json": None,
                "error": str(e)
            }
