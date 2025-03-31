import httpx
import json
import time
import random
import datetime
import re
from datetime import datetime
import base64

DEBUG = False
from headers import get_headers





BASE_URL = "https://api.hamsterkombatgame.io"

def countdown_timer(seconds, text):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = text + " {:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")  # Перезаписываем строку
        time.sleep(1)
        seconds -= 1
    # Очищаем строку после завершения
    print(' ' * len(timer), end='\r')



def debug_print(*args):
    if DEBUG:
        print(*args)







def select_game(JSON,setting,genres):
    random_adjective = random.choice(JSON["config"]["gameAdjectives"])
    settings = JSON.get("config", {}).get("settings", [])
    for item in settings:
        if item.get("setting") == setting:
            names = item.get("names", [])
            iconId = (genres + "_" + item.get("iconId", "")).lower()
            if names and iconId:
                gameName = random_adjective + ' ' + random.choice(names)  # Выбираем случайное имя
    return gameName, iconId








def dailyCiphers(game_cfg,user): #Если произойдёт какое то очко функция вернёт None
    encoded_str = game_cfg["config"]["dailyCiphers"][0]["cipherEncoded"] # Тут получаем кодированный шифр 
    # Удаляем четвертый символ с начала строки
    modified_str = encoded_str[:3] + encoded_str[4:]
    # Декодируем строку из base64
    decoded_bytes = base64.b64decode(modified_str)
    decoded_str = decoded_bytes.decode('utf-8')

    # Входные данные
    enableAt = game_cfg["config"]["dailyCiphers"][0]["toggle"]["enableAt"]
    disableAt = game_cfg["config"]["dailyCiphers"][0]["toggle"]["disableAt"]
    dailyCipherLastClaimed = user["user"]["dailyCipherLastClaimed"]

    # Преобразуем строки в datetime объекты (без Z, так как это UTC)
    fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
    enable_at_dt = datetime.strptime(enableAt, fmt)
    disable_at_dt = datetime.strptime(disableAt, fmt)
    claimed_dt = datetime.strptime(dailyCipherLastClaimed, fmt)

    # Проверяем, находится ли claimed_dt в пределах enableAt и disableAt
    is_within_range = enable_at_dt <= claimed_dt <= disable_at_dt

    if not is_within_range:
        return True,decoded_str
    elif is_within_range:
        return False,decoded_str
    return None










