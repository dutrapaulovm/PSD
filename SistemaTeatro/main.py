from dominio import *
from conexao import *

peca_repository = PecaRepository(session=session)
resultados = peca_repository.get_all()

for peca in resultados:    
    print(peca.NOME)
