from conexao import *
from teatro.FormCadastroTeatro_ui import *

class CadastroTeatroUi(QWidget):

    def __init__(self):
        super(CadastroTeatroUi, self).__init__()
        self.ui = Ui_FormCadastroTeatro()
        self.ui.setupUi(self)

        #Cria um objeto padrão para informar os dados do teatro
        self.teatro = Teatro()  
        self.teatro.CODTEATRO = 0

    """
        Método chamado automaticamente quando o formulário
        é fechado. Quando chamado, atualiza a tabela do formulário
        de pesquisa.
    """
    def closeEvent(self, event):
        self.form_pesquisa.preencher_tabela()
        return super().closeEvent(event)
    
    def salvar(self):

        try:

            self.teatro.NOME = self.ui.edtNome.text()
            #Converte o conteúdo para inteiro
            capacidade = int(self.ui.spnCapAssentos.text())
            #Atribuindo a variável no campo 
            self.teatro.CAPACIDADEASSENTOS = capacidade

            if (self.teatro.CODTEATRO <= 0):
               session.add(self.teatro)
            else:
               session.merge(self.teatro)

            session.commit()

            #Fecha o formulário
            self.close()
        
        except Exception as e:
            print(e)
