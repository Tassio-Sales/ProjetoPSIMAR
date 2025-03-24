# Importando o roteador da FastAPI, dependências para acessar o banco de dados e HTTPException
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserResponse # Importando os esquemas necessários para validação
from app.crud import create_user # Importando a função que cria o usuário no banco

# Instanciando o roteador para o endpoint de usuários
router = APIRouter(prefix="/users", tags=["users"])

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para registrar um novo usuário
@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar se o usuário aceitou os termos
    if not user.aceitou_termos:
        raise HTTPException(status_code=400, detail="Os termos devem ser aceitos para cadastro.")
    existing_user = db.query(User).filter(User.email == user.email).first()     # Verificando se o email já está registrado no banco de dados
    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado") # Se o usuário já existe, lançar erro 400
    return create_user(db, user) # Se não existir, criar o novo usuário e retornar