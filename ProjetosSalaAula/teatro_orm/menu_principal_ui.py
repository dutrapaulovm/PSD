"""
Importando o arquivo utilizado por todas
as janelas da aplicação
"""
from dialogo_padrao import *

#Importando as janelas de pesquisa
from ator.pesquisa_ator_ui import *

"""
Criando a nossa janela principal. Toda classe
que representa uma interface deve herdar a classe
DialogoPadraoUI
"""
class MenuPrincipalUI(DialogoPadraoUI): 

    def __init__(self, ui_filename = "MenuPrincipalUI.ui", parent = None):
        super().__init__(ui_filename, parent)  
        #Vinculando o método exibir_cad_ator com a opção do menu
        self.ui.actionAtor.triggered.connect(self.exibir_cad_ator) 

    @Slot()
    def exibir_cad_ator(self):
        """
        No construtor devemos informar o parâmetro 
        parent, associando a janela principal
        """
        self.cadastro = PesquisaAtor()
        self.cadastro.show()  
