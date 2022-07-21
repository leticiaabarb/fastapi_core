from fastapi import APIRouter
from schemas.ocorrencia import OcorrenciaSchema
from models.ocorrencia import Ocorrencia, getAllOcorrencias, countAllStatus, countByDateStatus, countByDateIntervalStatus, getAllOcorrenciasRelatedEquipamento, getOcorrenciasRelatedEquipamentoById
from typing import Optional, List
from fastapi_pagination import Page, add_pagination, paginate

router_ocorrencia = APIRouter() 

@router_ocorrencia.get('/ocorrencias', response_model=Page[OcorrenciaSchema] )
def list_all_ocorrencias():
    return paginate(getAllOcorrenciasRelatedEquipamento())

@router_ocorrencia.get('/ocorrencias-all', response_model=List[OcorrenciaSchema] )
def list_all_ocorrencias():
    return getAllOcorrenciasRelatedEquipamento()

@router_ocorrencia.get('/ocorrencias/{id}')
def list_all_ocorrencias(id: int):
    return getOcorrenciasRelatedEquipamentoById(id)

#@router_ocorrencia.get('/ocorrencias-equipamento', response_model=Page[OcorrenciaSchema] )
#def list_all_ocorrencias_equipamento():
#    return paginate(getAllOcorrenciasRelatedEquipamento())


@router_ocorrencia.get('/ocorrencias-count/')
def count_status(status: int, date:Optional[str]=None, date_start:Optional[str]=None, date_end:Optional[str]=None):
    if(date):
        return countByDateStatus(status,date)
    if(date_start and date_end):
        return countByDateIntervalStatus(status,date_start,date_end)
    return countAllStatus(status)

add_pagination(router_ocorrencia)

