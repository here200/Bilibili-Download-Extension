import requests

_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
    # 防盗链
    "referer": "https://www.bilibili.com/",
    "cookie": ""
}


def get(url, params=None):
    return requests.get(headers=_headers, url=url, params=params)


def decode_response(response):
    return response.content.decode()
