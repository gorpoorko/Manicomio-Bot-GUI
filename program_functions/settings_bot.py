#!/usr/bin/env python
# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020

from main import *
from bot_files.config import na_bot
from datetime import datetime
import os
import sqlite3
from PIL import  Image

def settingsBot(self):
    #database
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()
    #texto
    self.ui.aviso_banimento_automatico.setText('')
    self.ui.aviso_local_inteligencia.setText('')
    self.ui.aviso_frequencia_fala.setText('')
    #botoes
    self.ui.botao_carregar_database_configuracoes.clicked.connect(lambda: carregarDbSettings(self))
    self.ui.botao_fechar_database_configuracoes.clicked.connect(lambda: fecharDbSettings(self))
    self.ui.botao_ativa_banimento.clicked.connect(lambda: ativaBanimento(self))
    self.ui.botao_desativa_banimento.clicked.connect(lambda: desativaBanimento(self))
    self.ui.botao_inteligencia_local.clicked.connect(lambda: inteligenciaLocal(self))
    self.ui.botao_inteligencia_global.clicked.connect(lambda: inteligenciaGlobal(self))
    self.ui.botao_sair_grupo.clicked.connect(lambda: sairGrupo(self))
    self.ui.botao_banir_usuario.clicked.connect(lambda: banirUsuario(self))

    #slider
    self.ui.slider_frequencia_fala.valueChanged.connect(lambda: frequencia(self))





def fecharDbSettings(self):
    self.conexao_sqlite.close()

def carregarDbSettings(self):
    # database dos tokens, inserir tokens na database usando painel ou via CLI
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()
    self.cursor_sqlite.execute("""SELECT * FROM chats""")
    self.chats = self.cursor_sqlite.fetchall()
    self.todos_chats = []
    for chat in self.chats:
        self.chat = chat['chat_id']
        self.todos_chats.append(f'{self.chat}')
    self.ui.comboBox_configuracoes.addItems(self.todos_chats)
    self.conexao_sqlite.close()

def sairGrupo(self):
    self.id_grupo1 = self.ui.id_manual_configuracoes.text()
    print(self.id_grupo1)
    na_bot.leaveChat(int(self.id_grupo1))
    self.ui.id_manual_configuracoes.setText('sai do grupo')


def banirUsuario(self):
    try:
        na_bot.kickChatMember(self.ui.id_manual_configuracoes.text(),self.ui.id_usuario_ban.text())
    except:
        pass
    try:
        na_bot.kickChatMember(self.ui.comboBox_configuracoes.currentText(),self.ui.id_usuario_ban.text())
    except:
        pass
#893192395   #perplex para testes 1367451130




def frequencia(self):
    self.slider_frequencia = self.ui.slider_frequencia_fala.value()
    self.grupos_listado = self.ui.comboBox_configuracoes.currentText()
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()
    self.cursor_sqlite.execute("""SELECT * FROM frequencia; """)
    self.frequencias = self.cursor_sqlite.fetchall()
    try:
        self.comparar_vazio = []
        self.freq = list(self.frequencias)
        if self.freq == self.comparar_vazio:
            self.cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{self.grupos_listado}','{self.grupos_listado}','{self.slider_frequencia}')""")
            self.conexao_sqlite.commit()
        else:
            for self.frequencia in self.frequencias:  # loop em todos resultados da Database
                self.cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{self.grupos_listado}'""")
                self.conexao_sqlite.commit()
                self.cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{self.grupos_listado}','{self.grupos_listado}','{self.slider_frequencia}')""")
                self.conexao_sqlite.commit()
                self.conexao_sqlite.close()
            #envia mensagens e troca os textos
            if int(self.slider_frequencia) == 0:
                self.ui.aviso_frequencia_fala.setText('Frequencia 0: Mudo')
                na_bot.sendMessage(self.grupos_listado, f'🤖 `Frequencia alterada para {self.slider_frequencia}, estou mutado so irei reponder comandos cadastrados`','markdown')
            if int(self.slider_frequencia) == 1:
                self.ui.aviso_frequencia_fala.setText('Frequencia 1')
                na_bot.sendMessage(self.grupos_listado, f'🤖 `Frequencia alterada para {self.slider_frequencia}, vou tentar falar pouco`','markdown')
            if int(self.slider_frequencia) >= 2:
                self.ui.aviso_frequencia_fala.setText(f'Frequencia: {self.slider_frequencia}')
                na_bot.sendMessage(self.grupos_listado, f'🤖 `Frequencia alterada para {self.slider_frequencia}, vou falar bastante`\nCaso queira que eu pare de falar defina a frequencia: 0\n Para eu falar menos defina frequencia: 1','markdown')
            self.conexao_sqlite.close()
    except Exception as e:
        print(e)
        pass


