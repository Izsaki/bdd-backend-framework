import requests
from requests import Response


def get(url: str, params: object = None) -> Response:
    return requests.get(url, params=params)


def post(url: str, data: object = None, json: object = None) -> Response:
    return requests.post(url, data=data, json=json)


def put(url: str, data: object = None, json: object = None) -> Response:
    return requests.put(url, data=data, json=json)


def delete(url: str, data: object = None, json: object = None, params: object = None) -> Response:
    return requests.delete(url, data=data, json=json, params=params)


class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def call(self, endpoint: str, method: str, params: object = None, data: object = None,
             json: object = None) -> Response:
        url = f"{self.base_url}/{endpoint}"
        if method.upper() == "GET":
            return get(url, params=params)

        elif method.upper() == "POST":
            return post(url, data=data, json=json)

        elif method.upper() == "PUT":
            return put(url, data=data, json=json)

        elif method.upper() == "DELETE":
            return delete(url, data=data, json=json, params=params)
