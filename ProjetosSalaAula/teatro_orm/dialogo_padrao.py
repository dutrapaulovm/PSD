#Utilizado para acessar funções
#internas do sistema. Como por exemplo, finalizar a aplicação
import sys
from typing import Optional

#Utilizada para chamar iniciar a aplicação em QT
from PySide6.QtWidgets import QApplication

#Utilizada para criar as janelas e dialogos
from PySide6.QtWidgets import QMainWindow, QDialog

#Importando os componentes para ter acesso aos botões
#caixas de texto
from PySide6.QtWidgets import QPushButton, QLineEdit

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QTableView
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QTableWidgetItem

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, QObject, Slot

class DialogoPadraoUI(QDialog):
    
    """
    Definindo o construtor da janela de diálogo.
    O construtor é utilizado para carregar o arquivo
    feito em QTDesigner e definir ações para os componentes
    da interface.
    """
    def __init__(self, ui_filename, parent):
        
        super().__init__(parent)

        #Utilizado para carregar o arquivo da interface    
        loader = QUiLoader()
        
        #Defindo o arquivo que será carregado pelo QT
        ui_file = QFile(ui_filename)
        
        #Testando se o arquivo pode ser aberto
        if not ui_file.open(QIODevice.ReadOnly):
            msg = "Erro ao abrir o arquivo: "
            print(f"{msg} {ui_filename}: {ui_file.errorString()}")
            sys.exit(-1)

        #Caso não haja erro, abre o arquivo da interface
        ui_file.open(QFile.ReadOnly)
        """
        Carrega o arquivo da interface. A propriedade
        self.ui, representa o objeto da interface. Então
        esse objeto será utilizado para obtermos acesso a 
        qualquer componente incluído na interface no QTDesigner 
        """
        self.ui = loader.load(ui_file, self)
        #Fecha o arquivo
        ui_file.close()    

    """
    Estamos sobreesvendo o método show da classe
    QDialog para que possamos exibir o conteúdo do
    arquivo da interface.
    """
    def show(self):
        self.ui.show()

    def showMaximized(self):
        self.ui.showMaximized()