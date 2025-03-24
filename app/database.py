# Importando classes do SQLAlchemy para configuração do banco de dados
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db" # URL de conexão com o banco de dados (aqui usando SQLite local)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # Criação do engine de conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Criando a sessão para interagir com o banco de dados
Base = declarative_base() # Base para definir as tabelas no banco de dados

# Função para criar todas as tabelas definidas pelo SQLAlchemy
def create_tables():
    Base.metadata.create_all(bind=engine)