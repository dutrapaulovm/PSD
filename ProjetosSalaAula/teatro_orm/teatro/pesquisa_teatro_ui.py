#Importando o formulário de pesquisa padrão
from FormPesquisa_ui import *
#Importanto o arquivo de conexão com o banco de dados
from conexao import *
#Importando o formulário de cadastro
from teatro.cadastro_teatro_ui import *

"""
Implementando o código para o formulário de pesquisa
do teatro
"""
class FormPesquisaTeatro(QWidget):
    
    def __init__(self):
        super(FormPesquisaTeatro, self).__init__()
        #Inicializando os componentes do formulário de pesquisa
        self.ui = Ui_FormPesquisa()
        self.ui.setupUi(self)

        #Chamando o método para preencher a tabela com os dados
        self.preencher_tabela()

        #Associando o botão de incluir com o método exibir_cadastro
        self.ui.BtnIncluir.clicked.connect(self.exibir_cadastro)

        #Associando o duplo clique da tabela para selecionar a linha
        self.ui.tableResultado.itemDoubleClicked.connect(self.seleciona_linha)

        #Associando o evento da caixa de pesquisa
        self.ui.EdtValorPesquisa.textChanged.connect(self.pesquisa_por_valor)        


    def exibir_cadastro(self):
        pass

    def seleciona_linha(self):
        pass

    def pesquisa_por_valor(self):
        self.preencher_tabela()

    """
    Realiza a consulta no banco de dados e preenche
    a tabela com os dados consultados
    """
    def preencher_tabela(self):
        #Recuperando o valor da caixa de texto
        valor = self.ui.EdtValorPesquisa.text()

        if (valor == ""):
            #Busca todos os registro no banco
            query = session.query(Teatro)
            resultado = query.all()
        else:
            #Realiza o filtro de acordo com o valor
            query = session.query(Teatro)
            #Aplicando o filtro na consulta
            filtro = query.filter(Teatro.NOME.contains(valor))
            resultado = filtro.all()

        #Retornando a quantidade de registros
        total = len(resultado)

        #Definindo o título das colunas da tabela
        colunas = ["Código", "Nome", "Cap. Assentos"]

        #Limpando os dados da tabela, se houve algum
        self.ui.tableResultado.setRowCount(0)

        #Definindo a nova quantidade de linhas
        self.ui.tableResultado.setRowCount(total)

        #Retornando o total de colunas
        total_colunas = len(colunas)

        #Definindo o total de colunas na tabela
        self.ui.tableResultado.setColumnCount(total_colunas)

        #Definindo o nomes da colunas
        table = self.ui.tableResultado
        table.setHorizontalHeaderLabels(colunas)

        #Preenchendo a tabela
        for linha in range(len(resultado)):
            #Recuperando um item do resultado
            teatro = resultado[linha]
            #Preenchendo as colunas da linha
            for coluna in range(len(colunas)):
                if coluna == 0: #CODTEATRO
                    valor = QTableWidgetItem(f"{teatro.CODTEATRO}")
                if coluna == 1: #Nome
                    valor = QTableWidgetItem(f"{teatro.NOME}")
                if coluna == 2: #Cap. Assentos
                    valor = QTableWidgetItem(f"{teatro.CAPACIDADEASSENTOS}")

                #Atualizando a linha da tabela com os dados
                self.ui.tableResultado.setItem(linha, coluna, valor)