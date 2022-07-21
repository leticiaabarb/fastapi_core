
from fastapi import APIRouter
from schemas.cliente import ClienteSchema
from models.cliente import Cliente, getAllClientes                                                                                                                                                                                                                                                                                                                                                                                                                    
from typing import Dict,List
from fastapi_pagination import Page, add_pagination, paginate



router_cliente = APIRouter()

@router_cliente.get('/clientes', response_model=Page[ClienteSchema] )
def list_all_clientes():
    return paginate(getAllClientes())

@router_cliente.get('/clientes-all', response_model=List[ClienteSchema] )
def list_all_clientes():
    return getAllClientes()


add_pagination(router_cliente)