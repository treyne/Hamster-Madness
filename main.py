import time
import API.core as core
# import API.logger as logger
from API.logger import logger
import random
from datetime import datetime, timedelta, UTC





def main():
    while True:
        try:
            logger.info(f"[--------->Начата новая иттерация<---------]")
            IP = core.IP()
            logger.info(f"Ваш IP: <red>{IP['ip']}</red> | Country: <blue>{IP['country_code']}</blue> | City: <green>{IP['city_name']}</green>")
            AccountInfo = core.account_info()
            logger.info(f"Ваш аккаунт ID: <blue>{AccountInfo['accountInfo']['id']}</blue> | Name: <blue>{AccountInfo['accountInfo']['name']}</blue> | at: <blue>{AccountInfo['accountInfo']['at']}</blue>")
            season2_config_version,user = core.sync()

            logger.info(f"gamepads: <blue>{user['user']['profile']['gamepads']}</blue> | gamepads Toltal: <blue>{user['user']['profile']['gamepads_total']}</blue> | reputation: <blue>{user['user']['profile']['reputation']}</blue>")
            logger.info(f"soft money total: <fg #FFD700>{user['user']['profile']['soft_money_total']}</fg #FFD700> | soft money: <fg #FFD700>{user['user']['profile']['soft_money']}</fg #FFD700>")
            logger.info(f"hard money total: <fg #FFD700>{user['user']['profile']['hard_money_total']}</fg #FFD700> | hard money: <fg #FFD700>{user['user']['profile']['hard_money']}</fg #FFD700>")
            logger.info(f"Total Profit: <yellow>{user['user']['statistics']['totalProfit']}</yellow> | totalFun: <yellow>{user['user']['statistics']['totalFun']}</yellow>| totalGames: <yellow>{user['user']['statistics']['totalGames']}</yellow>")
            game_cfg = core.game_config(season2_config_version)
            if game_cfg:
                 logger.success(f"Файл конфигурации <green>{season2_config_version}.json</green> загружен")
            
            
            StartWork = core.command({"command":{"type":"StartWork"}}) #Пинаем программистов под зад!
            if StartWork[1] == 200:
                logger.success(f"Стартовали работу!")            
            
            
            
            # Тут настройки выбора игры
            set_genre = "Tycoon"
            set_setting = "Sports"
            

            current_genre = user['user']['game']['genre']
            logger.info(f"Текущий жанр <green>{current_genre}</green> ")
            gameName,iconId = core.select_game(game_cfg,set_setting,set_genre) #Сгенерировали имя игры и получили iconId
      
            try:
                for reward_data in user.get("user", {}).get("deferredRewards", []):
                    reward = reward_data.get("reward", {})
                    if reward.get("type") == "DeferredRewardGamesRelease":
                        totalGames = reward.get('totalGames')
                        totalFun = reward.get('totalFun')
                if totalGames > 0:
                    logger.success(f"Игр выпущено! {totalGames} шт | очков фана {totalFun}")
                    Released = core.command({"command":{"type":"ClaimReleasedGamesRewards"}}) #Собираем ништяки
                    if Released[1] == 200:
                        logger.success(f"Сбор ништяков произведён успешно!")
                        
                        # logger.success(f"{user['user']['deferredRewards'][0]['reward']['totalFunReward'][0]['type']}: <fg #FFD700>{user['user']['deferredRewards'][0]['reward']['totalFunReward'][0]['amount']}</fg #FFD700> | {user['user']['deferredRewards'][0]['reward']['totalFunReward'][1]['type']}: <fg #FFD700>{user['user']['deferredRewards'][0]['reward']['totalFunReward'][1]['amount']}</fg #FFD700> ")
                else:
                    logger.info(f"Собирать нечего. :)")
            except Exception as Err:
                logger.info(f"Собирать нечего. :)")

            


            #################################Тут работа с ежедневной наградой###########################################################       
            updated_at_str = user["user"]["counters"]["dailyRewardCounter"]["updatedAt"] # Получаем строку с датой
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=UTC) # Преобразуем её в объект datetime (указываем, что это UTC-время) 
            yesterday = (datetime.now(UTC) - timedelta(days=1)).date() # Определяем вчерашнюю дату в UTC

            # Проверяем, относится ли дата к вчерашнему дню
            if updated_at.date() == yesterday:
                logger.info(f"Стартуем получение ежедневной награды! ")
                ClaimDailyRewards = core.command({"command":{"type":"ClaimDailyRewards"}})
                if ClaimDailyRewards[1] == 200:  
                    logger.success(f"Получили ежедневную награду!")
                else:
                    logger.error(f"Не смогли получить ежндневную награду! Код ответа сервера: {ClaimDailyRewards[1]}")
                    logger.error(f"ответа сервера: {ClaimDailyRewards[0]}")
            else:
                logger.info(f"Ежедневная награда уже получена! | dailyRewardCounter.count = {user["user"]["counters"]["dailyRewardCounter"]["count"]} ")
            #################################Закончили работу с ежедневной наградой###########################################################
            

            
            
            ZoiPM = core.ZoiPM(set_genre,current_genre,iconId,set_setting,gameName)
            if ZoiPM == 200:
                logger.success(f"В разработку прияната игра: <blue>{gameName}</blue> | в жанре: <blue>{set_genre}</blue>")
                logger.debug(f"iconId: <blue>{iconId}</blue>")
                
            core.get_promos()
            

            dailyCiphers = core.dailyCiphers(game_cfg,user)                                
            if dailyCiphers[0] == 200:
                logger.success(f"Шифр успешно введён: <green>{dailyCiphers[1]}</green> ")
            else:
                logger.info(f"{dailyCiphers[0]}")
            print ("\n")
            
            # Тут будем собирать комбо
            
            
            core.countdown_timer(random.randint(197, 200),'До следующего логина: ')
            time.sleep(3)
        except Exception as error:
            print(f'Ошибка {error}')
            time.sleep(50)
            return main()

if __name__ == "__main__":
    main()



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
