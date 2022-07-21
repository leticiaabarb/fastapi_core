from fastapi import APIRouter
from schemas.equipamento import EquipamentoSchema
from models.equipamento import Equipamento, getAllEquipamentosDetail, getEquipamentosDetailById
from typing import Dict,List
from fastapi_pagination import Page, add_pagination, paginate

router_equipamento = APIRouter()

@router_equipamento.get('/equipamentos', response_model=Page[EquipamentoSchema] )
def list_all_equipamentos():
    return paginate(getAllEquipamentosDetail())

@router_equipamento.get('/equipamentos/{id}', response_model=List[EquipamentoSchema] )
def list_equipamentos_by_id(id: int):
    return getEquipamentosDetailById(id)


@router_equipamento.get('/equipamentos-all', response_model=List[EquipamentoSchema])
def list_all_equipamentos():
    return getAllEquipamentosDetail()

#@router_equipamento.get('/equipamentos-detail', response_model=Page[EquipamentoSchema])
#def list_all_equipamentos_related_unidade():
#    return paginate(getAllEquipamentosDetail())

add_pagination(router_equipamento)