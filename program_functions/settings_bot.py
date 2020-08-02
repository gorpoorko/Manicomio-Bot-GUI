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
    self.conexao_sqlite = sqlite3.connect('bot_files/bot_database.db')
    self.conexao_sqlite.row_factory = sqlite3.Row
    self.cursor_sqlite = self.conexao_sqlite.cursor()

    self.ui.slider_banimento_automatico.valueChanged.connect(lambda: banimento(self))






def banimento(self):
    #self.ui.aviso_banimento_automatico.text('')
    self.slider_banimento = self.ui.slider_banimento_automatico.value()
    print(self.slider_banimento)
    #pass





def inteligencia(self):
    self.ui.aviso_local_inteligencia.text('')
    self.slider_inteligencia = self.ui.slider_local_inteligencia.value()
    pass




def frequencia(self):
    self.ui.aviso_frequencia_fala.text('')
    self.slider_frequencia = self.ui.slider_frequencia_fala.value()
    pass