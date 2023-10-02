
#O método Column será para definir
#as colunas das tabelas do banco de dados
from sqlalchemy import Column

#Nesta linha estamos importando os tipos
#de dados que serão utilizadas pelas
#colunas
from sqlalchemy import Date, String, Integer, Double

#Nesta linha estamos importando o 
#método ForeignKey para definir as colunas
#que serão chave estrangeira
from sqlalchemy import ForeignKey

#Nesta linha importamos o método relationship
#para definir o relacionamento entre as tabelas
from sqlalchemy.orm import relationship

#Nesta linha importamos o método declarative_base
#para criar a classe Base para todas as entidades
#do banco de dados
from sqlalchemy.ext.declarative import declarative_base

#Nesta linha, estamos criar um classe utilizada
#pela biblioteca sqlalchemy para que possamos mapear
#as entidades do banco de dados.
Base = declarative_base()

"""
A partir deste ponto, iremos realizar o mapeamento
das entidades do banco de dados em classes para
ser utilizada em conjunto com a biblioteca sqlalchemy
"""
class Ator(Base):

    __tablename__ = 'ator'
    CODATOR = Column(Integer, primary_key = True)
    NOME = Column(String(300), default = '', nullable=False)

class Teatro(Base):
    __tablename__ = "teatro"
    CODTEATRO = Column(Integer, primary_key = True)
    NOME = Column(String(300), default = '', nullable = False)
    CAPACIDADEASSENTOS = Column(Integer, default = 0, nullable = False)

class Peca(Base):
    __tablename__ = "peca"
    CODPECA = Column(Integer, primary_key =True)
    NOME = Column(String(300), default = '', nullable=False)

class AtorPeca(Base):
    __tablename__ = "atorpeca"
    CODATOR = Column(Integer, 
            ForeignKey('ator.CODATOR'), primary_key=True)
    CODPECA = Column(Integer, 
            ForeignKey('peca.CODPECA'), primary_key=True)
    
class Apresentacao(Base):
    __tablename__ = "apresentacao"
    CODAPRESENTACAO = Column(Integer, primary_key=True)
    CODTEATRO = Column(Integer, 
        ForeignKey('teatro.CODTEATRO'), nullable=False)
    CODPECA = Column(Integer,
        ForeignKey('peca.CODPECA'), nullable=False)
    QUANTPUBLICO = Column(Integer, default=0, nullable=False)
    DATA = Column(Date, nullable=False)


class Ingresso(Base):
    __tablename__ = "ingresso"
    CODINGRESSO = Column(Integer, primary_key=True)
    CODAPRESENTACAO = Column(Integer, 
        ForeignKey('apresentacao.CODAPRESENTACAO'), nullable=False)
    TIPOCADEIRA = Column(String(1), default='', nullable=False)
    DATA = Column(Date, nullable=False)
    PRECO = Column(Double, default=0.0, nullable=False)




    





