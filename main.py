# :’-(    (つ﹏<。)

import configparser
import time
import API.core as core
# import API.logger as logger
from API.logger import logger
import random
from datetime import datetime, timedelta, UTC
from API.http_client import HTTPClient
from API import Combo






def main():
    # Получаем настройки 
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Чтение параметров из секции settings
    set_genre = config.get('settings', 'Genre')
    set_setting  = config.get('settings', 'Setting')
    TIME_LOGIN = config.getint('settings', 'TIME_LOGIN')

    APPLY_DAILY_CIPHER = config.getboolean('settings', 'APPLY_DAILY_CIPHER')
    APPLY_DAILY_REWARD = config.getboolean('settings', 'APPLY_DAILY_REWARD')    
    APPLY_PROMO_CODES = config.getboolean('settings', 'APPLY_PROMO_CODES') 
    APPLY_COMBO = config.getboolean('settings', 'APPLY_COMBO')    
    USE_TAPS = config.getboolean('settings', 'USE_TAPS')
 
    BASE_URL = "https://api.hamsterkombatgame.io"
    
    
    while True:
        # try:
        
            #################################--->Получаем данные об IP адресе<---###########################################################
            logger.info(f"[--------->Начата новая иттерация<---------]")
            client = HTTPClient(BASE_URL)
            status,IP = client.get("/ip")
            logger.info(f"Ваш IP: <red>{IP['ip']}</red> | Country: <blue>{IP['country_code']}</blue> | City: <green>{IP['city_name']}</green>")
            #################################--->/Получаем данные об IP адресе<---###########################################################
            
            
            
            
            #################################--->Получаем данные о аккаунте<---###########################################################
            client = HTTPClient(BASE_URL)
            status,AccountInfo = client.post("/auth/account-info")
            logger.info(f"Ваш аккаунт ID: <blue>{AccountInfo['accountInfo']['id']}</blue> | Name: <blue>{AccountInfo['accountInfo']['name']}</blue> | at: <blue>{AccountInfo['accountInfo']['at']}</blue>")
            #################################--->/Получаем данные о аккаунте<---###########################################################
            
            
            
            
            #################################--->Получаем данные синхронизации<---###########################################################
            client = HTTPClient(BASE_URL)
            status_code, user, season2_config_version = client.post("/season2/sync",data={},sync=True)
            logger.info(f"gamepads: <blue>{user['user']['profile']['gamepads']}</blue> | gamepads Toltal: <blue>{user['user']['profile']['gamepads_total']}</blue> | reputation: <blue>{user['user']['profile']['reputation']}</blue>")
            logger.info(f"soft money total: <fg #FFD700>{user['user']['profile']['soft_money_total']}</fg #FFD700> | soft money: <fg #FFD700>{user['user']['profile']['soft_money']}</fg #FFD700>")
            logger.info(f"hard money total: <fg #FFD700>{user['user']['profile']['hard_money_total']}</fg #FFD700> | hard money: <fg #FFD700>{user['user']['profile']['hard_money']}</fg #FFD700>")
            logger.info(f"Total Profit: <fg #FFD700>{user['user']['statistics']['totalProfit']}</fg #FFD700> | totalFun: <fg #FFD700>{user['user']['statistics']['totalFun']}</fg #FFD700>| totalGames: <fg #FFD700>{user['user']['statistics']['totalGames']}</fg #FFD700>")
            #################################--->/Получаем данные синхронизации<---###########################################################


            
            
            #################################--->Получаем файл конфигурации<---###########################################################
            client = HTTPClient(BASE_URL)
            game_cfg = client.get(f"/season2/config/{season2_config_version}")
            if game_cfg[0]==200 and game_cfg[1]:
                 logger.success(f"Файл конфигурации <green>{season2_config_version}.json</green> загружен")
            #################################--->/Получаем файл конфигурации<---###########################################################
            
            
            

            #################################--->Получаем данные о активных ивентах<---###########################################################
            client = HTTPClient(BASE_URL)
            GetActive_Events = client.get("/season2/get-active-events")
            # print(GetActive_Events)
            # Преобразуем строки в datetime объекты (без Z, так как это UTC)
            fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
            startTime = datetime.strptime(GetActive_Events[1][0]['startTime'], fmt)
            endTime = datetime.strptime(GetActive_Events[1][0]['endTime'], fmt)
            rewardReleaseTime = datetime.strptime(GetActive_Events[1][0]['rewardReleaseTime'], fmt)
            logger.info(f"event ID: <blue>{GetActive_Events[1][0]['eventId']}</blue> | startTime: <blue>{startTime}</blue> | endTime: <blue>{endTime}</blue> \n                                      rewardReleaseTime: <blue>{rewardReleaseTime}</blue>")
            ###############################################################################################################################            
            
            


            #################################--->Получаем данные о Leaderboard <---###########################################################
            client = HTTPClient(BASE_URL)
            leaderboard = client.post("/season2/get-top-of-leaderboard",data={f"eventId":GetActive_Events[1][0]['eventId']})
            # print (leaderboard)
            logger.info(f"Leaderboard! Ваша позиция <blue>{leaderboard[1]['position']}</blue> | Рейтинг: <blue>{leaderboard[1]['ratingParameter']}</blue>")
            ###############################################################################################################################





            #################################--->Получаем Bitquest action <---###########################################################
            client = HTTPClient(BASE_URL)
            BitQuest_action = client.get("/season2/bitquest-action")
            # print (BitQuest_action)
            #logger.info(f"Ваш аккаунт ID: <blue>{AccountInfo['accountInfo']['id']}</blue> | Name: <blue>{AccountInfo['accountInfo']['name']}</blue> | at: <blue>{AccountInfo['accountInfo']['at']}</blue>")
            ###############################################################################################################################



            #################################--->Получаем user event rewards <---###########################################################
            client = HTTPClient(BASE_URL)
            user_event_rewards = client.post("/season2/user-event-rewards",data={f"eventId":GetActive_Events[1][0]['eventId']})
            # print (user_event_rewards)
            logger.info(f"user event rewards - position: <blue>{user_event_rewards[1]['position']}</blue> | rewards: <blue>{user_event_rewards[1]['rewards']}</blue> | rewardsClaimed: <blue>{user_event_rewards[1]['rewardsClaimed']}</blue>")
            ###############################################################################################################################


            
            
            
            
            #################################--->Тут наша задача разбудить программистов<---###############################################
            client = HTTPClient(BASE_URL) #Пинаем программистов под зад!
            status,StartWork = client.post(f"/season2/command", data={"command":{"type":"StartWork"}})
            if status == 200:
                logger.success(f"Стартовали работу!")            
            ####################--->Можно организовать слежение времени от последнего логина но мне лень :D<---############################  
         
      
      
      
            #########################--->Проверка на наличие ништяков, надо допилить вывод информации в лог<---#############################
            try:
                for reward_data in user.get("user", {}).get("deferredRewards", []):
                    reward = reward_data.get("reward", {})
                    if reward.get("type") == "DeferredRewardGamesRelease":
                        totalGames = reward.get('totalGames')
                        totalFun = reward.get('totalFun')
                if totalGames > 0:
                    logger.success(f"Игр выпущено! {totalGames} шт | очков фана {totalFun}")
                    client = HTTPClient(BASE_URL)
                    Released = client.post(f"/season2/command", data={"command":{"type":"ClaimReleasedGamesRewards"}}) #Собираем ништяки
                    if Released[0] == 200:
                        logger.success(f"Сбор ништяков произведён успешно!")
                        
                        # logger.success(f"{user['user']['deferredRewards'][0]['reward']['totalFunReward'][0]['type']}: <fg #FFD700>{user['user']['deferredRewards'][0]['reward']['totalFunReward'][0]['amount']}</fg #FFD700> | {user['user']['deferredRewards'][0]['reward']['totalFunReward'][1]['type']}: <fg #FFD700>{user['user']['deferredRewards'][0]['reward']['totalFunReward'][1]['amount']}</fg #FFD700> ")
                else:
                    logger.info(f"Собирать нечего. :)")
            except Exception as Err:
                logger.info(f"Собирать нечего. :)")
            ##################################################################################################################################
            





           ###################################Тут работа с ежедневной наградой###########################################################
            if APPLY_DAILY_REWARD:
                updated_at_str = user["user"]["counters"]["dailyRewardCounter"]["updatedAt"] # Получаем строку с датой
                updated_at = datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=UTC) # Преобразуем её в объект datetime (указываем, что это UTC-время) 
                yesterday = (datetime.now(UTC) - timedelta(days=1)).date() # Определяем вчерашнюю дату в UTC
                # Проверяем, сколько прошло времени
                if updated_at.date() <= yesterday:
                    logger.info(f"Стартуем получение ежедневной награды! ")
                    client = HTTPClient(BASE_URL)
                    ClaimDailyRewards = client.post(f"/season2/command", data={"command":{"type":"ClaimDailyRewards"}})
                    if ClaimDailyRewards[0] == 200:  
                        logger.success(f"Получили ежедневную награду!")
                    else:
                        logger.error(f"Не смогли получить ежндневную награду! Код ответа сервера: {ClaimDailyRewards[0]}")
                        logger.error(f"ответа сервера: {ClaimDailyRewards[0]}")
                else:
                    logger.info(f"Ежедневная награда уже получена! | dailyRewardCounter.count = {user["user"]["counters"]["dailyRewardCounter"]["count"]} ")
            ##################################Закончили работу с ежедневной наградой###########################################################
            

            
            
            
            
            
            #########################--->А вот тут живёт Zoi которая подрабатывает PM'ом вместо Анны <---#############################
            #########################--->Работает 24/7 и заряжает те проекты которые ты укажешь <---#############################
            
            current_genre = user['user']['game']['genre']
            logger.info(f"Текущий жанр <green>{current_genre}</green> ")
            gameName,iconId = core.select_game(game_cfg[1],set_setting,set_genre) #Сгенерировали имя игры и получили iconId

            client = HTTPClient(BASE_URL)
            ZoiPM = client.post(f"/season2/command", data={"command":{"type":"ChangeGameInDevelopment","genre":set_genre,"setting":set_setting,"name":gameName,"iconId":iconId}})
            if ZoiPM[0] == 200:
                logger.success(f"В разработку прияната игра: <blue>{gameName}</blue> | в жанре: <blue>{set_genre}</blue>")
                logger.debug(f"iconId: <blue>{iconId}</blue>")
            #############################################################################################################################
                
                
                
                        
            
            
            
            
            #########################--->Декодирование и ввод шифра<---#############################
            if APPLY_DAILY_CIPHER:
                CipherStatus,decoded_Cipher = core.dailyCiphers(game_cfg[1],user)
                if CipherStatus and decoded_Cipher:
                    client = HTTPClient("https://api.hamsterkombatgame.io")
                    dailyCiphers = client.post(f"/season2/command", data={"command":{"type":"ClaimDailyCipher","cipher":decoded_Cipher}})  
                    if dailyCiphers[0] == 200:
                        logger.success(f"Шифр успешно введён: <green>{decoded_Cipher}</green> ")
                    else:
                        logger.info(f"{dailyCiphers[0]}")
                    print ("\n")               
            #########################################################################################
            
            
            
            
            
            
            #########################--->Тут будем мутить комбо<---#############################
            if APPLY_COMBO:
                Combo.GetCombo(user,game_cfg[1])
 
 
 
            core.countdown_timer(random.randint(TIME_LOGIN+5, TIME_LOGIN+10),'До следующего логина: ')
            time.sleep(3)
        # except Exception as error:
            # print(f'Ошибка {error}')
            time.sleep(50)
            


main()



      