def desativaBanimento(self):
    try:
        self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
        self.conexao_sqlite.row_factory = sqlite3.Row
        self.cursor_sqlite = self.conexao_sqlite.cursor()
        self.ui.aviso_banimento_automatico.setText('Desativado')
        self.grupos_listado = self.ui.comboBox_configuracoes.currentText()
        self.data = datetime.now().strftime('%d/%m/%Y %H:%M')
        # desativar sistema de cadastro assim evita o banimento
        self.cursor_sqlite.execute(f"""DELETE FROM banimento WHERE id_grupo='{self.grupos_listado}' """)
        self.cursor_sqlite.execute(f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'criado via programa','criado via programa','{self.grupos_listado}','bot','bot','{self.data}','0')""")
        self.conexao_sqlite.commit()
        self.conexao_sqlite.close()
        na_bot.sendMessage(self.grupos_listado,"`Sistema de Cadastramento Automático para Banimento:`***DESATIVADO***\nAgora todos usuários que entrarem no grupo não receberão uma data limite de permanencia automática, porém estes dados ainda podem ser inseridos manualmente para restringir a permanência do usuário no grupo, para mais informações consulte os menus /help",'markdown')
    except:
        pass


def ativaBanimento(self):
    try:
        self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
        self.conexao_sqlite.row_factory = sqlite3.Row
        self.cursor_sqlite = self.conexao_sqlite.cursor()
        self.ui.aviso_banimento_automatico.setText('Ativado')
        self.grupos_listado = self.ui.comboBox_configuracoes.currentText()
        self.data = datetime.now().strftime('%d/%m/%Y %H:%M')
        #ativar sistema de cadastro assim evita o banimento
        self.cursor_sqlite.execute(f"""DELETE FROM banimento WHERE id_grupo='{self.grupos_listado}' """)
        self.cursor_sqlite.execute(f"""INSERT INTO banimento (int_id, grupo, tipo_grupo, id_grupo, admin, id_admin, data, valor)VALUES(null,'criado via programa','criado via programa','{self.grupos_listado}','bot','bot','{self.data}','1')""")
        self.conexao_sqlite.commit()
        self.conexao_sqlite.close()
        na_bot.sendMessage(self.grupos_listado,"`Sistema de Cadastramento Automático para Banimento:`***ATIVO***\nAgora todos usuários que entrarem no grupo receberão uma data limite de permanencia, caso queira remover restriçao do usuário ou inserir mais dias de permanência consulte /help",'markdown')
    except Exception as e:
        print(e)


def inteligenciaLocal(self):
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()
    self.ui.aviso_local_inteligencia.setText('IA Local')
    self.grupos_listado = self.ui.comboBox_configuracoes.currentText()
    try:
        self.cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{self.grupos_listado}' """)
        self.cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'criado no programa{self.grupos_listado}','criado no programa','{self.grupos_listado}','bot','bot','bot program','IA','{datetime.now().strftime('%d/%m/%Y %H:%M')}','local')""")
        self.conexao_sqlite.commit()
        self.conexao_sqlite.close()
        na_bot.sendMessage(self.grupos_listado,f"`Inteligencia Artificial:`***Local***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
    except Exception as e:
        print(f'banco de dados inteligencia erro: {e}')


def inteligenciaGlobal(self):
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()
    self.ui.aviso_local_inteligencia.setText('IA Global')
    self.grupos_listado = self.ui.comboBox_configuracoes.currentText()
    try:
        self.cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{self.grupos_listado}' """)
        self.cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'criado no programa{self.grupos_listado}','criado no programa','{self.grupos_listado}','bot','bot','bot program','IA','{datetime.now().strftime('%d/%m/%Y %H:%M')}','global')""")
        self.conexao_sqlite.commit()
        self.conexao_sqlite.close()
        na_bot.sendMessage(self.grupos_listado,f"`Inteligencia Artificial:`***Global***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
    except Exception as e:
        print(f'banco de dados inteligencia erro: {e}')

