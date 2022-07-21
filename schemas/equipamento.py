
from dependencies.schema_dependencies import *

class EquipamentoSchema(BaseModel):
    idequipamento: int = Field(None,title="Identificador da tabela equipamento")
    idclientes: int
    idunidade: int = Field("Identificador da unidade",title="Identificador da unidade", description="Representa o identificador da tabela unidades")
    nome_equipamento: str = Field("Nome do equipamento", title="Nome do equipamento", description="Nome do equipamento")
    nome_unidade:str
    nome_cliente:str
    class Config:
        orm_mode = True