from env import Base,session
from dependencies.base_dependencies import *
from sqlalchemy.orm import relationship
from models.unidade import Unidade
from models.cliente import Cliente
from sqlalchemy import select, alias

class Equipamento(Base):
    __tablename__ = 'equipamentos' #obrigatorio nome tabela
    idequipamento = Column(Integer, primary_key=True)
    idunidade = Column(Integer)
    nome = Column(String(64))

    def __init__(self, idequipamento, idunidade,nome):
        self.idequipamento  = idequipamento
        self.idunidade = idunidade
        self.nome = nome
        
#def getAllEquipamentos():
#    return session.query(Equipamento).all()

def getAllEquipamentosDetail():
    statement = select([Equipamento.idequipamento,Equipamento.idunidade, Unidade.idclientes, Equipamento.nome.label('nome_equipamento'), Unidade.nome.label('nome_unidade'), Cliente.nome.label('nome_cliente')]).join(Unidade, Equipamento.idunidade == Unidade.idunidade).join(Cliente, Cliente.idclientes == Unidade.idclientes)
    result = session.execute(statement)
    ls = []
    for elements in result:
        ls.append(elements)
    return ls

def getEquipamentosDetailById(id):
    statement = select([Equipamento.idequipamento,Equipamento.idunidade, Unidade.idclientes, Equipamento.nome.label('nome_equipamento'), Unidade.nome.label('nome_unidade'), Cliente.nome.label('nome_cliente')]).join(Unidade, Equipamento.idunidade == Unidade.idunidade).join(Cliente, Cliente.idclientes == Unidade.idclientes).where(Equipamento.idequipamento == id)
    result = session.execute(statement)
    ls = []
    for elements in result:
        ls.append(elements)
    return ls