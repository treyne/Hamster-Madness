import httpx
import time
import random
import uuid
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import json
import API.core as core
from API.logger import logger


# Загрузка переменных из .env файла
load_dotenv()
Bearer = os.getenv('Bearer')
DEBUG = False
LOG_ON = False

# Импортируем функции для получения заголовков
from headers import get_headers_opt, get_headers_post

configurations = [
    {'app_token': 'ed526e8c-e6c8-40fd-b72a-9e78ff6a2054', 'promo_id': 'ed526e8c-e6c8-40fd-b72a-9e78ff6a2054','rnd1':'40','rnd2':'60','game':'Cooking Stories'}, 
    {'app_token': '8d1cc2ad-e097-4b86-90ef-7a27e19fb833', 'promo_id': 'dc128d28-c45b-411c-98ff-ac7726fbaea4','rnd1':'40','rnd2':'60','game':'Merge Away'},
    {'app_token': 'ab93d8d2-bd0b-47c9-98f6-e202f900b5df', 'promo_id': 'ab93d8d2-bd0b-47c9-98f6-e202f900b5df','rnd1':'40','rnd2':'60','game':'Draw To Smash'}, 
    {'app_token': 'd02fc404-8985-4305-87d8-32bd4e66bb16', 'promo_id': 'd02fc404-8985-4305-87d8-32bd4e66bb16','rnd1':'40','rnd2':'60','game':'Factory World'},         
    {'app_token': '13f7bd7c-b4b3-41f1-9905-a7db2e814bff', 'promo_id': '13f7bd7c-b4b3-41f1-9905-a7db2e814bff','rnd1':'40','rnd2':'60','game':'Merge Dale'},         
    {'app_token': 'e53b902b-d490-406f-9770-21a27fff1d31', 'promo_id': 'e53b902b-d490-406f-9770-21a27fff1d31','rnd1':'40','rnd2':'60','game':'Doodle God'},     
    {'app_token': 'bc72d3b9-8e91-4884-9c33-f72482f0db37', 'promo_id': 'bc72d3b9-8e91-4884-9c33-f72482f0db37','rnd1':'40','rnd2':'60','game':'Bouncemasters'},         
    {'app_token': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b', 'promo_id': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b','rnd1':'40','rnd2':'60','game':'Zoopolis'},     
    {'app_token': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71', 'promo_id': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71','rnd1':'40','rnd2':'60','game':'Polysphere'},     
    #{'app_token': 'd1690a07-3780-4068-810f-9b5bbf2931b2', 'promo_id': 'b4170868-cef0-424f-8eb9-be0622e8e8e3','rnd1':'20','rnd2':'30','game':'Chain Cube 2048'},     
    #{'app_token': '82647f43-3f87-402d-88dd-09a90025313f', 'promo_id': 'c4480ac7-e178-4973-8061-9ed5b2e17954','rnd1':'125','rnd2':'140','game':'Train Miner'},   
    #{'app_token': 'eb518c4b-e448-4065-9d33-06f3039f0fcb', 'promo_id': 'eb518c4b-e448-4065-9d33-06f3039f0fcb','rnd1':'100','rnd2':'122','game':'Infected Frontier'},  
    #{'app_token': '53bf823a-948c-48c4-8bd5-9c21903416df', 'promo_id': '53bf823a-948c-48c4-8bd5-9c21903416df','rnd1':'100','rnd2':'122','game':'Tower Defense'},    
    
]

def debug_print(*args):
    if DEBUG:
        print(*args)


def LOG(*args):
    if LOG_ON:
        current_time = datetime.now()
        file_name = f"PlayGround_{current_time.strftime('%d.%m.%Y_%H-%M')}.txt"
        try:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(' '.join(map(str, args)) + '\n')
        except Exception as e:
            print(f"Error writing to file: {e}")
 

def countdown_timer(seconds, text):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = text + " {:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print(' ' * len(timer), end='\r')


def generate_client_id():
    timestamp = int(time.time() * 1000)
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(19))
    return f"{timestamp}-{random_numbers}"


def login_client(app_token):
    client_id = generate_client_id()
    try:
        with httpx.Client(http2=True) as client:
            response = client.post('https://api.gamepromo.io/promo/login-client', json={
                'appToken': app_token,
                'clientId': client_id,
                'clientOrigin': 'android',
            }, headers={'Content-Type': 'application/json; charset=utf-8'})
            response.raise_for_status()
            data = response.json()
            logger.success(f"login-client [clientToken] =  {data['clientToken']}")
            return data['clientToken']
    except httpx.RequestError as error:
        print(f'Ошибка при входе клиента: {error}')
        LOG(f'Ошибка при входе клиента: {error}')
        countdown_timer(20, 'timer after login_client Error')
        return login_client(app_token)


