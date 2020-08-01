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


"""
#HEROKU CONFIG - rodar no heroku use as linhas abaixo------->
token = os.environ['TELEGRAM_TOKEN']
logs = os.environ['LOGS']
sudoers = os.environ['SUDOERS']
"""
import amanobot
import amanobot.aio
import asyncio
import os
import sqlite3















conexao_sqlite = sqlite3.connect('bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT * FROM tokens_bot""")
resultados = cursor_sqlite.fetchall()
print(resultados)



#-----------------
#LOCAL CONFIG rodar em local host use as linhas abaixo--->
token =  "1096480409:AAE6sg6eJZtH5Z_TEIzgq10SQtCvGf4KYSc"
logs = -1001402280935
sudoers = [522510051,]
backups_chat = 522510051  # Put a 0, False or None to disable ou seu id privado ou id privado de um canal ou grupo
keys = dict(
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  # https://here.com
    yandex = 'trnsl.1.1.20190811T184100Z.f3e1e6d6d3507525.7ea9c786af32b18cedeb125ca46cc2d9ee154e09',#https://tech.yandex.com/translate
    giphy = '7f6ws7EvslO9BuaAKie9BieyYnD3OkkT',    # https://developers.giphy.com
    token_dropbox = 's4rxVFP2mcAAAAAAAAC2eXinDL33K0tSIhnR1chqOmrtBPy-Dl6Ll0znnRP3Phm5',   #https://www.dropbox.com/developers/
    token_imgur = "ebfc2558bda96e5",        #https://api.imgur.com/oauth2/addclient
    token_bitly = ["a001cef9d44ed8083ed4d952d475e98079e60577", ],  #link?
)




#variaveis do bot essenciais
loop = asyncio.get_event_loop()
bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)
me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']


#horario de backup e git
backup_hours = ['15:56']
git_repo = ('https://github.com/gorpoorko/Manicomio-Bot-IA', 'master') #repositorio para upgrade do bot
max_time = 60
version = '7.0'

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
    'kibe',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'admins',
    'warns',
    'prints',
    'pypi',
    'weather',
    'youtube',
    'ping',
    'gif',
    'git',
    'reddit',
    'coub',
    'sudos',
    'ids',
    'ip',
    'jsondump',
    'dice',
    'misc',
    'tcxs',
    'hora_data',
    'trollagens',
    'randomicas',
    'calculadora',
    'users',
    'antiflood',
    'avatar',
    #sistemas web
    'dropbox_upload',
    'link_direto',
    'notepad_telegraph',
    'cria_site_telegraph',
    'qrcode',
    'gdrive_upload',
    #inteligencias---------->
    'inteligencia',
    'ia_privado_bot',
    'ia_mensagens_proibidas',
    'permanencia',
    'ia_cadastro_manual',
    'ia_cadastro_perguntas',
    'ia_corrige_palavras',
    'ia_crawler_sites',
    'ia_deepnude',
    'ia_reconhecimento',
    'ia_wikipedia',




]
