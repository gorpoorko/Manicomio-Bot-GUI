# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]


from main import *
import sqlite3
import subprocess
import os
import time

# database dos tokens, inserir tokens na database usando painel ou via CLI
conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT * FROM tokens_bot""")
tokens = cursor_sqlite.fetchall()
def tokensBot(self):

    if tokens != []:
        self.ui.inserir_token_bot.setText('token encontrado')
        self.ui.inserir_canal_bot.setText('token encontrado')
        self.ui.inserir_id_pessoal_bot.setText('token encontrado')
        self.ui.inserir_id_backups.setText('token encontrado')
        self.ui.inserir_token_dropbox.setText('token encontrado')
        self.ui.inserir_token_giphy.setText('token encontrado')
        self.ui.inserir_token_yandex.setText('token encontrado')
        self.ui.inserir_token_weather.setText('token encontrado')
        self.ui.inserir_token_imgur.setText('token encontrado')
        self.ui.inserir_token_bitly.setText('token encontrado')
        self.ui.inserir_id_google.setText('token encontrado')
        self.ui.inserir_key_google.setText('token encontrado')
        self.ui.botao_start_bot.clicked.connect(lambda: startBotYesToken(self))
    else:
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
        self.ui.botao_start_bot.clicked.connect(lambda: startBotNoToken(self))


def startBotYesToken(self):
    # exibe os tokens
    self.ui.inserir_token_bot.setText(tokens[0]['token_bot'])
    self.ui.inserir_canal_bot.setText(tokens[0]['id_canal'])
    self.ui.inserir_id_pessoal_bot.setText(tokens[0]['id_pessoal'])
    self.ui.inserir_id_backups.setText(tokens[0]['id_backups'])
    self.ui.inserir_token_dropbox.setText(tokens[0]['token_dropbox'])
    self.ui.inserir_token_giphy.setText(tokens[0]['token_giphy'])
    self.ui.inserir_token_yandex.setText(tokens[0]['token_yandex'])
    self.ui.inserir_token_weather.setText(tokens[0]['token_weather'])
    self.ui.inserir_token_imgur.setText(tokens[0]['token_imgur'])
    self.ui.inserir_token_bitly.setText(tokens[0]['token_bitly'])
    self.ui.inserir_id_google.setText(tokens[0]['id_google'])
    self.ui.inserir_key_google.setText(tokens[0]['key_google'])
    self.ui.botao_start_bot.setText('[ Bot Iniciado com Sucesso | Para mudar os tokens delete da database e reinicie ] ')
    self.ui.botao_start_bot.clicked.connect(lambda: self.processo_bot.terminate())
    self.ui.rodape_desenvolvedor.setText('AVISO: Para mudar tokens delete da database e reinicie o programa')
    conexao_sqlite.close()
    # inicia o bot
    self.processo_bot = subprocess.Popen('python bot_files/bot.py')


def startBotNoToken(self):
    # recebe os textos das inputs dos tokens
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
    id_google = self.ui.inserir_id_google.text()
    key_google = self.ui.inserir_key_google.text()
    if os.path.isfile('bot_files/arquivos/settings_gdrive.yaml') == False:
        # cria o arquivo settings_gdrive.yaml
        with open('bot_files/arquivos/settings_gdrive.yaml', 'w') as documento:
            settings_gdrive = f"""client_config_backend: settings
    client_config:
      client_id: {id_google}
      client_secret: {key_google}
    
    save_credentials: True
    save_credentials_backend: file
    save_credentials_file: credentials.json
    
    get_refresh_token: True
    
    oauth_scope:
      - https://www.googleapis.com/auth/drive.file
      - https://www.googleapis.com/auth/drive.install"""
            documento.write(settings_gdrive)
            documento.close()
    else:
        pass

    # conexao, gravação, reposição tokens database----->
    conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    try:
        cursor_sqlite.execute(f"""DELETE FROM tokens_bot;""")
        conexao_sqlite.commit()
        cursor_sqlite.execute(f"""INSERT INTO tokens_bot (int_id, token_bot, id_canal, id_pessoal, id_backups, token_dropbox, token_giphy,token_weather, token_imgur, token_yandex, token_bitly, id_google, key_google)VALUES(null,'{token_bot}','{id_canal}','{id_pessoal}','{id_backups}','{token_dropbox}','{token_giphy}','{token_weather}','{token_imgur}','{token_yandex}','{token_bitly}','{id_google}','{key_google}')""")
        conexao_sqlite.commit()
        conexao_sqlite.close()
    except:
        cursor_sqlite.execute(f"""INSERT INTO tokens_bot (int_id, token_bot, id_canal, id_pessoal, id_backups, token_dropbox, token_giphy,token_weather, token_imgur, token_yandex, token_bitly, id_google, key_google)VALUES(null,'{token_bot}','{id_canal}','{id_pessoal}','{id_backups}','{token_dropbox}','{token_giphy}','{token_weather}','{token_imgur}','{token_yandex}','{token_bitly}','{id_google}','{key_google}')""")
        conexao_sqlite.commit()

    #inicia o bot
    self.ui.botao_start_bot.setText('[ Bot Iniciado com Sucesso | Para mudar os tokens delete da database e reinicie ] ')
    self.processo_bot = subprocess.Popen('python bot_files/bot.py')