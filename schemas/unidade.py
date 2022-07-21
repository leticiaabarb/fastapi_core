
from dependencies.schema_dependencies import *

class UnidadeSchema(BaseModel):
    idclientes: int = Field(None,title="Identificador da tabela clientes")
    idunidade: int = Field(None,title="Identificador da unidade", description="Representa o identificador da tabela unidades")
    nome_unidade: str = Field(None,title="Nome da unidade", description="Nome da unidade")
    class Config:
        orm_mode = True