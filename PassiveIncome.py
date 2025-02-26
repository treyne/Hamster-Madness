import time
import API.core as core
import random






def main():
    while True:
        try:
            core.IP()
            core.account_info()
            season2_config_version,user = core.sync()
            game_cfg = core.game_config(season2_config_version)
            
            
            set_genre = "VisualNovel"
            set_setting = "Sports"
            current_genre = user["user"]["game"]["genre"]            
            gameName,iconId = core.select_game(game_cfg,set_setting,set_genre)
            core.command({"command":{"type":"ClaimReleasedGamesRewards"}}) #Собираем ништяки
            print(f'iconId =  {iconId}                                        !!!!!!!!!!!!!!!!')
            core.ZoiPM(set_genre,current_genre,iconId,set_setting,gameName)
            core.get_promos()
            

            core.dailyCiphers(game_cfg,user)                                
           
            
            
            core.countdown_timer(random.randint(180, 355),'До следующего логина: ')
            time.sleep(50)
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
