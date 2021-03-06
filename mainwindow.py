# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(726, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("program_functions/images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.barra_superior = QtWidgets.QFrame(self.centralwidget)
        self.barra_superior.setMinimumSize(QtCore.QSize(0, 50))
        self.barra_superior.setMaximumSize(QtCore.QSize(16777215, 50))
        self.barra_superior.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.barra_superior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barra_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_superior.setObjectName("barra_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.barra_superior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_logo = QtWidgets.QFrame(self.barra_superior)
        self.frame_logo.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_logo.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_logo.setStyleSheet("image: url(:/logo_manicomio/program_functions/images//logo_manicomio.png);")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_2.addWidget(self.frame_logo)
        self.frame_botoes = QtWidgets.QFrame(self.barra_superior)
        self.frame_botoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes.setObjectName("frame_botoes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_botoes)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.espacador_topo = QtWidgets.QFrame(self.frame_botoes)
        self.espacador_topo.setMinimumSize(QtCore.QSize(250, 0))
        self.espacador_topo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.espacador_topo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.espacador_topo.setObjectName("espacador_topo")
        self.horizontalLayout_3.addWidget(self.espacador_topo)
        self.botao_home = QtWidgets.QPushButton(self.frame_botoes)
        self.botao_home.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_home.setStyleSheet("QPushButton {\n"
"    background-image: url(:/home/program_functions/images//home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_home.setText("")
        self.botao_home.setObjectName("botao_home")
        self.horizontalLayout_3.addWidget(self.botao_home)
        self.botao_bot = QtWidgets.QPushButton(self.frame_botoes)
        self.botao_bot.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_bot.setStyleSheet("QPushButton {\n"
"background-image: url(:/bot/program_functions/images//telegram.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>80</x>\n"
"     <y>0</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QPushButton {\n"
"    background-image: url(:/home/program_functions/images//home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.botao_bot.setText("")
        self.botao_bot.setObjectName("botao_bot")
        self.horizontalLayout_3.addWidget(self.botao_bot)
        self.botao_database = QtWidgets.QPushButton(self.frame_botoes)
        self.botao_database.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_database.setStyleSheet("QPushButton {\n"
"background-image: url(:/banco de dados/program_functions/images//data-configuration-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>80</x>\n"
"     <y>0</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QPushButton {\n"
"    background-image: url(:/home/program_functions/images//home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.botao_database.setText("")
        self.botao_database.setObjectName("botao_database")
        self.horizontalLayout_3.addWidget(self.botao_database)
        self.botao_deepnude = QtWidgets.QPushButton(self.frame_botoes)
        self.botao_deepnude.setMinimumSize(QtCore.QSize(0, 50))
        self.botao_deepnude.setStyleSheet("QPushButton {\n"
"background-image: url(:/deepnude/program_functions/images//icons8-bottom-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>80</x>\n"
"     <y>0</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QPushButton {\n"
"    background-image: url(:/home/program_functions/images//home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.botao_deepnude.setText("")
        self.botao_deepnude.setObjectName("botao_deepnude")
        self.horizontalLayout_3.addWidget(self.botao_deepnude)
        self.botao_config = QtWidgets.QPushButton(self.frame_botoes)
        self.botao_config.setMinimumSize(QtCore.QSize(50, 50))
        self.botao_config.setStyleSheet("QPushButton {\n"
"background-image: url(:/configuracoes/program_functions/images//services-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>80</x>\n"
"     <y>0</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QPushButton {\n"
"    background-image: url(:/home/program_functions/images//home-5-24.png);\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.botao_config.setText("")
        self.botao_config.setObjectName("botao_config")
        self.horizontalLayout_3.addWidget(self.botao_config)
        self.horizontalLayout_2.addWidget(self.frame_botoes)
        self.verticalLayout.addWidget(self.barra_superior)
        self.palco_central = QtWidgets.QFrame(self.centralwidget)
        self.palco_central.setStyleSheet("background-color: rgb(31,31,31);")
        self.palco_central.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.palco_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.palco_central.setObjectName("palco_central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.palco_central)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.palco_central)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_home = QtWidgets.QWidget()
        self.pagina_home.setStyleSheet("")
        self.pagina_home.setObjectName("pagina_home")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pagina_home)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.banner_home = QtWidgets.QFrame(self.pagina_home)
        self.banner_home.setMinimumSize(QtCore.QSize(0, 330))
        self.banner_home.setAutoFillBackground(False)
        self.banner_home.setStyleSheet("background-image: url(:/background/program_functions/images//bg_home.jpg);\n"
"background-color: rgb(0, 0, 0);\n"
"background-position: center center;\n"
"background-repeat: no-repeat;\n"
"background-attachment: fixed;\n"
"background-size: cover;")
        self.banner_home.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.banner_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.banner_home.setObjectName("banner_home")
        self.verticalLayout_2.addWidget(self.banner_home)
        self.frame_configs_bot = QtWidgets.QFrame(self.pagina_home)
        self.frame_configs_bot.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_configs_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_configs_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_configs_bot.setObjectName("frame_configs_bot")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_configs_bot)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_dados_bot = QtWidgets.QFrame(self.frame_configs_bot)
        self.frame_dados_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_dados_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dados_bot.setObjectName("frame_dados_bot")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_dados_bot)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.inserir_token_bot = QtWidgets.QLineEdit(self.frame_dados_bot)
        self.inserir_token_bot.setMinimumSize(QtCore.QSize(0, 30))
        self.inserir_token_bot.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_bot.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_bot.setClearButtonEnabled(False)
        self.inserir_token_bot.setObjectName("inserir_token_bot")
        self.verticalLayout_6.addWidget(self.inserir_token_bot)
        self.inserir_canal_bot = QtWidgets.QLineEdit(self.frame_dados_bot)
        self.inserir_canal_bot.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_canal_bot.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_canal_bot.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_canal_bot.setClearButtonEnabled(False)
        self.inserir_canal_bot.setObjectName("inserir_canal_bot")
        self.verticalLayout_6.addWidget(self.inserir_canal_bot)
        self.inserir_id_pessoal_bot = QtWidgets.QLineEdit(self.frame_dados_bot)
        self.inserir_id_pessoal_bot.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_id_pessoal_bot.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_id_pessoal_bot.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_id_pessoal_bot.setClearButtonEnabled(False)
        self.inserir_id_pessoal_bot.setObjectName("inserir_id_pessoal_bot")
        self.verticalLayout_6.addWidget(self.inserir_id_pessoal_bot)
        self.inserir_id_backups = QtWidgets.QLineEdit(self.frame_dados_bot)
        self.inserir_id_backups.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_id_backups.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_id_backups.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_id_backups.setClearButtonEnabled(False)
        self.inserir_id_backups.setObjectName("inserir_id_backups")
        self.verticalLayout_6.addWidget(self.inserir_id_backups)
        self.horizontalLayout_5.addWidget(self.frame_dados_bot)
        self.frame_tokens = QtWidgets.QFrame(self.frame_configs_bot)
        self.frame_tokens.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_tokens.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tokens.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tokens.setObjectName("frame_tokens")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_tokens)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.inserir_token_dropbox = QtWidgets.QLineEdit(self.frame_tokens)
        self.inserir_token_dropbox.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_dropbox.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_dropbox.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_dropbox.setClearButtonEnabled(False)
        self.inserir_token_dropbox.setObjectName("inserir_token_dropbox")
        self.verticalLayout_5.addWidget(self.inserir_token_dropbox)
        self.inserir_token_giphy = QtWidgets.QLineEdit(self.frame_tokens)
        self.inserir_token_giphy.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_giphy.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_giphy.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_giphy.setClearButtonEnabled(False)
        self.inserir_token_giphy.setObjectName("inserir_token_giphy")
        self.verticalLayout_5.addWidget(self.inserir_token_giphy)
        self.inserir_token_bitly = QtWidgets.QLineEdit(self.frame_tokens)
        self.inserir_token_bitly.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_bitly.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_bitly.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_bitly.setClearButtonEnabled(False)
        self.inserir_token_bitly.setObjectName("inserir_token_bitly")
        self.verticalLayout_5.addWidget(self.inserir_token_bitly)
        self.inserir_id_google = QtWidgets.QLineEdit(self.frame_tokens)
        self.inserir_id_google.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_id_google.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_id_google.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_id_google.setClearButtonEnabled(False)
        self.inserir_id_google.setObjectName("inserir_id_google")
        self.verticalLayout_5.addWidget(self.inserir_id_google)
        self.horizontalLayout_5.addWidget(self.frame_tokens)
        self.frame_2 = QtWidgets.QFrame(self.frame_configs_bot)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.inserir_token_weather = QtWidgets.QLineEdit(self.frame_2)
        self.inserir_token_weather.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_weather.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_weather.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_weather.setClearButtonEnabled(False)
        self.inserir_token_weather.setObjectName("inserir_token_weather")
        self.verticalLayout_11.addWidget(self.inserir_token_weather)
        self.inserir_token_imgur = QtWidgets.QLineEdit(self.frame_2)
        self.inserir_token_imgur.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_imgur.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_imgur.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_imgur.setClearButtonEnabled(False)
        self.inserir_token_imgur.setObjectName("inserir_token_imgur")
        self.verticalLayout_11.addWidget(self.inserir_token_imgur)
        self.inserir_token_yandex = QtWidgets.QLineEdit(self.frame_2)
        self.inserir_token_yandex.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_token_yandex.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_token_yandex.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_token_yandex.setClearButtonEnabled(False)
        self.inserir_token_yandex.setObjectName("inserir_token_yandex")
        self.verticalLayout_11.addWidget(self.inserir_token_yandex)
        self.inserir_key_google = QtWidgets.QLineEdit(self.frame_2)
        self.inserir_key_google.setMinimumSize(QtCore.QSize(0, 20))
        self.inserir_key_google.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 13px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.inserir_key_google.setAlignment(QtCore.Qt.AlignCenter)
        self.inserir_key_google.setClearButtonEnabled(False)
        self.inserir_key_google.setObjectName("inserir_key_google")
        self.verticalLayout_11.addWidget(self.inserir_key_google)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame_configs_bot)
        self.botao_start_bot = QtWidgets.QPushButton(self.pagina_home)
        self.botao_start_bot.setMinimumSize(QtCore.QSize(0, 30))
        self.botao_start_bot.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_start_bot.setObjectName("botao_start_bot")
        self.verticalLayout_2.addWidget(self.botao_start_bot)
        self.stackedWidget.addWidget(self.pagina_home)
        self.pagina_bot = QtWidgets.QWidget()
        self.pagina_bot.setObjectName("pagina_bot")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pagina_bot)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_entradas_bot = QtWidgets.QFrame(self.pagina_bot)
        self.frame_entradas_bot.setMaximumSize(QtCore.QSize(16777215, 180))
        self.frame_entradas_bot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_entradas_bot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_entradas_bot.setObjectName("frame_entradas_bot")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_entradas_bot)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_botoes_enviar = QtWidgets.QFrame(self.frame_entradas_bot)
        self.frame_botoes_enviar.setStyleSheet("border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.frame_botoes_enviar.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_botoes_enviar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes_enviar.setObjectName("frame_botoes_enviar")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_botoes_enviar)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_grupos_bot = QtWidgets.QComboBox(self.frame_botoes_enviar)
        self.comboBox_grupos_bot.setStyleSheet("QComboBox {\n"
"background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QComboBox:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.comboBox_grupos_bot.setObjectName("comboBox_grupos_bot")
        self.comboBox_grupos_bot.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_grupos_bot)
        self.botao_enviar_imagem_bot = QtWidgets.QPushButton(self.frame_botoes_enviar)
        self.botao_enviar_imagem_bot.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_enviar_imagem_bot.setObjectName("botao_enviar_imagem_bot")
        self.verticalLayout_7.addWidget(self.botao_enviar_imagem_bot)
        self.botao_enviar_video_bot = QtWidgets.QPushButton(self.frame_botoes_enviar)
        self.botao_enviar_video_bot.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_enviar_video_bot.setObjectName("botao_enviar_video_bot")
        self.verticalLayout_7.addWidget(self.botao_enviar_video_bot)
        self.botao_enviar_documento_bot = QtWidgets.QPushButton(self.frame_botoes_enviar)
        self.botao_enviar_documento_bot.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_enviar_documento_bot.setObjectName("botao_enviar_documento_bot")
        self.verticalLayout_7.addWidget(self.botao_enviar_documento_bot)
        self.horizontalLayout_4.addWidget(self.frame_botoes_enviar)
        self.frame_enviar_mensagem = QtWidgets.QFrame(self.frame_entradas_bot)
        self.frame_enviar_mensagem.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_enviar_mensagem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_enviar_mensagem.setObjectName("frame_enviar_mensagem")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_enviar_mensagem)
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_4 = QtWidgets.QFrame(self.frame_enviar_mensagem)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.botao_carregar_db = QtWidgets.QPushButton(self.frame_4)
        self.botao_carregar_db.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_carregar_db.setObjectName("botao_carregar_db")
        self.horizontalLayout_9.addWidget(self.botao_carregar_db)
        self.botao_fechar_db = QtWidgets.QPushButton(self.frame_4)
        self.botao_fechar_db.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_fechar_db.setObjectName("botao_fechar_db")
        self.horizontalLayout_9.addWidget(self.botao_fechar_db)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.texto_enviar_mensagem = QtWidgets.QTextEdit(self.frame_enviar_mensagem)
        self.texto_enviar_mensagem.setMaximumSize(QtCore.QSize(16777215, 250))
        self.texto_enviar_mensagem.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.texto_enviar_mensagem.setObjectName("texto_enviar_mensagem")
        self.verticalLayout_8.addWidget(self.texto_enviar_mensagem)
        self.botao_enviar_mensagem = QtWidgets.QPushButton(self.frame_enviar_mensagem)
        self.botao_enviar_mensagem.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_enviar_mensagem.setObjectName("botao_enviar_mensagem")
        self.verticalLayout_8.addWidget(self.botao_enviar_mensagem)
        self.horizontalLayout_4.addWidget(self.frame_enviar_mensagem)
        self.verticalLayout_3.addWidget(self.frame_entradas_bot)
        self.frame_mensagens_recebidas = QtWidgets.QFrame(self.pagina_bot)
        self.frame_mensagens_recebidas.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_mensagens_recebidas.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.frame_mensagens_recebidas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mensagens_recebidas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mensagens_recebidas.setObjectName("frame_mensagens_recebidas")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_mensagens_recebidas)
        self.verticalLayout_9.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.linha_mensagem = QtWidgets.QLineEdit(self.frame_mensagens_recebidas)
        self.linha_mensagem.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.linha_mensagem.setObjectName("linha_mensagem")
        self.verticalLayout_9.addWidget(self.linha_mensagem)
        self.botao_receber_mensagens = QtWidgets.QPushButton(self.frame_mensagens_recebidas)
        self.botao_receber_mensagens.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_receber_mensagens.setObjectName("botao_receber_mensagens")
        self.verticalLayout_9.addWidget(self.botao_receber_mensagens)
        self.mensagens_recebidas = QtWidgets.QTextEdit(self.frame_mensagens_recebidas)
        self.mensagens_recebidas.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.mensagens_recebidas.setObjectName("mensagens_recebidas")
        self.verticalLayout_9.addWidget(self.mensagens_recebidas)
        self.verticalLayout_3.addWidget(self.frame_mensagens_recebidas)
        self.stackedWidget.addWidget(self.pagina_bot)
        self.pagina_database = QtWidgets.QWidget()
        self.pagina_database.setObjectName("pagina_database")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pagina_database)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_botoes_database = QtWidgets.QFrame(self.pagina_database)
        self.frame_botoes_database.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_botoes_database.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_botoes_database.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes_database.setObjectName("frame_botoes_database")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_botoes_database)
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.botao_carregar_database = QtWidgets.QPushButton(self.frame_botoes_database)
        self.botao_carregar_database.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_carregar_database.setObjectName("botao_carregar_database")
        self.horizontalLayout_6.addWidget(self.botao_carregar_database)
        self.botao_fechar_database = QtWidgets.QPushButton(self.frame_botoes_database)
        self.botao_fechar_database.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_fechar_database.setObjectName("botao_fechar_database")
        self.horizontalLayout_6.addWidget(self.botao_fechar_database)
        self.verticalLayout_10.addWidget(self.frame_botoes_database)
        self.frame_tabela_database = QtWidgets.QFrame(self.pagina_database)
        self.frame_tabela_database.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_tabela_database.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tabela_database.setObjectName("frame_tabela_database")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_tabela_database)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.frame_tabela_database)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.comboBox_seleciona_tabela = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_seleciona_tabela.setStyleSheet("QComboBox {\n"
"background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QComboBox:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.comboBox_seleciona_tabela.setObjectName("comboBox_seleciona_tabela")
        self.comboBox_seleciona_tabela.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_seleciona_tabela)
        self.botao_deletar_linha = QtWidgets.QPushButton(self.frame_3)
        self.botao_deletar_linha.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_deletar_linha.setObjectName("botao_deletar_linha")
        self.horizontalLayout_8.addWidget(self.botao_deletar_linha)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.tabela_dados_db = QtWidgets.QTableView(self.frame_tabela_database)
        self.tabela_dados_db.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(120,0,0);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(120,0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db.setObjectName("tabela_dados_db")
        self.tabela_dados_db.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_4.addWidget(self.tabela_dados_db)
        self.verticalLayout_10.addWidget(self.frame_tabela_database)
        self.stackedWidget.addWidget(self.pagina_database)
        self.pagina_deepnude = QtWidgets.QWidget()
        self.pagina_deepnude.setObjectName("pagina_deepnude")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.pagina_deepnude)
        self.verticalLayout_26.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame_deepnude = QtWidgets.QFrame(self.pagina_deepnude)
        self.frame_deepnude.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_deepnude.setObjectName("frame_deepnude")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_deepnude)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_imagem_normal = QtWidgets.QFrame(self.frame_deepnude)
        self.frame_imagem_normal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_imagem_normal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_normal.setObjectName("frame_imagem_normal")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_imagem_normal)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.imagem_deepnude_normal = QtWidgets.QLabel(self.frame_imagem_normal)
        self.imagem_deepnude_normal.setText("")
        self.imagem_deepnude_normal.setPixmap(QtGui.QPixmap("program_functions/images/bg1.png"))
        self.imagem_deepnude_normal.setAlignment(QtCore.Qt.AlignCenter)
        self.imagem_deepnude_normal.setObjectName("imagem_deepnude_normal")
        self.horizontalLayout_25.addWidget(self.imagem_deepnude_normal)
        self.horizontalLayout_22.addWidget(self.frame_imagem_normal)
        self.frame_imagem_renderizada = QtWidgets.QFrame(self.frame_deepnude)
        self.frame_imagem_renderizada.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_imagem_renderizada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_renderizada.setObjectName("frame_imagem_renderizada")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_imagem_renderizada)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.imagem_deepnude_renderizada = QtWidgets.QLabel(self.frame_imagem_renderizada)
        self.imagem_deepnude_renderizada.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imagem_deepnude_renderizada.setText("")
        self.imagem_deepnude_renderizada.setPixmap(QtGui.QPixmap("program_functions/images/bg2.png"))
        self.imagem_deepnude_renderizada.setAlignment(QtCore.Qt.AlignCenter)
        self.imagem_deepnude_renderizada.setObjectName("imagem_deepnude_renderizada")
        self.horizontalLayout_24.addWidget(self.imagem_deepnude_renderizada)
        self.horizontalLayout_22.addWidget(self.frame_imagem_renderizada)
        self.verticalLayout_26.addWidget(self.frame_deepnude)
        self.frame_botoes_deepnude = QtWidgets.QFrame(self.pagina_deepnude)
        self.frame_botoes_deepnude.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_botoes_deepnude.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_botoes_deepnude.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_botoes_deepnude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes_deepnude.setObjectName("frame_botoes_deepnude")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_botoes_deepnude)
        self.horizontalLayout_23.setContentsMargins(22, 0, 25, 0)
        self.horizontalLayout_23.setSpacing(50)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.botao_imagem_deepnude_2 = QtWidgets.QPushButton(self.frame_botoes_deepnude)
        self.botao_imagem_deepnude_2.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_imagem_deepnude_2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_imagem_deepnude_2.setObjectName("botao_imagem_deepnude_2")
        self.horizontalLayout_23.addWidget(self.botao_imagem_deepnude_2)
        self.botao_criar_deepnude_2 = QtWidgets.QPushButton(self.frame_botoes_deepnude)
        self.botao_criar_deepnude_2.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_criar_deepnude_2.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_criar_deepnude_2.setObjectName("botao_criar_deepnude_2")
        self.horizontalLayout_23.addWidget(self.botao_criar_deepnude_2)
        self.verticalLayout_26.addWidget(self.frame_botoes_deepnude)
        self.stackedWidget.addWidget(self.pagina_deepnude)
        self.pagina_configuracoes = QtWidgets.QWidget()
        self.pagina_configuracoes.setObjectName("pagina_configuracoes")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.pagina_configuracoes)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_extras_configuracoes = QtWidgets.QFrame(self.pagina_configuracoes)
        self.frame_extras_configuracoes.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_extras_configuracoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extras_configuracoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extras_configuracoes.setObjectName("frame_extras_configuracoes")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_extras_configuracoes)
        self.horizontalLayout_27.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.frame_frequencia_configuracoes = QtWidgets.QFrame(self.frame_extras_configuracoes)
        self.frame_frequencia_configuracoes.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_frequencia_configuracoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_frequencia_configuracoes.setObjectName("frame_frequencia_configuracoes")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_frequencia_configuracoes)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.botao_carregar_database_configuracoes = QtWidgets.QPushButton(self.frame_frequencia_configuracoes)
        self.botao_carregar_database_configuracoes.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_carregar_database_configuracoes.setObjectName("botao_carregar_database_configuracoes")
        self.verticalLayout_12.addWidget(self.botao_carregar_database_configuracoes)
        self.comboBox_configuracoes = QtWidgets.QComboBox(self.frame_frequencia_configuracoes)
        self.comboBox_configuracoes.setStyleSheet("QComboBox {\n"
"background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QComboBox:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.comboBox_configuracoes.setObjectName("comboBox_configuracoes")
        self.comboBox_configuracoes.addItem("")
        self.verticalLayout_12.addWidget(self.comboBox_configuracoes)
        self.botao_fechar_database_configuracoes = QtWidgets.QPushButton(self.frame_frequencia_configuracoes)
        self.botao_fechar_database_configuracoes.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_fechar_database_configuracoes.setObjectName("botao_fechar_database_configuracoes")
        self.verticalLayout_12.addWidget(self.botao_fechar_database_configuracoes)
        self.horizontalLayout_27.addWidget(self.frame_frequencia_configuracoes)
        self.frame_banimento_automatico_2 = QtWidgets.QFrame(self.frame_extras_configuracoes)
        self.frame_banimento_automatico_2.setStyleSheet("")
        self.frame_banimento_automatico_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_banimento_automatico_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_banimento_automatico_2.setObjectName("frame_banimento_automatico_2")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_banimento_automatico_2)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_banimento_automatico_2 = QtWidgets.QLabel(self.frame_banimento_automatico_2)
        self.label_banimento_automatico_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;")
        self.label_banimento_automatico_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_banimento_automatico_2.setObjectName("label_banimento_automatico_2")
        self.verticalLayout_32.addWidget(self.label_banimento_automatico_2)
        self.id_manual_configuracoes = QtWidgets.QLineEdit(self.frame_banimento_automatico_2)
        self.id_manual_configuracoes.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.id_manual_configuracoes.setAlignment(QtCore.Qt.AlignCenter)
        self.id_manual_configuracoes.setObjectName("id_manual_configuracoes")
        self.verticalLayout_32.addWidget(self.id_manual_configuracoes)
        self.botao_sair_grupo = QtWidgets.QPushButton(self.frame_banimento_automatico_2)
        self.botao_sair_grupo.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_sair_grupo.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_sair_grupo.setObjectName("botao_sair_grupo")
        self.verticalLayout_32.addWidget(self.botao_sair_grupo)
        self.horizontalLayout_27.addWidget(self.frame_banimento_automatico_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_extras_configuracoes)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_local_inteligencia_2 = QtWidgets.QLabel(self.frame_6)
        self.label_local_inteligencia_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;")
        self.label_local_inteligencia_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_local_inteligencia_2.setObjectName("label_local_inteligencia_2")
        self.verticalLayout_33.addWidget(self.label_local_inteligencia_2)
        self.id_usuario_ban = QtWidgets.QLineEdit(self.frame_6)
        self.id_usuario_ban.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(120,0,0);\n"
