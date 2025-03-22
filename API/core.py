import httpx
import json
import time
import random
import os
import datetime
import re
from datetime import datetime
import base64
from bs4 import BeautifulSoup


from dotenv import load_dotenv
# Загрузка переменных из .env файла
load_dotenv()
Bearer = os.getenv('Bearer')
Bearer_BitQuest = os.getenv('Bearer_BitQuest')
DEBUG = False




# Импортируем функции для получения заголовков
from headers import get_headers_opt, get_headers_post

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




def perform_options_request(url,Method):
    headers_opt = get_headers_opt(Method)  # Получаем заголовки OPTIONS запроса
    try:
        with httpx.Client(http2=True, timeout=10.0) as client:
            response = client.options(url, headers=headers_opt)
        
        debug_print(f"Status Code: {response.status_code}")
        debug_print("Headers:")
        
        for header, value in response.headers.items():
            debug_print(f"{header}: {value}")
        
        if response.content:
            debug_print("\nResponse Body:")
            debug_print(response.text)
            debug_print("\n\n\n")
        
        return response.headers.get("season2-config-version")
    
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None



def account_info():
    url = f"{BASE_URL}/auth/account-info"
    perform_options_request(url,"POST")  # Выполняем OPTIONS-запрос
    headers_post = get_headers_post(Bearer)  # Получаем заголовки для POST-запроса
    try:
        with httpx.Client(http2=True, timeout=10.0) as client:
            response = client.post(url, headers=headers_post)
        
        debug_print(f"Status Code: {response.status_code}")
        
        if response.content:
            try:
                response_json = response.json()
                debug_print('account_info JSON = ', response_json)
                return response_json
            except json.JSONDecodeError as e:
                debug_print("JSON decode error: ", e)
                return None
    
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None

    return None


def game_config(season2_config_version):
    url = f"{BASE_URL}/season2/config/{season2_config_version}"
    perform_options_request(url, "GET")
    headers_post = get_headers_post(Bearer)  # Получаем заголовки GET запроса

    with httpx.Client(http2=True, timeout=10.0) as client:
        response = client.get(url, headers=headers_post)

    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('game_config JSON = ', response_json)
            return response_json
        except ValueError as e:  # JSONDecodeError -> ValueError в httpx
            debug_print("JSON decode error: ", e)
            return None
    return None




	
def sync():
    url = f"{BASE_URL}/season2/sync"
    perform_options_request(url, "POST")
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса

    with httpx.Client(http2=True, timeout=10.0) as client:
        response = client.post(url, headers=headers_post, json={})

    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('sync JSON = ', response_json)
            season2_config_version = response.headers.get('season2-config-version')  # Получаем значение из заголовков
            debug_print('season2-config-version: ', season2_config_version)
            return season2_config_version,response_json  # Возвращаем значение заголовка
        except ValueError as e:  # JSONDecodeError -> ValueError в httpx
            debug_print("JSON decode error: ", e)
            return None
    return None
    
    
 
def IP():
    url = f"{BASE_URL}/ip"
    perform_options_request(url,"GET")  # Выполняем OPTIONS-запрос
    headers_post = get_headers_post(Bearer)  # Получаем заголовки для GET-запроса
    try:
        with httpx.Client(http2=True, timeout=10.0) as client:
            response = client.get(url, headers=headers_post)
        debug_print(f"Status Code: {response.status_code}")
        if response.content:
            try:
                response_json = response.json()
                debug_print('IP JSON = ', response_json)
                return response_json
            except json.JSONDecodeError as e:
                debug_print("JSON decode error: ", e)
                return None
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None

    return None 
    
    
        
   
        

                
                
def get_promos():
    url = f"{BASE_URL}/season2/get-promos"
    perform_options_request(url, "POST")
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса
    
    
    headersO = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "application/json",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Authorization": "Bearer 1740550840408DqFBr7ekpd6N9l3gCyIcC02l6WR5jHcxj0wQfCx0anSa647ku1HMIrRUqmZsAfpJ7453211883",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }      

    
    
    
    with httpx.Client(http2=True, timeout=10.0) as client:
        response = client.post(url, headers=headersO,)

    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('get_promos = ', response_json)
            return response_json
        except ValueError as e:  # JSONDecodeError -> ValueError в httpx
            debug_print("JSON decode error: ", e)
            return None
    return None
                
                
                
           
