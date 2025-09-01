from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_buscar_pokemon_nome():
    response = client.get("/pokemon/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Pikachu"
    assert "id" in data
    assert "tipos" in data


def test_buscar_pokemon_id():
    response = client.get("/pokemon/1")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Bulbasaur"
    assert "id" in data
    assert "tipos" in data


def test_buscar_pokemon_id_invalido():
    response = client.get("/pokemon/99999999999")
    assert response.status_code == 404


def test_buscar_pokemon_nome_invalido():
    response = client.get("/pokemon/PedroVilas")
    assert response.status_code == 404
