from env import Base,session
from dependencies.base_dependencies import *

class TipoOcorrencia(Base):
    __tablename__ = 'tbl_tipo_ocorrencia' #obrigatorio nome tabela
    idtipo = Column(Integer, primary_key=True)
    nmtipo = Column(String(255))
    def __init__(self, idtipo, nmtipo):
        self.idtipo = idtipo
        self.nmtipo = nmtipo
        
def getAllTipoOcorrencias():
    return session.query(TipoOcorrencia).all()