def command(cmd):
    url = f"{BASE_URL}/season2/command"
    perform_options_request(url,"POST")  # Выполняем OPTIONS-запрос
    headers_post = get_headers_post(Bearer)  # Получаем заголовки для POST-запроса
    
    try:
        with httpx.Client(http2=True, timeout=10.0) as client:
            response = client.post(url, headers=headers_post, json=cmd)
        debug_print(f"Status Code: {response.status_code}")
        if response.content:
            try:
                response_json = response.json()
                # debug_print('command JSON = ', response_json)
                return response_json, response.status_code
            except json.JSONDecodeError as e:
                debug_print("JSON decode error: ", e)
                return None
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None
    return None                





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



def ZoiPM(set_genre,current_genre,iconId,set_setting,gameName):
    if current_genre == "Clicker":
        status = command({"command":{"type":"ChangeGameInDevelopment","genre":set_genre,"setting":set_setting,"name":gameName,"iconId":iconId}})
        return status[1]
    return None
# {"command":{"type":"ChangeGameInDevelopment","genre":"Puzzle","setting":"Sports","name":"Super Tournament","iconId":"puzzle_sports"}}




# def combos(cards):
    # command()
    # # user.combos TODO
    #{"command":{"type":"TryCardToDailyCombo","cardId":4}}
    # # {"command":{"type":"ClaimDailyCombo"}}
    # # {"command":{"type":"OpenLootboxes","count":1,"lootboxId":"lootbox1"}}
    # user.combos

           
        
# def taps():       
    # command()
# # command({"command": {"type": "ApplyTaps", "progress": {"DEV": 400, "ART": 328, "GD": 377}, "funProgress": 101}}) #TAPS TODO


# Apply PromoCode
# {"command":{"type":"ApplyBitQuestPromoCode","promoCode":"MERGE-L66X-WZNEY-YVGP6-WGH8"}}

# Task Daily


# OneTimeTask
# {"command":{"type":"CheckOneTimeTask","taskId":"youtube_global_s2_e19"}}
# {"command":{"type":"CheckOneTimeTask","taskId":"subscribe_telegram_group"}}



def dailyCiphers(game_cfg,user):
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
        status = command({"command":{"type":"ClaimDailyCipher","cipher":decoded_str}})  #Вводим шифр
        return status[1],decoded_str
    elif is_within_range:
        return "Шифр уже введён! Дальнейшие действия не требуются :3 ",decoded_str


    
    return decoded_str





def httpx_request(url, method, data=None,http2activ=True):
    """Отправляет HTTP-запрос с указанным методом и данными."""
    headers_post = get_headers_post(Bearer)  # Получаем заголовки
    try:
        with httpx.Client(http2=http2activ, timeout=10.0) as client:
            method_func = getattr(client, method.lower(), None)
            if method_func is None:
                debug_print(f"Ошибка: метод {method} не поддерживается")
                return None
            
            # Разные параметры для GET и остальных методов
            kwargs = {"headers": headers_post}
            if method.upper() == "GET":
                kwargs["params"] = data  # GET использует params
            else:
                kwargs["json"] = data  # Остальные методы используют json
            
            response = method_func(url, **kwargs)
            debug_print(f"Status Code: {response.status_code}")

            if response.content:
                try:
                    response_json = response.json()
                    debug_print("info =", response_json)
                    return response_json
                except json.JSONDecodeError as e:
                    debug_print("JSON decode error:", e)
                    return None
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None




def bitquest():

    url = "https://api.bitquest.games/bitquest/sync"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Authorization": f"Bearer {Bearer_BitQuest}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Priority": "u=4",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

    with httpx.Client(http2=True, follow_redirects=True) as client:
        response = client.post(url, headers=headers)
        # print(response.status_code)
        # print(response.text)
        return response.json(), response.status_code







