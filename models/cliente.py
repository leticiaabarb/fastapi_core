from env import Base,session
from dependencies.base_dependencies import *
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = 'clientes' #obrigatorio nome tabela
    idclientes = Column(Integer, primary_key=True)
    nome = Column(String(40))

    def __init__(self, idclientes, nome):
        self.idclientes = idclientes
        self.nome = nome
        
def getAllClientes():
    return session.query(Cliente, Cliente.nome.label('nome_cliente'), Cliente.idclientes).all()