"    color: rgb(120,0,0);\n"
"}")
        self.id_usuario_ban.setAlignment(QtCore.Qt.AlignCenter)
        self.id_usuario_ban.setObjectName("id_usuario_ban")
        self.verticalLayout_33.addWidget(self.id_usuario_ban)
        self.botao_banir_usuario = QtWidgets.QPushButton(self.frame_6)
        self.botao_banir_usuario.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_banir_usuario.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_banir_usuario.setObjectName("botao_banir_usuario")
        self.verticalLayout_33.addWidget(self.botao_banir_usuario)
        self.horizontalLayout_27.addWidget(self.frame_6)
        self.verticalLayout_27.addWidget(self.frame_extras_configuracoes)
        self.frame_configuracoes = QtWidgets.QFrame(self.pagina_configuracoes)
        self.frame_configuracoes.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_configuracoes.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_configuracoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_configuracoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_configuracoes.setObjectName("frame_configuracoes")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_configuracoes)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_banimento_automatico = QtWidgets.QFrame(self.frame_configuracoes)
        self.frame_banimento_automatico.setStyleSheet("")
        self.frame_banimento_automatico.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_banimento_automatico.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_banimento_automatico.setObjectName("frame_banimento_automatico")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_banimento_automatico)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_banimento_automatico = QtWidgets.QLabel(self.frame_banimento_automatico)
        self.label_banimento_automatico.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;")
        self.label_banimento_automatico.setAlignment(QtCore.Qt.AlignCenter)
        self.label_banimento_automatico.setObjectName("label_banimento_automatico")
        self.verticalLayout_28.addWidget(self.label_banimento_automatico)
        self.botao_ativa_banimento = QtWidgets.QPushButton(self.frame_banimento_automatico)
        self.botao_ativa_banimento.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_ativa_banimento.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_ativa_banimento.setObjectName("botao_ativa_banimento")
        self.verticalLayout_28.addWidget(self.botao_ativa_banimento)
        self.botao_desativa_banimento = QtWidgets.QPushButton(self.frame_banimento_automatico)
        self.botao_desativa_banimento.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_desativa_banimento.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_desativa_banimento.setObjectName("botao_desativa_banimento")
        self.verticalLayout_28.addWidget(self.botao_desativa_banimento)
        self.aviso_banimento_automatico = QtWidgets.QLabel(self.frame_banimento_automatico)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.aviso_banimento_automatico.setFont(font)
        self.aviso_banimento_automatico.setStyleSheet("color: rgb(120,0,0);")
        self.aviso_banimento_automatico.setAlignment(QtCore.Qt.AlignCenter)
        self.aviso_banimento_automatico.setObjectName("aviso_banimento_automatico")
        self.verticalLayout_28.addWidget(self.aviso_banimento_automatico)
        self.horizontalLayout_26.addWidget(self.frame_banimento_automatico)
        self.frame_local_inteligencia = QtWidgets.QFrame(self.frame_configuracoes)
        self.frame_local_inteligencia.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_local_inteligencia.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_local_inteligencia.setObjectName("frame_local_inteligencia")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_local_inteligencia)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_local_inteligencia = QtWidgets.QLabel(self.frame_local_inteligencia)
        self.label_local_inteligencia.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;")
        self.label_local_inteligencia.setAlignment(QtCore.Qt.AlignCenter)
        self.label_local_inteligencia.setObjectName("label_local_inteligencia")
        self.verticalLayout_30.addWidget(self.label_local_inteligencia)
        self.botao_inteligencia_local = QtWidgets.QPushButton(self.frame_local_inteligencia)
        self.botao_inteligencia_local.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_inteligencia_local.setObjectName("botao_inteligencia_local")
        self.verticalLayout_30.addWidget(self.botao_inteligencia_local)
        self.botao_inteligencia_global = QtWidgets.QPushButton(self.frame_local_inteligencia)
        self.botao_inteligencia_global.setMinimumSize(QtCore.QSize(0, 20))
        self.botao_inteligencia_global.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120,0,0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,0,0);\n"
