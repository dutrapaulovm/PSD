from sqlalchemy import Column, Integer, String, Date, Double, DateTime, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Teatro(Base):
    __tablename__ = 'teatro'
    CODTEATRO = Column(Integer, primary_key=True)
    NOME = Column(String(300), nullable=False)
    CAPACIDADEASSENTOS = Column(Integer)

class Ator(Base):
    __tablename__ = 'ator'
    CODATOR = Column(Integer, primary_key=True)
    NOME = Column(String(300)) 

class Peca(Base):
    __tablename__ = 'peca'
    CODPECA = Column(Integer, primary_key=True)
    NOME = Column(String(300))    
    atores = relationship('Ator', secondary='atorpeca')       

class AtorPeca(Base):
    __tablename__ = 'atorpeca'
    CODPECA = Column(Integer, ForeignKey('peca.CODPECA'), primary_key=True)
    CODATOR = Column(Integer, ForeignKey('ator.CODATOR'), primary_key=True)    


class Apresentacao(Base):
    __tablename__ = 'apresentacao'
    CODAPRESENTACAO = Column(Integer, primary_key=True)
    CODTEATRO = Column(Integer, ForeignKey('teatro.CODTEATRO'))
    CODPECA = Column(Integer, ForeignKey('peca.CODPECA'))
    QUANTIDADEPUBLICO = Column(Integer, default=0)
    DATA = Column(Date)

    teatro = relationship('Teatro')
    peca = relationship('Peca')
    ingressos = relationship('Ingresso')    


class Ingresso(Base):
    __tablename__ = 'ingresso'
    CODINGRESSO = Column(Integer, primary_key=True)
    CODAPRESENTACAO = Column(Integer, ForeignKey('apresentacao.CODAPRESENTACAO'))
    TIPOCADEIRA = Column(String(1), default='S')
    DATA = Column(Date)
    PRECO = Column(Double, default=0)

    apresentacao = relationship('Apresentacao')    