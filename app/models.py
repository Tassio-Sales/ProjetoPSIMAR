# Importando a classe Column do SQLAlchemy e Base de database.py
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

# Definindo o modelo de dados "User" para a tabela "users"
class User(Base):
    # Nome da tabela no banco de dados
    __tablename__ = "users"

    # Definição das colunas da tabela
    id = Column(Integer, primary_key=True, index=True) # ID do usuário
    nome = Column(String, index=True) # Nome do usuário
    email = Column(String, unique=True, index=True) # Email do usuário, único
    senha = Column(String) # Senha do usuário
    is_admin = Column(Boolean, default=False) # Verificação se é administrador
    aceitou_termos = Column(Boolean, default=False) # Verificação se aceitou os termos