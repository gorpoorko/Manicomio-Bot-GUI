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

def funcoesBot(self):
    self.ui.botao_receber_mensagens.clicked.connect(lambda: receberMensagens(self))
    self.ui.botao_enviar_mensagem.clicked.connect(lambda:enviarMensagens(self))
    self.ui.botao_fechar_db.clicked.connect(lambda: fecharDb(self))
    self.ui.botao_carregar_db.clicked.connect(lambda: carregarDb(self))
    self.ui.comboBox_grupos_bot.activated.connect(lambda: carregarGrupo(self))
    self.ui.botao_enviar_imagem_bot.clicked.connect(lambda: enviarImagem(self))
    self.ui.botao_enviar_video_bot.clicked.connect(lambda: enviarVideo(self))
    self.ui.botao_enviar_documento_bot.clicked.connect(lambda: enviarDocumento(self))
    self.ui.texto_enviar_mensagem.mousePressEvent = lambda a: self.ui.texto_enviar_mensagem.clear()
    #QlineEdit manda mensagem com o enter com facilidade - QText Edit so com botao
    self.ui.linha_mensagem.returnPressed.connect(lambda: enviarMensagens(self))
    self.ui.linha_mensagem.mousePressEvent = lambda a: self.ui.linha_mensagem.clear()

def eventFilter(self, obj, event):
    if event.type() == QtCore.QEvent.KeyPress and obj is self.text_box:
        if event.key() == QtCore.Qt.Key_Return and self.text_box.hasFocus():
            print('Enter pressed')
    return super().eventFilter(obj, event)

def fecharDb(self):
    self.conexao_sqlite.close()

def carregarDb(self):
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
    self.ui.comboBox_grupos_bot.addItems(self.todos_chats)


def carregarGrupo(self):
    self.grupos_listado = self.ui.comboBox_grupos_bot.currentText()
    #print(self.grupos_listado)
    conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    cursor_sqlite = conexao_sqlite.cursor()
    cursor_sqlite.execute("""SELECT id_grupo, grupo FROM mensagens""")
    tupla_grupo = cursor_sqlite.fetchall()
    gp_lst = []
    for tu in tupla_grupo:
        #print(tu[0])
        if tu[0] == self.grupos_listado:
            gp_lst.append(tu[1])
    self.ui.texto_enviar_mensagem.setText(f'Mensagens serão enviadas para: {gp_lst[0]}')
    self.ui.texto_enviar_mensagem.mousePressEvent = lambda a: self.ui.texto_enviar_mensagem.clear()


def enviarImagem(self):
    self.imagem_recebida = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('Manicômio | Enviar Imagem')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "MANICOMIO | ENVIO DE IMAGENS | Escolha sua imagem", "",
                                                  "All Files (*);;JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.ui.imagem_deepnude_normal.setPixmap(QtGui.QPixmap(fileName).scaled(800, 450,
                                                                                    QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            self.ui.imagem_deepnude_renderizada.setPixmap(
                QtGui.QPixmap('bot_files/images/temp.png').scaled(300, 450,
                                                                         QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            if fileName in self.imagem_recebida:
                self.imagem_recebida.clear()
            else:
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
                self.imagem_recebida.append(fileName)
                print(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        im1 = Image.open(self.imagem_recebida[0])
        # salva a imagem usando a extensao que quisermos
        im1 = im1.save("bot_files/arquivos/temp.jpg")
        na_bot.sendPhoto(self.grupos_listado, photo=open('bot_files/arquivos/temp.jpg','rb'))
        os.remove('bot_files/arquivos/temp.jpg')
    except Exception as e:
        print(e)







def enviarVideo(self):
    pass

def enviarDocumento(self):
    pass



def enviarMensagens(self):
    self.texto = self.ui.texto_enviar_mensagem.toPlainText()
    try:
        na_bot.sendMessage(self.grupos_listado, self.texto)
    except:
        pass







def receberMensagens(self):
    mbot = na_bot.getUpdates()
    for i in range(len(mbot)):
        try:
            grupo = f"https://t.me/{mbot[i]['message']['chat']['username']}"
        except:
            try:
                grupo = f"Secreto: {mbot[i]['message']['chat']['title']}"
            except:
                grupo = 'none'
            pass
        try:
            usuario = f"@{mbot[i]['message']['from']['username']}"
        except:
            try:
                usuario = f"@{mbot[i]['message']['from']['id']}({mbot[i]['message']['from']['first_name']})"
            except:
                usuario = 'não reconhecido'
            pass
        try:
            mensagem = mbot[i]['message']['text']
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            infos_compiladas =  f'🧙{usuario.center(10)} 💀{grupo.center(15)}  📆{data.center(10)}\n💬{mensagem}\r'
            #print("X" + s.center(10) + "X")
            print(infos_compiladas)
            self.ui.mensagens_recebidas.append(infos_compiladas)
        except Exception as e:
            print(e)
            pass