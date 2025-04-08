import os
from dotenv import load_dotenv

def get_headers(Method, BitQuest=False):
    # Загрузка переменных из .env файла
    load_dotenv()
    Bearer = os.getenv('Bearer')
    Bearer_BitQuest = os.getenv('Bearer_BitQuest')

    referer = "https://app.bitquest.games/" if BitQuest else "https://season2.hamsterkombatgame.io/"
    token = Bearer_BitQuest if BitQuest else Bearer

    common_headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Referer": referer,
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4"
    }

    if Method == "OPTION":
        return {
            "Accept": "*/*",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            **common_headers,
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Access-Control-Request-Method": Method,
            "Access-Control-Request-Headers": "authorization,content-type",
        }

    if Method == "POST":
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Authorization": f"Bearer {token}",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Priority": "u=4",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Referer": referer
        }
        return headers

    if Method == "GET":
        headers = {
            "Accept": "application/json",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            **common_headers,
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        return headers
