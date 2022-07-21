from fastapi import FastAPI as api
from v1.endpoints.controller_ocorrencia import router_ocorrencia
from v1.endpoints.controller_tipo_ocorrencia import router_ocorrencia_tipo
from v1.endpoints.controller_equipamento import router_equipamento
from v1.endpoints.controller_unidade import router_unidade
from v1.endpoints.controller_cliente import router_cliente
from v1.endpoints.controller_search import router_search
from fastapi.middleware.cors import CORSMiddleware



app = api()
app.include_router(router_ocorrencia, prefix='/v1')
app.include_router(router_ocorrencia_tipo, prefix='/v1')
app.include_router(router_equipamento, prefix='/v1')
app.include_router(router_unidade, prefix='/v1')
app.include_router(router_cliente, prefix='/v1')
app.include_router(router_search, prefix='/v1')

origins = [
    "http://localost",
    "http://localhost:8000",
    "http://localhost:8080",
    "*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def index():
    return {'status': 'OK!'}