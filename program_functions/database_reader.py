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


def funcoesBancodados(self):
    self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    self.db.setDatabaseName('bot_files/bot_database.db')
    self.model = QtSql.QSqlTableModel()
    self.nome_tabelas = self.db.tables()
    #self.ui.comboBox_seleciona_tabela.clear()
    self.ui.comboBox_seleciona_tabela.addItems(self.nome_tabelas)
    self.ui.comboBox_seleciona_tabela.activated.connect(lambda: carregaTabelas(self))
    self.model.setTable('mensagens')
    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model.select()
    self.ui.tabela_dados_db.setModel(self.model)
    self.i = self.model.rowCount()
    self.ui.botao_deletar_linha.clicked.connect(lambda: deletarLinha(self) )
    self.db.close()


def carregaTabelas(self):
    a = self.ui.comboBox_seleciona_tabela.currentText()
    self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    self.db.setDatabaseName('bot_files/bot_database.db')
    self.model = QtSql.QSqlTableModel()
    self.model.setTable(a)
    self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    self.model.select()
    self.ui.tabela_dados_db.setModel(self.model)
    self.i = self.model.rowCount()
    self.db.close()



def deletarLinha(self):
    self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    self.db.setDatabaseName('bot_files/bot_database.db')
    self.model = QtSql.QSqlTableModel()
    if self.ui.tabela_dados_db.currentIndex().row() > -1:
        self.model.removeRow(self.ui.tabela_dados_db.currentIndex().row())
        self.i -= 1
        self.model.select()
        self.db.close()
    else:
        QMessageBox.question(self, 'Mensagem', "Selecione uma linha para deletar", QMessageBox.Ok)
        self.show()