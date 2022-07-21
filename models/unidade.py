from env import Base,session
from dependencies.base_dependencies import *
from sqlalchemy.orm import relationship
from models.cliente import Cliente
from sqlalchemy import select

class Unidade(Base):
    __tablename__ = 'unidades' #obrigatorio nome tabela
    idunidade = Column(Integer, primary_key=True)
    nome = Column(String(64))
    idclientes = Column(Integer)

    def __init__(self, idunidade, nome):
        self.idunidade = idunidade
        self.nome = nome
        
def getAllUnidades():
    return session.query(Unidade).all()

def getAllUnidadesRelatedClientes():
    statement = select([Unidade.nome.label('nome_unidade'),Unidade.idunidade,Cliente.idclientes, Cliente.nome]).join(Cliente, Cliente.idclientes == Unidade.idclientes)
    result = session.execute(statement)
    ls = []
    for elements in result:
        ls.append(elements)
    return ls