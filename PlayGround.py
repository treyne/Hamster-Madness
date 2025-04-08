import asyncio
import httpx
import random
import uuid
import os
import API.core as core
from datetime import datetime, timedelta, timezone
import json
from API.logger import logger
from API.http_client import HTTPClient



DEBUG = False
LOG_ON = False

configurations = [
    {'app_token': 'ed526e8c-e6c8-40fd-b72a-9e78ff6a2054', 'promo_id': 'ed526e8c-e6c8-40fd-b72a-9e78ff6a2054','rnd1':'80','rnd2':'120','game':'Cooking Stories'}, 
    {'app_token': '8d1cc2ad-e097-4b86-90ef-7a27e19fb833', 'promo_id': 'dc128d28-c45b-411c-98ff-ac7726fbaea4','rnd1':'80','rnd2':'120','game':'Merge Away'},
    {'app_token': 'ab93d8d2-bd0b-47c9-98f6-e202f900b5df', 'promo_id': 'ab93d8d2-bd0b-47c9-98f6-e202f900b5df','rnd1':'80','rnd2':'120','game':'Draw To Smash'}, 
    {'app_token': 'd02fc404-8985-4305-87d8-32bd4e66bb16', 'promo_id': 'd02fc404-8985-4305-87d8-32bd4e66bb16','rnd1':'80','rnd2':'120','game':'Factory World'},         
    {'app_token': '13f7bd7c-b4b3-41f1-9905-a7db2e814bff', 'promo_id': '13f7bd7c-b4b3-41f1-9905-a7db2e814bff','rnd1':'80','rnd2':'120','game':'Merge Dale'},         
    {'app_token': 'e53b902b-d490-406f-9770-21a27fff1d31', 'promo_id': 'e53b902b-d490-406f-9770-21a27fff1d31','rnd1':'80','rnd2':'120','game':'Doodle God'},     
    {'app_token': 'bc72d3b9-8e91-4884-9c33-f72482f0db37', 'promo_id': 'bc72d3b9-8e91-4884-9c33-f72482f0db37','rnd1':'80','rnd2':'120','game':'Bouncemasters'},         
    {'app_token': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b', 'promo_id': 'b2436c89-e0aa-4aed-8046-9b0515e1c46b','rnd1':'80','rnd2':'120','game':'Zoopolis'},     
    {'app_token': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71', 'promo_id': '2aaf5aee-2cbc-47ec-8a3f-0962cc14bc71','rnd1':'80','rnd2':'120','game':'Polysphere'},     
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

def generate_client_id():
    timestamp = int(datetime.now().timestamp() * 1000)
    random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(19))
    return f"{timestamp}-{random_numbers}"

async def login_client(app_token):
    client_id = generate_client_id()
    try:
        async with httpx.AsyncClient(http2=True, timeout=30) as client:
            response = await client.post(
                'https://api.gamepromo.io/promo/login-client',
                json={
                    'appToken': app_token,
                    'clientId': client_id,
                    'clientOrigin': 'android',
                },
                headers={'Content-Type': 'application/json; charset=utf-8'}
            )
            response.raise_for_status()
            data = response.json()
            logger.success(f"login-client [clientToken] =  {data['clientToken']}")
            return data['clientToken']
    except httpx.RequestError as error:
        LOG(f'Ошибка при входе клиента: {error}')
        await asyncio.sleep(20)
        return await login_client(app_token)

async def register_event(token, promo_id, delay):
    event_id = str(uuid.uuid4())
    try:
        async with httpx.AsyncClient(http2=True, timeout=30) as client:
            response = await client.post(
                'https://api.gamepromo.io/promo/register-event',
                json={'promoId': promo_id, 'eventId': event_id, 'eventOrigin': 'undefined'},
                headers={
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json; charset=utf-8',
                }
            )
            response.raise_for_status()
            data = response.json()
            if not data.get('hasCode', False):
                await asyncio.sleep(random.randint(delay[0], delay[1]))
                return await register_event(token, promo_id, delay)
            return True
    except httpx.RequestError as error:
        LOG(f'Ошибка при register_event: {error}')
        await asyncio.sleep(120)
        return await register_event(token, promo_id, delay)

async def create_code(token, promo_id):
    while True:
        try:
            async with httpx.AsyncClient(http2=True, timeout=30) as client:
                response = await client.post(
                    'https://api.gamepromo.io/promo/create-code',
                    json={'promoId': promo_id},
                    headers={
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json; charset=utf-8',
                    }
                )
                response.raise_for_status()
                data = response.json()
                return data['promoCode']
        except httpx.RequestError as error:
            print(f'Ошибка при создании кода: {error}')
            await asyncio.sleep(120)

async def genCode(config):
    token = await login_client(config['app_token'])
    await asyncio.sleep(random.randint(80, 100))
    await register_event(token, config['promo_id'], (int(config['rnd1']), int(config['rnd2'])))
    code_data = await create_code(token, config['promo_id'])
    logger.success(f"Сгенерированный код для {config['game']}: {code_data}")
    return code_data

def TmZ(data):
    current_time = datetime.now(timezone.utc)
    earliest_reward_time = min(
        [datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
         for promo in data["user"]["promos"]]
    )
    time_diff = current_time - earliest_reward_time
    if time_diff < timedelta(hours=4):
        wait_time = timedelta(hours=4, minutes=15) - time_diff
        return int(round(wait_time.total_seconds()))
    return 10

async def checkTime(config):
    BASE_URL = "https://api.hamsterkombatgame.io"
    
    client = HTTPClient("https://api.bitquest.games/",follow_redirects=True)
    status,bitquest = client.post("bitquest/sync",BitQuest=True)
    
    # status,bitquest = core.bitquest() 
    
    # client = HTTPClient("https://httpbin.org",follow_redirects=True)
    # status,bitquest = client.post("/post",BitQuest=True)
    print (bitquest)
    if status != 200:
        logger.error(f"Получение данных BitQuest провалено!  | статус ответа: {status}")
        return False

    try:
        logger.success(f"Данные BitQuest успешно получены!  | Ваш ID: {bitquest['user']['id']}")
    except (KeyError, IndexError, TypeError) as e:
        logger.error(f"Ошибка получения ID: {e}")
        return False

    current_time = datetime.now(timezone.utc)

    for promo in bitquest["user"]["promos"]:
        if promo["promoId"] != config["app_token"]:
            continue

        rewardsToday = promo["rewardsToday"]
        last_time = datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)
        yesterday = (current_time - timedelta(days=1)).date()

        if last_time.date() == yesterday:
            rewardsToday = 0

        if rewardsToday < 4:
            if current_time - last_time > timedelta(hours=4):
                logger.info(f"КД прошло, начинаю генерацию для {config['game']} (сегодня {rewardsToday})")
                promo_code = await genCode(config)
                await asyncio.sleep(random.randint(10, 30))
                client = HTTPClient(BASE_URL)
                status,ApplyBitQuestPromoCode = client.post("/season2/command",data={"command": {"type": "ApplyBitQuestPromoCode", "promoCode": promo_code}})
                if status == 200:
                    logger.success(f"Промокод {promo_code} успешно введён!")
                    return True
                else:
                    logger.error(f"Ошибка при вводе промокода {promo_code} | статус: {status} | ответ: {resp}")
                    return False
            else:
                logger.info(f"Рано для {config['game']} | введено сегодня: {rewardsToday}")
                return True
    return True

async def main():
    PlayGround = True
    while PlayGround:
        for config in configurations:
            logger.info(f"Обработка: {config['game']}")
            PlayGround = await checkTime(config)
            await asyncio.sleep(5)
            if not PlayGround:
                break
        if not PlayGround:
            break
            
            
        client = HTTPClient("https://api.bitquest.games/")
        status,bitquest = client.post("bitquest/sync",BitQuest=True)    
   
        wait_time = TmZ(bitquest)
        logger.info(f"Ожидание {wait_time} секунд до следующей попытки.")
        await asyncio.sleep(wait_time)

if __name__ == "__main__":
    asyncio.run(main())
