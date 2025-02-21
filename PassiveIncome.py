import requests
import json
import base64
import time
import random
import os
import hashlib
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

def perform_options_request(url):
    headers_opt = get_headers_opt()  # Получаем заголовки OPTIONS запроса
    response = requests.options(url, headers=headers_opt)
    debug_print(f"Status Code: {response.status_code}")
    debug_print("Headers:")
    
    for header, value in response.headers.items():
        debug_print(f"{header}: {value}")
    
    if response.content:
        debug_print("\nResponse Body:")
        debug_print(response.content.decode('utf-8'))
        debug_print("\n\n\n")
    
    return response.headers.get("season2-config-version")


def account_info():
    url = f"{BASE_URL}/auth/account-info"
    perform_options_request(url)
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса с актуальным Bearer токеном
    response = requests.post(url, headers=headers_post)
    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('JSON = ', response_json)
            return response_json.get('accountInfo', {}).get('id')
        except json.JSONDecodeError as e:
            debug_print("JSON decode error: ", e)
            return None
    return None


def game_config(season2_config_version):
    url = f"{BASE_URL}/season2/config/{season2_config_version}"
    perform_options_request(url)
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса
    response = requests.post(url, headers=headers_post)
    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('game_config JSON = ', response_json) 
            return response_json.get('dailyKeysMiniGames', {}).get('Candles', {}).get('isClaimed'), response_json.get('dailyKeysMiniGames', {}).get('Candles', {}).get('startDate')
        except json.JSONDecodeError as e:
            debug_print("JSON decode error: ", e)
            return None
    return None




def sync():
    url = f"{BASE_URL}/season2/sync"
    url = "https://httpbin.org/post"
    url = "https://api.hamsterkombatgame.io/season2/fast-sync"
    # perform_options_request(url)
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса
    print (url)
    response = requests.post(url, headers=headers_post)
    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('sync JSON = ', response_json) 
            return response_json
        except json.JSONDecodeError as e:
            debug_print("JSON decode error: ", e)
            return None
    return None    
    
    
 
def IP():
    url = f"{BASE_URL}/ip"
    perform_options_request(url)
    headers_post = get_headers_post(Bearer)  # Получаем заголовки POST запроса
    response = requests.get(url, headers=headers_post)
    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('IP JSON = ', response_json) 
            return response_json
        except json.JSONDecodeError as e:
            debug_print("JSON decode error: ", e)
            return None
    return None        
    
    
        
   
        
def get_promos():
#-----------------------------------------------###OPTIONS###-----------------------------------------------#  
        resp = requests.options('https://api.hamsterkombatgame.io/season2/get-promos', 
        headers=get_headers_opt())
        print(f"get_promos [options] Status Code: {resp.status_code}")
        
        time.sleep(3)
#-----------------------------------------------###POST###-----------------------------------------------#     
        resp = requests.post('https://api.hamsterkombatgame.io/season2/get-promos', 
        headers=get_headers_post(Bearer))
        print(f"get_promos [post] Status Code: {resp.status_code}")
        if resp.content:
            try:
                response_json = resp.json()
                debug_print('get_promos JSON = ', response_json)
                return response_json
            except json.JSONDecodeError as e:
                debug_print("JSON decode error: ", e)
                
                
                
                
                

def nuxt():
    url = "https://season2.hamsterkombatgame.io/_nuxt/builds/meta/941a0d9c-941d-4925-a239-12803afe0d54.json"
    headers_nuxt = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://season2.hamsterkombatgame.io/",
    "Connection": "keep-alive",
    "Cookie": "initData=user%3D%257B%2522id%2522%253A7453211883%252C%2522first_name%2522%253A%2522Rainbow%2522%252C%2522last_name%2522%253A%2522Crash%2522%252C%2522username%2522%253A%2522Rainbow0crash%2522%252C%2522language_code%2522%253A%2522ru%2522%252C%2522allows_write_to_pm%2522%253Atrue%252C%2522photo_url%2522%253A%2522https%253A%255C%252F%255C%252Ft.me%255C%252Fi%255C%252Fuserpic%255C%252F320%255C%252FIhjCglrDTlqihRpcyQ2qrETF8SSpxa03mOLdVlMpmRi8u7JuK5DLIBoc20_nlm-P.svg%2522%257D%26chat_instance%3D-7519436474689938738%26chat_type%3Dsender%26auth_date%3D1740128652%26signature%3DNxclKzTe6_NIx532SYF4Ia8ZvtSlRKgMk9ii3a2w1JNtXF9DgkdvA2aCDIIVltrQKOuPq8afbzUyci0vqf8wAw%26hash%3Daceea4913c31310431a8436aea2fa9f2011781ee362defe56e879214e66aed8e",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=4",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
    }
    
    response = requests.get(url, headers=headers_nuxt)
    debug_print(f"Status Code: {response.status_code}")
    if response.content:
        try:
            response_json = response.json()
            debug_print('nuxt JSON = ', response_json) 
            return response_json
        except json.JSONDecodeError as e:
            debug_print("JSON decode error: ", e)
            return None
    return None        



           
        
        

    

def main():
    while True:
        try:
            # IP()
            # account_info()
            nuxt()
            season2_config_version = sync()
            # game_config(season2_config_version)
            # get_promos()
            # countdown_timer(random.randint(1800, 11000),'До следующего логина: ')
            time.sleep(50)
        except Exception as error:
            print(f'Ошибка {error}')
            time.sleep(5)
            return main()

if __name__ == "__main__":
    main()
