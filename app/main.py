from fastapi import FastAPI # Importando a classe FastAPI do FastAPI para criar o aplicativo
from app.routers import users, auth # Importando os routers de usuários e autenticação
from app.database import create_tables # Função para criar as tabelas no banco de dados

app = FastAPI(title="PSIMAR - Atendimento Psicológico") # Criação da aplicação FastAPI com título personalizado


create_tables() # Criar tabelas no banco de dados ao iniciar a aplicação

# Incluir rotas da API para usuários e autenticação
app.include_router(users.router)
app.include_router(auth.router)

# Rota inicial para testar o funcionamento da API
@app.get("/")
def home():
    return {"message": "Bem-vindo ao PSIMAR"}