def register_event(token, promo_id, delay):
    event_id = str(uuid.uuid4())
    try:
        with httpx.Client(http2=True) as client:
            response = client.post('https://api.gamepromo.io/promo/register-event', json={
                'promoId': promo_id,
                'eventId': event_id,
                'eventOrigin': 'undefined'
            }, headers={
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json; charset=utf-8',
            })
            response.raise_for_status()
            data = response.json()
            if not data.get('hasCode', False):
                countdown_timer(random.randint(delay[0], delay[1]), 'next try register_event')
                return register_event(token, promo_id, delay)
            return True
    except httpx.RequestError as error:
        print(f'Ошибка при register_event: {error}')
        LOG(f'Ошибка при register_event: {error}')
        countdown_timer(120, 'Задержка после ошибки register_event')
        return register_event(token, promo_id, delay)


def create_code(token, promo_id):
    while True:
        try:
            with httpx.Client(http2=True) as client:
                response = client.post('https://api.gamepromo.io/promo/create-code', json={
                    'promoId': promo_id
                }, headers={
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json; charset=utf-8',
                })
                response.raise_for_status()
                data = response.json()
                return data['promoCode']
        except httpx.RequestError as error:
            print(f'Ошибка при создании кода: {error}')
            countdown_timer(120, 'Задержка после ошибки создания кода')




def genCode(app_token):
    token = login_client(app_token)
    countdown_timer(random.randint(80, 100), 'wait for login')
    register_event(token, config['promo_id'], (int(config['rnd1']), int(config['rnd2'])))
    code_data = create_code(token, config['promo_id'])
    logger.success(f"Сгенерированный код для {config['game']}: {code_data}")
    return code_data

        


def TmZ(data):
    # Получаем текущую дату и время с UTC
    current_time = datetime.now(timezone.utc)

    # Находим самую раннюю дату rewardsLastTime
    earliest_reward_time = min(
        [datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc) 
         for promo in data["user"]["promos"]]
    )

    # Рассчитываем разницу во времени с текущей датой
    time_diff = current_time - earliest_reward_time

    # Если разница меньше 4 часов, считаем сколько нужно подождать до 4 часов и 15 минут
    if time_diff < timedelta(hours=4):
        wait_time = timedelta(hours=4, minutes=15) - time_diff
        wait_seconds = wait_time.total_seconds()
        wait_seconds = int(round(wait_seconds))
        # print(f"Нужно подождать: {wait_seconds} секунд.")
        return wait_seconds 
    else:
        print("Разница больше 4 часов = ", earliest_reward_time)
        return "10"





def checkTime(app_token,game):
    data,status = core.bitquest()
    if status == 200:
        try:
            logger.success(f"Данные BitQuest успешно получены!  | Ваш ID: {data['user']['id']}")
        except (KeyError, IndexError, TypeError) as e:
            logger.error(f"Данные BitQuest отсутствуют!  | Ошибка: {e}")
            return False
        
    current_time = datetime.now(timezone.utc)
    for promo in data["user"]["promos"]:
        rewardsToday = promo["rewardsToday"]
        
        last_time = datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        # Получаем дату вчерашнего дня
        yesterday = (current_time - timedelta(days=1)).date()

        # Проверяем, что last_time был вчера (в пределах того дня)
        if last_time.date() == yesterday:
            rewardsToday = 0
        
        if promo["promoId"] == app_token and rewardsToday < 4:
            last_time = datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
            if current_time - last_time > timedelta(hours=4):
                logger.info(f"КД для игры <fg #D8659E>{game}</fg #D8659E> прошло, ключей сегодня = {rewardsToday}")
                logger.info(f"Начинаю генерацию нового ключа...")
                Promo_code = genCode(app_token)
                url = "https://api.hamsterkombatgame.io/season2/command"
                countdown_timer(random.randint(10,30), 'Задержка перед вводом кода')
                resp,status = core.command({"command":{"type":"ApplyBitQuestPromoCode","promoCode":Promo_code}})
                if status == 200:
                    try:
                        logger.success(f"Промокод  <fg #00FFFF>{Promo_code}</fg #00FFFF> успешно введён! ")
                    except (KeyError, IndexError, TypeError) as e:
                        logger.error(f"Ошибка ввода промокода!  | err: {e}")
                        return False
                
                # print (resp)
            else:
                logger.info(f"Слишком рано для игры <fg #D8659E>{game}</fg #D8659E> ключей сегодня <fg #FFD700>{rewardsToday}</fg #FFD700>")
            break







PlayGround = True
while PlayGround:
    for config in configurations:
        # print(config['game'])
        checkTime(config['app_token'],config['game'])
        countdown_timer(5, 'Задержка кода')
    data,status = core.bitquest()    
    countdown_timer(TmZ(data), 'До следующего пака ключей')
        
  
    

