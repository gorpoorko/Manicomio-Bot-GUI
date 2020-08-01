
from main import *


#funcoes principais-------------->
def menusJanela(self):
    self.ui.botao_home.clicked.connect(lambda: paginaHome(self))
    self.ui.botao_bot.clicked.connect(lambda: paginaBot(self))
    self.ui.botao_database.clicked.connect(lambda: paginaDatabase(self))
    self.ui.botao_deepnude.clicked.connect(lambda: paginaDeepNude(self))
    self.ui.botao_config.clicked.connect(lambda: paginaConfigs(self))


def paginaHome(self):
    self.ui.stackedWidget.setCurrentIndex(0)
def paginaBot(self):
    self.ui.stackedWidget.setCurrentIndex(1)
def paginaDatabase(self):
    self.ui.stackedWidget.setCurrentIndex(2)
def paginaDeepNude(self):
    self.ui.stackedWidget.setCurrentIndex(3)
def paginaConfigs(self):
    self.ui.stackedWidget.setCurrentIndex(4)