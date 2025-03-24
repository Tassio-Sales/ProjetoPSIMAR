from fastapi.testclient import TestClient # Importando o cliente de teste da FastAPI para simular requisições HTTP
from app.main import app # Importando a aplicação FastAPI que contém os endpoints

client = TestClient(app) # Criando um cliente para enviar requisições para a aplicação

def test_register_user(): # Função para testar o registro de um usuário
    # Enviando uma requisição POST para o endpoint de criação de usuários
    response = client.post("/users/", json={
        "nome": "Teste", # Nome do usuário
        "email": "teste@example.com", # Email do usuário
        "senha": "123456", # Senha do usuário
        "aceitou_termos": True # Aceitação dos termos
    })
    assert response.status_code == 200  # Verificando se a resposta tem o status 200 (sucesso)
    assert response.json()["email"] == "teste@example.com"  # Verificando se o email retornado na resposta é o mesmo enviado

    # Teste de cadastro de usuário com email duplicado
    def test_register_user_with_duplicate_email():
        # Primeiro, cria um usuário
        client.post("/users/", json={
            "nome": "Teste",
            "email": "duplicado@example.com",
            "senha": "123456",
            "aceitou_termos": True
        })
        # Agora tenta criar outro usuário com o mesmo email
        response = client.post("/users/", json={
            "nome": "Outro Teste",
            "email": "duplicado@example.com",
            "senha": "123456",
            "aceitou_termos": True
        })
        assert response.status_code == 400  # Espera erro devido ao email duplicado
        assert response.json()["detail"] == "Email já cadastrado"

    # Teste de validação de senha curta
    def test_register_user_with_short_password():
        response = client.post("/users/", json={
            "nome": "Teste",
            "email": "senhaCurta@example.com",
            "senha": "123",  # Senha muito curta
            "aceitou_termos": True
        })
        assert response.status_code == 422  # Erro de validação
        assert "A senha deve ter pelo menos 6 caracteres." in response.json()["detail"]

    # Teste de aceitação de termos
    def test_register_user_without_accepting_terms():
        response = client.post("/users/", json={
            "nome": "Teste",
            "email": "semTermos@example.com",
            "senha": "123456",
            "aceitou_termos": False  # Não aceitou os termos
        })
        assert response.status_code == 400  # Espera erro de termos não aceitos
        assert response.json()["detail"] == "Os termos devem ser aceitos para cadastro."