def GetCombo():
    url = "https://gorodfactov.ru/hamster-gamedev-heroes-kombo/"
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен (HTTP 200)
        # print(response.text)  # Выводим содержимое ответа
    except httpx.HTTPStatusError as e:
        print(f"Ошибка HTTP: {e}")
    except httpx.RequestError as e:
        print(f"Ошибка запроса: {e}")
        

    html = response.text
    # html = '''<div class="dropshadowboxes-drop-shadow dropshadowboxes-lifted-both dropshadowboxes-rounded-corners dropshadowboxes-inside-and-outside-shadow" style="background-color:#FFFFFF;border-style:solid;border-width:2px;border-color:#DDDDDD;width:;padding:10px"><div><p><strong>Разработка — «Игровые кресла»<br>Разработка — «Индустриальный шпионаж»<br>Разработка — «Поехать на конференцию»</strong></p></div></div>'''

    soup = BeautifulSoup(html, 'html.parser')

    div_content = soup.find('div', class_='dropshadowboxes-drop-shadow')

    if div_content:
        text = div_content.get_text(strip=True, separator=' ')
        words_in_quotes = re.findall(r'«(.*?)»', text)
        print(words_in_quotes)
        
    cards = [
    {'id': '1', 'nameRussian': 'Игровые кресла'},
    {'id': '3', 'nameRussian': 'AI арт'},
    {'id': '5', 'nameRussian': 'Быстрый вай-фай'}, 
    {'id': '7', 'nameRussian': 'Игровая консоль'}, 
    {'id': '9', 'nameRussian': 'Трекинг времени'}, 
    {'id': '11', 'nameRussian': 'Пригласить ментора'}, 
    {'id': '13', 'nameRussian': 'Маскот студии'}, 
    {'id': '15', 'nameRussian': 'Локальные митапы'}, 
    {'id': '17', 'nameRussian': 'Индустриальный шпионаж'}, 
    {'id': '19', 'nameRussian': 'Уикенд геймджема'},  
    {'id': '21', 'nameRussian': 'Произнести речь'}, 
    {'id': '22', 'nameRussian': 'Поехать на конференцию'}, 
    {'id': '23', 'nameRussian': 'Разработать движок'}, 
    {'id': '24', 'nameRussian': 'Офисное спа'}, 
    {'id': '25', 'nameRussian': 'Быстрое прототипирование'}, 
    {'id': '26', 'nameRussian': 'Печеньки'}, 
    {'id': '27', 'nameRussian': 'R&D'}, 
    {'id': '28', 'nameRussian': 'Цифровой апельсин'}, 
    {'id': '29', 'nameRussian': 'Офисный шеф-повар'}, 
    {'id': '30', 'nameRussian': 'Быстрый рекрутинг'}, 
    {'id': '2', 'nameRussian': 'Реклама в своих играх'}, 
    {'id': '4', 'nameRussian': 'Начать стриминг'}, 
    {'id': '6', 'nameRussian': 'Лайки необходимы'}, 
    {'id': '8', 'nameRussian': 'Студийный подкаст'}, 
    {'id': '10', 'nameRussian': 'Реклама на билбордах'}, 
    {'id': '12', 'nameRussian': 'Распустить слухи'}, 
    {'id': '14', 'nameRussian': 'Открыть дискорд сервер'}, 
    {'id': '16', 'nameRussian': 'Утечка "прототипа"'}, 
    {'id': '18', 'nameRussian': 'Свой собственный магазин'}, 
    {'id': '20', 'nameRussian': 'Камео'},
    ]
 
    found_cards = {card['nameRussian']: card['id'] for card in cards if card['nameRussian'] in words_in_quotes}
    
    for name, card_id in found_cards.items():
        
        command({"command":{"type":"TryCardToDailyCombo","cardId":card_id}})
        logger.success(f"Карта : <blue>{name}</blue> была добавлена в комбо!)
        
        countdown_timer(7,'До следующей карты ')
        
        # print(f"{name}: {card_id}")

        
