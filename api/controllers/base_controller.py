import requests
from requests.exceptions import RequestException
import logging

from api.utils.json_schema_validator import validate_json_schema


class BaseController:
    def __init__(self, base_url: str = None, headers: dict = None, cookies: dict = None, auth=None):
        """
        Initialize the API client with base URL and default headers
        :param base_url: Base URL for all API requests
        :param headers: Dictionary of default headers
        """
        self.base_url = base_url.rstrip('/') if base_url else ''
        self.auth = auth
        self.cookies = cookies
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.logger = logging.getLogger(__name__)

    def _send_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Send HTTP request and handle response
        param method: HTTP method (get, post, put, delete, etc.)
        param endpoint: API endpoint (e.g., '/airports')
        param kwargs: Additional arguments for requests (params, json, headers, etc.)
        return: Response object
        """
        url = f"{self.base_url}{endpoint}"

        try:
            self.logger.debug(f"Sending {method.upper()} request to {url}")
            response = self.session.request(method, url, **kwargs)
            self.logger.debug(f"Response: {response.status_code}")
            return response
        except RequestException as req_err:
            self.logger.error(f"Request error occurred: {req_err}")
            raise

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Send GET request"""
        return self._send_request('get', endpoint, **kwargs)

    def post(self, endpoint: str, payload: dict = None, **kwargs) -> requests.Response:
        """Send POST request"""
        return self._send_request('post', endpoint, json=payload, **kwargs)

    def put(self, endpoint: str, payload: dict = None, **kwargs) -> requests.Response:
        """Send PUT request"""
        return self._send_request('put', endpoint, json=payload, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Send DELETE request"""
        return self._send_request('delete', endpoint, **kwargs)

    def add_header(self, key: str, value: str):
        """Add a header to all subsequent requests"""
        self.session.headers.update({key: value})

    def remove_header(self, key: str):
        """Remove a header from subsequent requests"""
        self.session.headers.pop(key, None)

    @staticmethod
    def assert_response_code(response: requests.Response, expected_code: int):
        """
        Assert that the response has the expected status code.
        Raises AssertionError if not.
        """
        actual_code = response.status_code
        assert actual_code == expected_code, (
            f"Expected status {expected_code}, got {actual_code}. "
            f"Response body: {response.text[:200]}")

    @staticmethod
    def validate_schema_file(response: requests.Response, schema_file):
        validate_json_schema(response.json(), schema_file)
