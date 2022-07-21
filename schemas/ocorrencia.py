from datetime import date
from dependencies.schema_dependencies import *

class OcorrenciaSchema(BaseModel):
    id_ocorrencia: int = Field(None, title="Codigo do carro",description="Îdentifica a ocorrencia")
    id_equipamento: int = Field(None,title="Código do equipamento", description="Identifica o equipamento")
    dt_ocorrencia: date = Field(None, title="Data da ocorrencia", description="Data da ocorrencia") 
    txt_ocorrencia: str = Field(None, title="Conteúdo da ocorrência", description="Conteúdo da ocorrencia")
    id_status: int = Field(None, title="Codigo do status", description="Identifica o status") 
    txt_acao: str = Field(None, title="Conteudo da açao", description="Conteudo da açao") 
    txt_conclusao: str = Field(None, title="Conteudo da conclusão", description="Conteudo da conclusao") 
    idtipo: int = Field(None, title="Codigo do tipo", description="Identifica o tipo") 
    id_prioridade: int = Field(None, title="Codigo da prioridade", description="Identifica a prioridade")
    notificar: bool = Field(None, title="Notificação", description="Identificar se é necessário ser notificado")
    nome_equipamento: str = Field(None, title="Notificação", description="Identificar se é necessário ser notificado")
    responsavel: str = Field(None, title="Responsável", description="Notifica o responsável")
    nome_unidade:str = Field(None, title="Responsável", description="Notifica o responsável")
    nome_cliente:str = Field(None, title="Responsável", description="Notifica o responsável")


    class Config:
        orm_mode = True
