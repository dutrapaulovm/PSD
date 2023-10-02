from FormPesquisa_ui import *
from conexao import *
from ator.cadastro_ator_ui import *
"""
Implementando o formulário de pesquisa para o ator
"""
class PesquisaAtor(QWidget):

    def __init__(self):
        super(PesquisaAtor, self).__init__()
        #Estamos criando a instância do formulário de pesquisa
        self.ui = Ui_FormPesquisa()
        #Chamando o método setupUi para configurar
        #os componentes da interface com o formulário
        self.ui.setupUi(self)

        #Chama o método para preencher a tabela do formulário
        self.preencher_tabela()

        #Associando o método para chamar o cadastro de ator
        self.ui.BtnIncluir.clicked.connect(self.exibir_cad_ator)

        #Associando o método de pesquisa com a caixa de texto
        self.ui.EdtValorPesquisa.textChanged.connect(self.pesquisa_por_valor)

        #Associando o evento de duplo clique do item na tabela
        self.ui.tableResultado.itemDoubleClicked.connect(self.seleciona_linha)

    def seleciona_linha(self):
        table  = self.ui.tableResultado        
        #Recuperando o índice selecionado na tabela
        linha = table.currentIndex().row()
        self.cadastro = CadastroAtorUI()
        """
            Passando a referência do formulário
            de pesquisa para o formulário de cadastro
        """
        self.cadastro.form_pesquisa = self

        #Recuperando os dados das colunas
        ator = Ator()
        """
        Utilizando o método item para recuperar o valor da
        linha seleciona. Estamos informando também o valor
        do indíce da coluna que devemos recuperar
        """
        ator.CODATOR = int(table.item(linha, 0).text())
        ator.NOME = table.item(linha, 1).text()        
        
        """
            O atributo ator deve ser declarado também no
            formulário de cadastro
        """
        self.cadastro.ator = ator
        """
        Atualizando os campos do formulário com os dados
        selecionados
        """
        self.cadastro.ui.edtNome.setText(ator.NOME)        
        
        self.cadastro.show()

    """
        Método chamado enquanto o usuário estiver
        digitando algo na caixa de texto de pesquisa
    """
    def pesquisa_por_valor(self):
        self.preencher_tabela()
    
    """
        Chamado quando clicamos no botão BtnIncluir
    """
    def exibir_cad_ator(self):
        self.cadastro = CadastroAtorUI()
        self.cadastro.form_pesquisa = self        
        self.cadastro.show()

    """
        Método responsável por realizar a consulta no banco 
        de dados e preenchar o componente de tabela no
        formulário de pesquisa
    """
    def preencher_tabela(self):

        #Recuperando o conteúdo da caixa de texto
        valor = self.ui.EdtValorPesquisa.text()    

        if valor != "":
            resultados = session.query(Ator).filter(Ator.NOME.contains(valor)).all()
        else:
            #Buscando os dados da tabela ator
            resultados = session.query(Ator).all()
                
        #Retornando a quantidade
        total = len(resultados) 

        """
        Para o componente QTableWidget devemos
        definir o título das colunas através de um
        vetor
        """
        colunas = ["Código", "Nome"]

        """
        Antes de preencher os dados da tabela
        devemos limpar o conteúdo da tabela
        através do método setRowCount
        """
        self.ui.tableResultado.setRowCount(0)

        """
        Configurando os dados da tabela com os dados
        consultados        
        """
        self.ui.tableResultado.setRowCount(total)
        #Recuperando o quantidade de colunas
        total_colunas = len(colunas)
        #Definindo a quantidade de colunas da tabela
        self.ui.tableResultado.setColumnCount(total_colunas)        
        #Definindo os títulos da tabela
        self.ui.tableResultado.setHorizontalHeaderLabels(colunas)

        #Preenchendo a tabela com os dados da consulta
        for linha in range(total):        
            #Para cada linha preenchemos os dados
            #de cada coluna com o seu valor
            ator = resultados[linha]
            for coluna in range(total_colunas):
                if (coluna == 0):
                    valor = QTableWidgetItem(f"{ator.CODATOR}")
                if (coluna == 1):
                    valor = QTableWidgetItem(f"{ator.NOME}")
                
                self.ui.tableResultado.setItem(linha, coluna, valor)




        
