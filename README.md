# Prerequisitos
- Instalar Python3
- Instalar MySQL
# Instalando
- Entrar no diretorio do projeto
- Primeiro criar um ambiente virtual venv, utilize o seguinte comando:
``` python3 -m venv venv ```
- Habilitar a venv com o comando: ```.\venv\Scripts\Activate```
- Instalar as dependencias necessarias: ``` pip install -r requirements.txt ````
## Banco de dados
- Definir uma senha e usuario no banco MySQL
- Executar os devidos arquivos SQL do banco de dados
- Na pasta core/env.py na linha 3 substituir <strong>root</strong> pelo usuiaro do banco e <strong>leticia123</strong> pela senha do banco criada anteriomente
- Proximo passo
## Executar API
- Dentro da pasta core, execute o seguinte comando: ``` uvicorn main:app --reload ```
- Acesse localhost:8000, se retornar um json com status ok! Entao aapi esta rodando, basta acessa-la agora.
                                              
