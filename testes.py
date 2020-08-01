import sqlite3

conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT * FROM tokens_bot""")
tokens= cursor_sqlite.fetchall()

token_bot = tokens[0]['token_bot']
id_canal = tokens[0]['id_canal']
id_pessoal = tokens[0]['id_pessoal']
id_backups = tokens[0]['id_backups']
token_dropbox = tokens[0]['token_dropbox']
token_giphy = tokens[0]['token_giphy']
token_weather = tokens[0]['token_weather']
token_imgur = tokens[0]['token_imgur']
token_yandex = tokens[0]['token_yandex']
token_bitly = tokens[0]['token_bitly']




