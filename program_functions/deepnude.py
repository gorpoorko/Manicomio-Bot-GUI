from main import *
from PIL import Image
import subprocess

def deepNude(self):
    self.ui.botao_imagem_deepnude_2.clicked.connect(lambda: selecionarImagem(self))
    self.ui.botao_criar_deepnude_2.clicked.connect(lambda: ativaDeepNudes(self))



def selecionarImagem(self):
    self.imagem_recebida = []
    try:
        janela2 = QWidget()
        janela2.resize(800, 600)
        janela2.move(100, 200)
        janela2.setWindowTitle('Manicômio | Deep Nude')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(janela2, "MANICOMIO | DEEP FAKE | Escolha sua imagem", "", "All Files (*);;JPG (*.jpg);;PNG (*.png)", options=options)
        if fileName:
            self.ui.imagem_deepnude_normal.setPixmap(QtGui.QPixmap(fileName).scaled(800, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            self.ui.imagem_deepnude_renderizada.setPixmap(QtGui.QPixmap('bot_files/images/processando.png').scaled(300, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
            if fileName in self.imagem_recebida:
                self.imagem_recebida.clear()
            else:
                # print(self.imagem_recebida)
                self.imagem_recebida.clear()
                self.imagem_recebida.append(fileName)
                #print(fileName)
        # carrega na variavel do Image do pilow (PIL) a imagem aberta
        im1 = Image.open(self.imagem_recebida[0])
        # salva a imagem usando a extensao que quisermos
        im1 = im1.save("bot_files/arquivos/file.jpg")
    except:
        pass


def ativaDeepNudes(self):
    try:
        subprocess.call('python bot_files/plugins/deep_nude/deepnude.py')
    except:
        pass
    self.ui.imagem_deepnude_renderizada.setPixmap(QtGui.QPixmap('bot_files/arquivos/renderizada.jpg').scaled(800, 450, QtCore.Qt.KeepAspectRatio))  # aumentar imagem com qtcore .scaled(200,200, QtCore.Qt.KeepAspectRatio)
