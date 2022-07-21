
from dependencies.schema_dependencies import *

class TipoOcorrenciaSchema(BaseModel):
    idtipo: int = Field(None,title="Îdentificador do  tipo  ocorrencia")
    nmtipo: str = Field("Troca para reparo",title="Nome do tipo da ocorrencia", description="Representa o nme do tipo da ocorrencia que ocorreu")
    class Config:
        orm_mode = True