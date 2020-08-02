#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020
"""Anotações:

criar arquivo mainwindow.py:
    pyuic5 -x mainwindow.ui -o mainwindow.py

criar arquivo files_rc_rc.py
    pyrcc5 -o files_rc_rc.py files_rc.qrc


sempre que quisermos chamar um stackedWidget usamos o comando abaixo e mudar sua "indexação"
    self.ui.stackedWidget.setCurrentIndex(1)

usando o sistema para chamar os arquivos do layout:
    self.ui.string_do_objeto


Exemplo de layout limpo:
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    # --------------FUNÇÃO DE INICIO
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
"""

import sys
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QFileDialog, QWidget
from PyQt5 import QtSql, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainwindow import Ui_MainWindow
from program_functions import menus, database_reader, deepnude, tokensBot, funcoes_bot, settings_bot
import subprocess
from PIL import Image


class MainWindow(QMainWindow):

    # --------------FUNÇÃO DE INICIO
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.clic = pyqtSignal()
        # menus
        menus.menusJanela(self)
        # funções
        database_reader.funcoesBancodados(self)
        deepnude.deepNude(self)
        tokensBot.tokensBot(self)
        funcoes_bot.funcoesBot(self)
        settings_bot.settingsBot(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
