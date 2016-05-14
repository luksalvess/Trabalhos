from sqlalchemy import Column, DateTime, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Grupo(Base):
    __tablename__ = 'grupo'

    codigo = Column(Integer, Sequence('grupo_codigo_seq'), primary_key=True)
    nome = Column(String(50))
    razao_social = Column(String(50))
    cnpj = Column(String(20))


class Cliente(Base):
    __tablename__ = 'cliente'

    codigo = Column(Integer, Sequence('cliente_codigo_seq'), primary_key=True)
    nome = Column(String(50))
    rua = Column(String(50))
    cidade = Column(String(50))
    nascimento = Column(DateTime)
