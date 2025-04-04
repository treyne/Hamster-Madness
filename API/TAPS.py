import configparser
from API.http_client import HTTPClient
from API.logger import logger
import random
BASE_URL = "https://api.hamsterkombatgame.io"


#################################--->Код который будет использовать тапы<---###########################################################
logger.info(f"[--------->Тапы задействованы<---------]")
client = HTTPClient(BASE_URL)
Sync = client.post("/season2/fast-sync") #Первичная синхронизация
if FastSync[0]==200:
    logger.info(f"Использовано тапов: <red>{Sync[0]['user']['counters']['tapCounter']['count']}</red> | ")


# user.counters.tapCounter.count
########################################################################################################################################