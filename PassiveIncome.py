import httpx
import json
import time
import random
import os
import datetime
from dotenv import load_dotenv
import re
from datetime import datetime


# Загрузка переменных из .env файла
load_dotenv()
Bearer = os.getenv('Bearer')
DEBUG = True

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

import requests



def perform_options_request(url,Method):
    headers_opt = get_headers_opt(Method)  # Получаем заголовки OPTIONS запроса
    print (headers_opt)
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
                return response_json.get('accountInfo', {}).get('id')
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

    with httpx.Client(http2=True, timeout=10.0) as client:
        response = client.post(url, headers=headers_post, json={})

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
                debug_print('command JSON = ', response_json)
                return response_json
            except json.JSONDecodeError as e:
                debug_print("JSON decode error: ", e)
                return None
    except httpx.RequestError as e:
        debug_print(f"Ошибка сети: {e}")
        return None
    return None                


                # "genre": "Clicker",
				# "genre": "Runner",
				# "genre": "Puzzle",
				# "genre": "Arcade",
				# "genre": "Platformer",
				# "genre": "Tycoon",
				# "genre": "VisualNovel",
				# "genre": "Adventure",
				# "genre": "Shooter",
				# "genre": "Simulator",
				# "genre": "RPG",
				# "genre": "Match-3",
				# "genre": "Action",
				# "genre": "Strategy",
				# "genre": "Slots",
				# "genre": "MMORPG",
				# "genre": "VRgame",
				# "genre": "NFTGame"


def select_game(JSON,setting,genres):
    random_adjective = random.choice(JSON["config"]["gameAdjectives"])
    settings = JSON.get("config", {}).get("settings", [])
    for item in settings:
        if item.get("setting") == setting:
            names = item.get("names", [])
            iconId = (genres + "_" + item.get("iconId", [])).replace((genres + "_")[0], (genres + "_")[0].lower(), 1)
            if names and iconId:
                gameName = random_adjective + ' ' + random.choice(names)  # Выбираем случайное имя
    return gameName, iconId



def ZoiPM(set_genre,current_genre,iconId,set_setting,gameName):
    if current_genre == "Clicker":
        command({"command":{"type":"ChangeGameInDevelopment","genre":set_genre,"setting":set_setting,"name":gameName,"iconId":iconId}})
# {"command":{"type":"ChangeGameInDevelopment","genre":"Puzzle","setting":"Sports","name":"Super Tournament","iconId":"puzzle_sports"}}





           
        
        
# command({"command": {"type": "ApplyTaps", "progress": {"DEV": 400, "ART": 328, "GD": 377}, "funProgress": 101}}) #TAPS


def main():
    while True:
        try:
            IP()
            #account_info()
            set_genre = "Platformer"
            set_setting = "Sports"
            
            season2_config_version,user = sync()
            current_genre = user["user"]["game"]["genre"]
            game_cfg = game_config(season2_config_version)
            gameName,iconId = select_game(game_cfg,set_setting,set_genre)
            command({"command":{"type":"ClaimReleasedGamesRewards"}}) #Собираем ништяки
            print(f'iconId =  {iconId}                                        !!!!!!!!!!!!!!!!')
            ZoiPM(set_genre,current_genre,iconId,set_setting,gameName)
            # get_promos()
            countdown_timer(random.randint(180, 355),'До следующего логина: ')
            time.sleep(5)
        except Exception as error:
            print(f'Ошибка {error}')
            time.sleep(5)
            return main()

if __name__ == "__main__":
    main()
