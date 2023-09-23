from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entidades import *

# Configuração da conexão com o banco de dados
user = 'root' #Nome do usuário do banco de dados
password = 'root' #Senha do usuário no banco de dados
host = 'localhost' #endereço do banco de dados 
port = '3306' #porta de conexão 
database = 'teatro' #nome do banco de dados

# Criação da URL de conexão
url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

# Criação do mecanismo de conexão
engine = create_engine(url)
session = None

# Teste de conexão
try:
    connection = engine.connect()
    print("Conexão estabelecida com sucesso!")
    connection.close()

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

except Exception as e:
    print("Falha na conexão:", e)