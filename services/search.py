from models.ocorrencia import Ocorrencia
from models.tipo_ocorrencia import TipoOcorrencia
from models.cliente import Cliente
from models.equipamento import Equipamento
from models.unidade import Unidade
from env import session


def searchEq(table,column,value):
    if(table.lower() == 'ocorrencia'):
        response = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) == value).all()
        count = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) == value).count()
        data = {'data': response, 'count':count}
        return data
    if(table.lower() == 'tipoocorrencia'):
        response = session.query(TipoOcorrencia).filter(getattr(TipoOcorrencia, column) == value)
        data = {'data': response.all(), 'count':response.count()}
        return data
    if(table.lower() == 'equipamento'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) == value)
        data = {'data': response.all(), 'count':response.count()}
        return data
    if(table.lower() == 'cliente'):
        response = session.query(Cliente).filter(getattr(Cliente, column) == value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'unidade'):
        response = session.query(Unidade).filter(getattr(Unidade, column) == value)
        data = {'data': response.all(), 'count':response.count()}
        return data

def searchGt(table,column,value):
    if(table.lower() == 'ocorrencia'):
        response = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) > value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'tipoocorrencia'):
        response = session.query(TipoOcorrencia).filter(getattr(TipoOcorrencia, column) > value)
        data = {'data': response.all(), 'count':response.count()}
        return data
        
    if(table.lower() == 'equipamento'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) > value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'cliente'):
        response = session.query(Cliente).filter(getattr(Cliente, column) > value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'unidade'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) > value)
        data = {'data': response.all(), 'count':response.count()}
        return data

def searchGe(table,column,value):
    if(table.lower() == 'ocorrencia'):
        response = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) >= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'tipoocorrencia'):
        response = session.query(TipoOcorrencia).filter(getattr(TipoOcorrencia, column) >= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'equipamento'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) >= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'cliente'):
        response = session.query(Cliente).filter(getattr(Cliente, column) >= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'unidade'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) >= value)
        data = {'data': response.all(), 'count':response.count()}
        return data


def searchLt(table,column,value):
    if(table.lower() == 'ocorrencia'):
        response = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'tipoocorrencia'):
        response = session.query(TipoOcorrencia).filter(getattr(TipoOcorrencia, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'equipamento'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'cliente'):
        response = session.query(Cliente).filter(getattr(Cliente, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'unidade'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

def searchLt(table,column,value):
    if(table.lower() == 'ocorrencia'):
        response = session.query(Ocorrencia).filter(getattr(Ocorrencia, column) <= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'tipoocorrencia'):
        response = session.query(TipoOcorrencia).filter(getattr(TipoOcorrencia, column) <= value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'equipamento'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data 

    if(table.lower() == 'cliente'):
        response = session.query(Cliente).filter(getattr(Cliente, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data

    if(table.lower() == 'unidade'):
        response = session.query(Equipamento).filter(getattr(Equipamento, column) < value)
        data = {'data': response.all(), 'count':response.count()}
        return data
    
    