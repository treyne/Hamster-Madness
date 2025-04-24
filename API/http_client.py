import httpx
from headers import get_headers

class HTTPClient:
    def __init__(self, base_url: str, follow_redirects: bool = False, http2: bool = True, timeout: float = 10.0):
        self.base_url = base_url
        self.follow_redirects = follow_redirects
        self.http2 = http2
        self.timeout = timeout
        self.client = httpx.Client(http2=self.http2, follow_redirects=self.follow_redirects, timeout=self.timeout)

    def _handle_response(self, response, sync=False):
        try:
            response.raise_for_status()
            content_type = response.headers.get("Content-Type", "")

            if "application/json" in content_type:
                result = response.json()
            elif "text/" in content_type or "html" in content_type:
                result = response.text
            else:
                result = response.content

            if sync:
                season2_config_version = response.headers.get('season2-config-version', None)
                return response.status_code, result, season2_config_version

            return response.status_code, result
        except httpx.RequestError as e:
            print(f"Ошибка запроса: {e}")
        except httpx.HTTPStatusError as e:
            print(f"HTTP ошибка {response.status_code}: {e.response.text}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        return None

    def get(self, endpoint: str, params: dict = None, headers: dict = None, sync=False, BitQuest=False):
        request_headers = headers if headers else get_headers("GET", BitQuest=BitQuest)
        response = self.client.get(f"{self.base_url}{endpoint}", params=params, headers=request_headers)
        return self._handle_response(response, sync)

    def post(self, endpoint: str, data: dict = None, headers: dict = None, sync=False, BitQuest=False):
        request_headers = headers if headers else get_headers("POST", BitQuest=BitQuest)
        response = self.client.post(f"{self.base_url}{endpoint}", json=data, headers=request_headers)
        return self._handle_response(response, sync)

    def options(self, endpoint: str, headers: dict = None, sync=False, BitQuest=False):
        request_headers = headers if headers else get_headers("OPTION", BitQuest=BitQuest)
        response = self.client.options(f"{self.base_url}{endpoint}", headers=request_headers)
        return self._handle_response(response, sync)

    def close(self):
        self.client.close()
