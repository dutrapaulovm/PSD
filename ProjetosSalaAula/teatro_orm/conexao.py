from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.orm import sessionmaker
from entidades import *

usuario  = "root"
senha    = "root"
porta    = "3306"
host     = "localhost"
database = "teatro"

# Criação da URL de conexão
url = f'mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{database}'

# Criação do mecanismo de conexão com o banco de dados
engine = create_engine(url)
"""
A variável session representa a sessão ativa de conexão com
o banco de dados
"""
session = None

try:

    #Criando a conexão com o banco de dados
    conexao = engine.connect()
    print("Conexão realizada com sucesso")
    conexao.close()

    """
    Cria as tabelas do banco de dados com base nas
    classes em Python
    """   
    Base.metadata.create_all(engine)
    """
    Cria a sessão com o banco de dados para realizar
    as operações nas tabelas
    """
    Session = sessionmaker(bind=engine)
    session = Session()

except Exception as e:
    print('Erro de conexão', e)