# Importando o roteador da FastAPI e outras dependências necessárias
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database import SessionLocal
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"]) # Instanciando o roteador para o endpoint de autenticação
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Instanciando o contexto para criptografia de senhas com bcrypt

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal() # Criando a sessão local para a requisição
    try:
        yield db # Retorna a sessão para ser usada nas rotas
    finally:
        db.close() # Fechando a sessão após o uso


# Endpoint para resetar a senha de um usuário
@router.post("/reset-password")
def reset_password(email: str, nova_senha: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()     # Procurando o usuário pelo email no banco de dados
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")     # Se o usuário não for encontrado, lançar erro 404


    user.senha = pwd_context.hash(nova_senha)     # Atualizando a senha do usuário com a nova senha criptografada
    db.commit()
    return {"message": "Senha alterada com sucesso"} # Retornando a mensagem de sucesso