"}")
        self.botao_inteligencia_global.setObjectName("botao_inteligencia_global")
        self.verticalLayout_30.addWidget(self.botao_inteligencia_global)
        self.aviso_local_inteligencia = QtWidgets.QLabel(self.frame_local_inteligencia)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.aviso_local_inteligencia.setFont(font)
        self.aviso_local_inteligencia.setStyleSheet("color: rgb(120,0,0);")
        self.aviso_local_inteligencia.setAlignment(QtCore.Qt.AlignCenter)
        self.aviso_local_inteligencia.setObjectName("aviso_local_inteligencia")
        self.verticalLayout_30.addWidget(self.aviso_local_inteligencia)
        self.horizontalLayout_26.addWidget(self.frame_local_inteligencia)
        self.frame_frequencia_fala = QtWidgets.QFrame(self.frame_configuracoes)
        self.frame_frequencia_fala.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_frequencia_fala.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_frequencia_fala.setObjectName("frame_frequencia_fala")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_frequencia_fala)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_frequencia_fala = QtWidgets.QLabel(self.frame_frequencia_fala)
        self.label_frequencia_fala.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 15px SegoeUIl, bold;")
        self.label_frequencia_fala.setAlignment(QtCore.Qt.AlignCenter)
        self.label_frequencia_fala.setObjectName("label_frequencia_fala")
        self.verticalLayout_29.addWidget(self.label_frequencia_fala)
        self.slider_frequencia_fala = QtWidgets.QSlider(self.frame_frequencia_fala)
        self.slider_frequencia_fala.setStyleSheet("QSlider::handle:horizontal {background-color: rgb(120,0,0);}")
        self.slider_frequencia_fala.setMaximum(10)
        self.slider_frequencia_fala.setPageStep(1)
        self.slider_frequencia_fala.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frequencia_fala.setInvertedAppearance(False)
        self.slider_frequencia_fala.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider_frequencia_fala.setObjectName("slider_frequencia_fala")
        self.verticalLayout_29.addWidget(self.slider_frequencia_fala)
        self.aviso_frequencia_fala = QtWidgets.QLabel(self.frame_frequencia_fala)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.aviso_frequencia_fala.setFont(font)
        self.aviso_frequencia_fala.setStyleSheet("color: rgb(120,0,0);")
        self.aviso_frequencia_fala.setAlignment(QtCore.Qt.AlignCenter)
        self.aviso_frequencia_fala.setObjectName("aviso_frequencia_fala")
        self.verticalLayout_29.addWidget(self.aviso_frequencia_fala)
        self.horizontalLayout_26.addWidget(self.frame_frequencia_fala)
        self.verticalLayout_27.addWidget(self.frame_configuracoes)
        self.frame = QtWidgets.QFrame(self.pagina_configuracoes)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_banimento_automatico_3 = QtWidgets.QLabel(self.frame)
        self.label_banimento_automatico_3.setGeometry(QtCore.QRect(30, 100, 691, 51))
        self.label_banimento_automatico_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"    font: 10px SegoeUIl, bold;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_banimento_automatico_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_banimento_automatico_3.setObjectName("label_banimento_automatico_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 411, 91))
        self.label_3.setStyleSheet("image: url(:/logo_telegram/program_functions/images//telegram_logo.png);")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_27.addWidget(self.frame)
        self.stackedWidget.addWidget(self.pagina_configuracoes)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.palco_central)
        self.rodape = QtWidgets.QFrame(self.centralwidget)
        self.rodape.setMinimumSize(QtCore.QSize(0, 17))
        self.rodape.setMaximumSize(QtCore.QSize(16777215, 17))
        self.rodape.setStyleSheet("background-color: rgb(17, 17, 17);")
        self.rodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape.setObjectName("rodape")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.rodape)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rodape_desenvolvedor = QtWidgets.QLabel(self.rodape)
        self.rodape_desenvolvedor.setMinimumSize(QtCore.QSize(0, 20))
        self.rodape_desenvolvedor.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_desenvolvedor.setObjectName("rodape_desenvolvedor")
        self.horizontalLayout_7.addWidget(self.rodape_desenvolvedor)
        self.rodape_versao = QtWidgets.QLabel(self.rodape)
        self.rodape_versao.setMinimumSize(QtCore.QSize(0, 20))
        self.rodape_versao.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_versao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rodape_versao.setObjectName("rodape_versao")
        self.horizontalLayout_7.addWidget(self.rodape_versao)
        self.verticalLayout.addWidget(self.rodape)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manicomio Artifical Inteligence | Telegram Bot"))
        self.inserir_token_bot.setText(_translate("MainWindow", "token  bot"))
        self.inserir_canal_bot.setText(_translate("MainWindow", "id canal "))
        self.inserir_id_pessoal_bot.setText(_translate("MainWindow", "id pessoal"))
        self.inserir_id_backups.setText(_translate("MainWindow", "id backups"))
        self.inserir_token_dropbox.setText(_translate("MainWindow", "token dropbox"))
        self.inserir_token_giphy.setText(_translate("MainWindow", "token giphy"))
        self.inserir_token_bitly.setText(_translate("MainWindow", "token bitly"))
        self.inserir_id_google.setText(_translate("MainWindow", "id google"))
        self.inserir_token_weather.setText(_translate("MainWindow", "token hgbrasilWeater"))
        self.inserir_token_imgur.setText(_translate("MainWindow", "token imgur"))
        self.inserir_token_yandex.setText(_translate("MainWindow", "token yandex"))
        self.inserir_key_google.setText(_translate("MainWindow", "key google"))
        self.botao_start_bot.setText(_translate("MainWindow", "start artificial inteligence"))
        self.comboBox_grupos_bot.setItemText(0, _translate("MainWindow", "      selecione"))
        self.botao_enviar_imagem_bot.setText(_translate("MainWindow", "enviar imagem"))
        self.botao_enviar_video_bot.setText(_translate("MainWindow", "enviar video"))
        self.botao_enviar_documento_bot.setText(_translate("MainWindow", "enviar documento"))
        self.botao_carregar_db.setText(_translate("MainWindow", "carregar database"))
        self.botao_fechar_db.setText(_translate("MainWindow", "fechar database"))
        self.texto_enviar_mensagem.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">Digite sua mensagem</span></p></body></html>"))
        self.botao_enviar_mensagem.setText(_translate("MainWindow", "enviar mensagem"))
        self.linha_mensagem.setText(_translate("MainWindow", "Envie sua mensagem usando Enter"))
        self.botao_receber_mensagens.setText(_translate("MainWindow", "receber mensagens"))
        self.mensagens_recebidas.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">Mensagens...</span></p></body></html>"))
        self.botao_carregar_database.setText(_translate("MainWindow", "carregar database"))
        self.botao_fechar_database.setText(_translate("MainWindow", "fechar database"))
        self.comboBox_seleciona_tabela.setItemText(0, _translate("MainWindow", "                      selecione a tabela"))
        self.botao_deletar_linha.setText(_translate("MainWindow", "deletar linha"))
        self.botao_imagem_deepnude_2.setText(_translate("MainWindow", "carregar imagem"))
        self.botao_criar_deepnude_2.setText(_translate("MainWindow", "deep fake"))
        self.botao_carregar_database_configuracoes.setText(_translate("MainWindow", "carregar database"))
        self.comboBox_configuracoes.setItemText(0, _translate("MainWindow", "selecione a tabela"))
        self.botao_fechar_database_configuracoes.setText(_translate("MainWindow", "fechar database"))
        self.label_banimento_automatico_2.setText(_translate("MainWindow", "SAIR DE UM GRUPO"))
        self.id_manual_configuracoes.setText(_translate("MainWindow", "id do grupo"))
        self.botao_sair_grupo.setText(_translate("MainWindow", "clique para sair"))
        self.label_local_inteligencia_2.setText(_translate("MainWindow", "BANIR UM USUÁRIO"))
        self.id_usuario_ban.setText(_translate("MainWindow", "id do usuário"))
        self.botao_banir_usuario.setText(_translate("MainWindow", "clique para banir"))
        self.label_banimento_automatico.setText(_translate("MainWindow", "BANIMENTO AUTOMATICO"))
        self.botao_ativa_banimento.setText(_translate("MainWindow", "ativado"))
        self.botao_desativa_banimento.setText(_translate("MainWindow", "desativado"))
        self.aviso_banimento_automatico.setText(_translate("MainWindow", "ATIVADO"))
        self.label_local_inteligencia.setText(_translate("MainWindow", "LOCAL INTELIGENCIA"))
        self.botao_inteligencia_local.setText(_translate("MainWindow", "local"))
        self.botao_inteligencia_global.setText(_translate("MainWindow", "global"))
        self.aviso_local_inteligencia.setText(_translate("MainWindow", "GLOBAL"))
        self.label_frequencia_fala.setText(_translate("MainWindow", "FREQUENCIA DA FALA"))
        self.aviso_frequencia_fala.setText(_translate("MainWindow", "MUDO"))
        self.label_banimento_automatico_3.setText(_translate("MainWindow", "Manicomio Articifial Inteligence with Database | 2020 @GorpoOrko "))
        self.rodape_desenvolvedor.setText(_translate("MainWindow", "@GorpoOrko | manicomio | 2020"))
        self.rodape_versao.setText(_translate("MainWindow", "v1.0  "))
import files_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
