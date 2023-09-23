from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dominio import * 

# Configuração da conexão com o banco de dados
user = 'root'
password = 'root'
host = 'localhost'
port = '3306'
database = 'teatro'

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