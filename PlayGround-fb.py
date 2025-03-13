

import json
from datetime import datetime, timedelta

def getCode(promo_id):
    print(f"Calling getCode() with promoId: {promo_id}")

# Входные данные
json_data = '''{"user":{"id":"7453211883","createdAt":"2025-02-24T18:09:05.382Z","promos":[{"promoId":"13f7bd7c-b4b3-41f1-9905-a7db2e814bff","rewardsTotal":1,"rewardsToday":1,"rewardsLastTime":"2025-03-03T12:56:35.931Z","lastPromoCodeLevel":0,"hashes":[3590644219]}]}}'''

data = json.loads(json_data)

# Текущая дата и время
now = datetime.utcnow()

# Проверяем каждую промо-акцию
for promo in data["user"]["promos"]:
    last_time = datetime.strptime(promo["rewardsLastTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if now - last_time > timedelta(hours=4) and promo["rewardsToday"] != 4:
        getCode(promo["promoId"])
