


import sqlite3
conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
#conexao_sqlite.row_factory = lambda cursor, row: row[0]
cursor_sqlite = conexao_sqlite.cursor()
cursor_sqlite.execute("""SELECT id_grupo, grupo FROM mensagens""")
tupla_grupo = cursor_sqlite.fetchall()

#print(tupla_grupo[0][0])

for tu in tupla_grupo:
    print(tu[0])

