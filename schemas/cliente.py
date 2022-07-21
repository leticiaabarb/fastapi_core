
from dependencies.schema_dependencies import *

class ClienteSchema(BaseModel):
    idclientes: int = Field(None,title="Identificador da tabela clientes")
    nome_cliente: str = Field("Nome da unidade", title="Nome da unidade", description="Nome da unidade")
    class Config:
        orm_mode = True