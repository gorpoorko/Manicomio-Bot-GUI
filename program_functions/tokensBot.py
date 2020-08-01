
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]


from main import *
import sqlite3

import subprocess

def tokensBot(self):
    self.ui.inserir_token_bot.mousePressEvent = lambda a: self.ui.inserir_token_bot.clear()
    self.ui.inserir_canal_bot.mousePressEvent = lambda a: self.ui.inserir_canal_bot.clear()
    self.ui.inserir_id_pessoal_bot.mousePressEvent = lambda a: self.ui.inserir_id_pessoal_bot.clear()
    self.ui.inserir_id_backups.mousePressEvent = lambda a: self.ui.inserir_id_backups.clear()
    self.ui.inserir_token_dropbox.mousePressEvent = lambda a: self.ui.inserir_token_dropbox.clear()
    self.ui.inserir_token_giphy.mousePressEvent = lambda a: self.ui.inserir_token_giphy.clear()
    self.ui.inserir_token_yandex.mousePressEvent = lambda a: self.ui.inserir_token_yandex.clear()
    self.ui.inserir_token_weather.mousePressEvent = lambda a: self.ui.inserir_token_weather.clear()
    self.ui.inserir_token_imgur.mousePressEvent = lambda a: self.ui.inserir_token_imgur.clear()
    self.ui.inserir_token_bitly.mousePressEvent = lambda a: self.ui.inserir_token_bitly.clear()
    self.ui.inserir_id_google.mousePressEvent = lambda a: self.ui.inserir_id_google.clear()
    self.ui.inserir_key_google.mousePressEvent = lambda a: self.ui.inserir_key_google.clear()

    self.ui.botao_start_bot.clicked.connect(lambda: startBot(self))

def startBot(self):
    subprocess.Popen('python bot_files/bot.py')
    #recebe os textos das inputs dos tokens
    token_bot = self.ui.inserir_token_bot.text()
    id_canal = self.ui.inserir_canal_bot.text()
    id_pessoal = self.ui.inserir_id_pessoal_bot.text()
    id_backups = self.ui.inserir_id_backups.text()
    token_dropbox = self.ui.inserir_token_dropbox.text()
    token_giphy = self.ui.inserir_token_giphy.text()
    token_yandex = self.ui.inserir_token_yandex.text()
    token_weather = self.ui.inserir_token_weather.text()
    token_imgur = self.ui.inserir_token_imgur.text()
    token_bitly = self.ui.inserir_token_bitly.text()
    id_google= self.ui.inserir_id_google.text()
    key_google = self.ui.inserir_key_google.text()

    #conexao, gravação, reposição tokens database----->
    conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()

    try:
        cursor_sqlite.execute(f"""DELETE FROM tokens_bot;""")
        conexao_sqlite.commit()
        cursor_sqlite.execute(f"""INSERT INTO tokens_bot (int_id, token_bot, id_canal, id_pessoal, id_backups, token_dropbox, token_giphy,token_weather, token_imgur, token_yandex, token_bitly, id_google, key_google)VALUES(null,'{token_bot}','{id_canal}','{id_pessoal}','{id_backups}','{token_dropbox}','{token_giphy}','{token_weather}','{token_imgur}','{token_yandex}','{token_bitly}','{id_google}','{key_google}')""")
        conexao_sqlite.commit()
    except Exception as e:
        cursor_sqlite.execute(f"""INSERT INTO tokens_bot (int_id, token_bot, id_canal, id_pessoal, id_backups, token_dropbox, token_giphy,token_weather, token_imgur, token_yandex, token_bitly, id_google, key_google)VALUES(null,'{token_bot}','{id_canal}','{id_pessoal}','{id_backups}','{token_dropbox}','{token_giphy}','{token_weather}','{token_imgur}','{token_yandex}','{token_bitly}','{id_google}','{key_google}')""")
        conexao_sqlite.commit()
    conexao_sqlite.close()


