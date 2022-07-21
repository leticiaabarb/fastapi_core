from fastapi import APIRouter
from schemas.tipo_ocorrencia import TipoOcorrenciaSchema
from models.tipo_ocorrencia import TipoOcorrencia, getAllTipoOcorrencias
from typing import Dict,List

router_ocorrencia_tipo = APIRouter()

@router_ocorrencia_tipo.get('/tipo_ocorrencias', response_model=List[TipoOcorrenciaSchema] )
def list_all_tipo_ocorrencia():
    return getAllTipoOcorrencias()