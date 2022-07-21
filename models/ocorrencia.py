from env import Base,session
from dependencies.base_dependencies import *
from models.equipamento import Equipamento
from models.unidade import Unidade
from models.cliente import Cliente
from sqlalchemy import text, select

class Ocorrencia(Base):
    __tablename__ = 'tbl_ocorrencia' #obrigatorio nome tabela
    id_ocorrencia = Column(Integer, primary_key=True)
    id_equipamento = Column(Integer)
    dt_ocorrencia = Column(Date)
    txt_ocorrencia = Column(String(255))
    id_status = Column(SmallInteger,default=0)
    txt_acao = Column(String(255), default=None)
    txt_conclusao = Column(String(255), default=None)
    idtipo = Column(Integer,default=None)
    id_prioridade = Column(Integer, default=0)
    notificar = Column(Boolean)
    responsavel = Column(String(64), default=None)
    def __init__(self, id_ocorrencia, id_equipamento, dt_ocorrencia, txt_ocorrencia, id_status, txt_acao, txt_conclusao, idtipo, id_prioridade, notificar, responsavel):
        self.id_ocorrencia = id_ocorrencia
        self.id_equipamento = id_equipamento
        self.dt_ocorrencia = dt_ocorrencia
        self.txt_ocorrencia = txt_ocorrencia
        self.id_status = id_status
        self.txt_acao = txt_acao
        self.txt_conclusao = txt_conclusao
        self.idtipo = idtipo
        self.id_prioridade = id_prioridade
        self.notificar = notificar
        self.responsavel = responsavel


def getAllOcorrencias():
    return session.query(Ocorrencia).all()

def countAllStatus(status):
    return session.query(Ocorrencia.id_status).filter(Ocorrencia.id_status == status).count()

def getAllOcorrenciasRelatedEquipamento():
    statement = select([
            Ocorrencia.id_ocorrencia,
            Ocorrencia.txt_ocorrencia, 
            Ocorrencia.id_equipamento,
            Ocorrencia.dt_ocorrencia,
            Ocorrencia.id_status,
            Ocorrencia.txt_acao,
            Ocorrencia.txt_conclusao,
            Ocorrencia.idtipo,
            Ocorrencia.id_prioridade,
            Ocorrencia.notificar,
            Ocorrencia.responsavel,
            Equipamento.nome,
        ]).join(Ocorrencia, Ocorrencia.id_equipamento == Equipamento.idequipamento)
    result = session.execute(statement)
    ls = []
    for elements in result:
        ls.append(elements)
    return ls
#Equipamento.idequipamento,Equipamento.idunidade, Unidade.idclientes, Equipamento.nome.label('nome_equipamento'), Unidade.nome.label('nome_unidade'), Cliente.nome.label('nome_cliente')]).join(Unidade, Equipamento.idunidade == Unidade.idunidade).join(Cliente, Cliente.idclientes == Unidade.idclientes)
def getOcorrenciasRelatedEquipamentoById(id):
    
    
    query_equipamento = text("SELECT COUNT(*) FROM tbl_ocorrencia LEFT JOIN equipamentos ON tbl_ocorrencia.id_equipamento = equipamentos.idequipamento WHERE equipamentos.idequipamento is NULL AND tbl_ocorrencia.id_ocorrencia =:id ")
    result_equipamento = session.execute(query_equipamento,{'id':id}).scalar()
    query_unidade = text("SELECT COUNT(*) FROM equipamentos INNER JOIN tbl_ocorrencia ON equipamentos.idequipamento = tbl_ocorrencia.id_equipamento LEFT JOIN unidades ON unidades.idunidade = equipamentos.idunidade WHERE unidades.idunidade is NULL AND tbl_ocorrencia.id_ocorrencia = :id;")
    result_unidade = session.execute(query_unidade,{'id':id}).scalar()
    ls = []

    statement = select([
            Ocorrencia.id_ocorrencia,
            Ocorrencia.txt_ocorrencia, 
            Ocorrencia.id_equipamento,
            Ocorrencia.dt_ocorrencia,
            Ocorrencia.id_status,
            Ocorrencia.txt_acao,
            Ocorrencia.txt_conclusao,
            Ocorrencia.idtipo,
            Ocorrencia.id_prioridade,
            Ocorrencia.notificar,
            Ocorrencia.responsavel,
            Equipamento.nome.label("nome_equipamento"),
            Unidade.nome.label("nome_unidade"),
            Cliente.nome.label("nome_cliente")
        ]).filter(Ocorrencia.id_ocorrencia == id).join(Equipamento, Ocorrencia.id_equipamento == Equipamento.idequipamento).join(Unidade, Unidade.idunidade == Equipamento.idunidade).join(Cliente, Unidade.idclientes == Cliente.idclientes)
    result = session.execute(statement)

 
    if((result_equipamento == 1 or result_unidade == 1)):
        statement_none = select([
                Ocorrencia.id_ocorrencia,
                Ocorrencia.txt_ocorrencia, 
                Ocorrencia.id_equipamento,
                Ocorrencia.dt_ocorrencia,
                Ocorrencia.id_status,
                Ocorrencia.txt_acao,
                Ocorrencia.txt_conclusao,
                Ocorrencia.idtipo,
                Ocorrencia.id_prioridade,
                Ocorrencia.notificar,
                Ocorrencia.responsavel,
            ]).filter(Ocorrencia.id_ocorrencia == id)
        result = session.execute(statement_none)
        for elements in result:
            response = {
                            "id_ocorrencia": elements.id_ocorrencia,
                            "îd_equipamento": "Nenhum",
                            "îd_status": elements.id_status,
                            "txt_acao": elements.txt_acao,
                            "txt_conclusao": elements.txt_conclusao,
                            "îdtipo":elements.idtipo,
                            "îd_prioridade":elements.id_prioridade,
                            "notificar":elements.notificar,
                            "nome_equipamento": 'Nenhum',
                            "nome_cliente": "Nenhum",
                            "nome_unidade": "Nenhum",

                        }
            ls.append(response)     
        return ls
    
    for elements in result:
        ls.append(elements)
    return ls
''''
    if(has_nenhum == False):
        statement = select([
            Ocorrencia.id_ocorrencia,
            Ocorrencia.txt_ocorrencia, 
            Ocorrencia.id_equipamento,
            Ocorrencia.dt_ocorrencia,
            Ocorrencia.id_status,
            Ocorrencia.txt_acao,
            Ocorrencia.txt_conclusao,
            Ocorrencia.idtipo,
            Ocorrencia.id_prioridade,
            Ocorrencia.notificar,
            Ocorrencia.responsavel,
            Equipamento.nome.label("nome_equipamento"),
            Unidade.nome.label("nome_unidade")
        ]).filter(Ocorrencia.id_ocorrencia == id).join(Ocorrencia, Ocorrencia.id_equipamento == Equipamento.idequipamento).join(Unidade, Equipamento.idunidade == Unidade.idunidade)
        result = session.execute(statement)
        ls = []
        for elements in result:
            ls.append(elements.id_ocorrencia)
        return ls
        '''


def countByDateStatus(status, date_start):
    return session.query(Ocorrencia.id_status).filter(Ocorrencia.dt_ocorrencia == date_start).filter(Ocorrencia.id_status == status).count()

def countByDateIntervalStatus(status,date_start,date_end):
     return session.query(Ocorrencia.id_status).filter(Ocorrencia.dt_ocorrencia.between(date_start,date_end)).filter(Ocorrencia.id_status == status).count()