from menu_principal_ui import *
"""
Definindo o ponto principal da aplicação.
Para executar a aplicação, devemos compilar a
partir desse arquivo.
"""
if __name__ == "__main__":
    #Criando o objeto para iniciar a aplicação
    app = QApplication(sys.argv)
    #Criando a classe do MenuPrincipal
    menuPrincipal = MenuPrincipalUI()
    #Exibindo a janela
    menuPrincipal.showMaximized()
    #Chamado após a aplicação ser finalizada
    sys.exit(app.exec_())