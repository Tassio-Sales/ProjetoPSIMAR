# Importando BaseModel do Pydantic para validação de dados
from pydantic import  BaseModel, EmailStr, validator


# Esquema de criação de usuário com validação dos campos
class UserCreate(BaseModel):
    nome: str # Nome do usuário
    email: EmailStr # Email com validação do formato
    senha: str # Senha do usuário
    aceitou_termos: bool # Aceitação dos termos

    # Validador para garantir que a senha tenha no mínimo 6 caracteres
    @validator("senha")
    def validar_senha(cls, senha):
        if len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        return senha

# Esquema de resposta para exibir os dados do usuário
class UserResponse(BaseModel):
    id: int # ID do usuário
    nome: str # Nome do usuário
    email: EmailStr # Email do usuário
    is_admin: bool # Se o usuário é administrador

    # Configuração para permitir que o Pydantic use atributos diretamente do modelo
    class Config:
        from_attributes = True