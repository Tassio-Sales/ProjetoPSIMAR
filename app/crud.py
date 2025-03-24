# Importando a sessão do banco de dados e o modelo User
from sqlalchemy.orm import Session
from app.models import User
# Importando o esquema UserCreate para receber os dados de entrada
from app.schemas import UserCreate
# Biblioteca para criptografar a senha
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # Instanciando o contexto para criptografia de senhas usando bcrypt

# Função para criar um novo usuário no banco de dados
def create_user(db: Session, user: UserCreate):
    # Criptografando a senha antes de salvar no banco
    hashed_password = pwd_context.hash(user.senha)
    # Criando uma instância do modelo User com os dados fornecidos
    db_user = User(
        nome=user.nome,
        email=user.email,
        senha=hashed_password,
        aceitou_termos=user.aceitou_termos
    )
    db.add(db_user) # Adicionando o novo usuário à sessão do banco
    db.commit() # Comitando (salvando) a mudança no banco de dados
    db.refresh(db_user) # Atualizando o objeto db_user com os dados persistidos no banco
    return db_user # Retornando o usuário criado