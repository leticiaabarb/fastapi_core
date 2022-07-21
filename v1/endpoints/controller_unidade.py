from fastapi import APIRouter
from schemas.unidade import UnidadeSchema
from models.unidade import Unidade, getAllUnidades, getAllUnidadesRelatedClientes
from fastapi_pagination import Page, add_pagination, paginate                                                                                                                                                                                                                                                                                                                                                                                                                         
from typing import Dict,List

router_unidade = APIRouter()

@router_unidade.get('/unidades', response_model=Page[UnidadeSchema] )
def list_all_unidades():
    return paginate(getAllUnidades())

@router_unidade.get('/unidades-clientes', response_model=Page[UnidadeSchema])
def list_all_unidades_clientes():
    return paginate(getAllUnidadesRelatedClientes())

@router_unidade.get('/unidades-clientes-all', response_model=List[UnidadeSchema])
def list_all_unidades_clientes():
    return getAllUnidadesRelatedClientes()

@router_unidade.get('/unidades-all', response_model=List[UnidadeSchema] )
def list_all_unidades():
    return getAllUnidades()

add_pagination(router_unidade)



