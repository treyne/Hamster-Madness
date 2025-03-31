from API.http_client import HTTPClient
from bs4 import BeautifulSoup
import re
from API.logger import logger
import requests
import time



def GetCombo(user,game_cfg):
    BASE_URL = "https://api.hamsterkombatgame.io"
    url_combo = "https://gorodfactov.ru/hamster-gamedev-heroes-kombo/"

    request_gorodfactov = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Referer": "https://github.com/treyne/",
    }

    response = requests.get(url_combo, headers=request_gorodfactov)

    if response.status_code == 200:
        print("Запрос успешен!")
        # print(response.text)  # Вывод HTML-кода страницы
        HTML = response.text
    else:
        print(f"Ошибка: {response.status_code}")

    # print (HTML)
    soup = BeautifulSoup(HTML, 'html.parser')

    div_content = soup.find('p', class_='has-pale-cyan-blue-background-color has-background')
    # print (div_content)
    try:
        text = div_content.get_text(strip=True, separator=' ')
        words_in_quotes = re.findall(r"(?:Разработка|Маркетинг) —\s*[«\"]?(.*?)[»\"]?(?=\s*(?:Разработка|Маркетинг) —|$)", text)
        print(words_in_quotes)
        # result = [" ".join(matches)]
        # print(result)



    except Exception as e:
        print(f"Произошла какая то ебота:{e}")
        
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
        client = HTTPClient(BASE_URL) #Пинаем программистов под зад!
        TryCardToDailyCombo = client.post(f"/season2/command", data={'command': {'type': 'TryCardToDailyCombo', 'cardId':int(card_id)}})
        try:
            if TryCardToDailyCombo[0] == 200:
                logger.success(f"Карта : <blue>{name}</blue> была добавлена в комбо! id карты: {card_id}")
                time.sleep(7)
            else:     
                logger.error(f"Карта : <blue>{name}</blue> не добавлена в комбо! :( ")
                logger.error(f"ответ сервера : {TryCardToDailyCombo[1]}, код ответа:{TryCardToDailyCombo[0]}")
                time.sleep(10)
            
        except Exception as e:
            logger.error(f"Карта : <blue>{name}</blue> не добавлена в комбо! Что то пошло не так:{e} ")
            time.sleep(20)
            break
    client = HTTPClient(BASE_URL)         
    ClaimDailyCombo = client.post(f"/season2/command", data={"command":{"type":"ClaimDailyCombo"}})
    return None









