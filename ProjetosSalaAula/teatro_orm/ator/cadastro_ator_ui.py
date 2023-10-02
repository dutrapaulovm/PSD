import PySide6.QtGui
from dialogo_padrao import *

from entidades import Ator
from conexao import *
from ator.FormCadastroAtor_ui import *

class CadastroAtorUI(QWidget):

    def __init__(self):
        super(CadastroAtorUI, self).__init__()
        self.ui = Ui_FormCadastroAtor()
        self.ui.setupUi(self)

        #Vinculando os métodos com os botões
        self.ui.btnSalvar.clicked.connect(self.salvar) 

        #Criando um objeto do tipo Ator
        self.ator = Ator()
        #Inicializa a chave primária com zero indicando
        #que inicialmente será realizado uma inserção
        self.ator.CODATOR = 0  
        """
        Atributo que faz referência ao formulário
        de pesquisa.
        """
        self.form_pesquisa = None           

    """
    O método closeEvent é chamado automaticamente
    sempre que um formulário é fechado
    """
    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)

    @Slot()
    def salvar(self):
        try:

            #Atribuindo cada atributo com o valor correspondente
            #da interface
            self.ator.NOME = self.ui.edtNome.text()            
            #Salvando os dados
            if self.ator.CODATOR <= 0:
                #Insere o registro no banco de dados
                session.add(self.ator)
            else:                
                #Atualiza o registro no banco de dados
                session.merge(self.ator)

            #Confirma a inclusão ou alteração    
            session.commit()            

            #Limpando o campo após salvar
            self.ui.edtNome.setText("")

            self.ator = Ator()
            self.ator.CODATOR = 0

            #Fecha janela de cadastro após operação    
            self.close()

        except Exception as e:
            print(e)