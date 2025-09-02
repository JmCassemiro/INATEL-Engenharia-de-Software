from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_buscar_pokemon_id():
    response = client.get("/pokemon/1")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Bulbasaur"
    assert "id" in data
    assert "tipos" in data


def test_buscar_pokemon_nome():
    response = client.get("/pokemon/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Pikachu"
    assert "id" in data
    assert "tipos" in data


def test_listar_pokemons():
    response = client.get("/pokemon/")
    assert response.status_code == 200
    data = response.json()
    assert "pokemons" in data
    assert "next_offset" in data
    assert "previous_offset" in data


def test_listar_pokemons_por_tipo():
    response = client.get("/pokemon/tipo/fire")
    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "Fire"
    assert "pokemons" in data
    assert "next_offset" in data
    assert "previous_offset" in data


def test_listar_pokemons_por_tipo_invalido():
    response = client.get("/pokemon/tipo/invalido")
    assert response.status_code == 404
    assert response.json()["detail"] == "Tipo 'invalido' não encontrado."


def test_buscar_pokemon_id_invalido():
    response = client.get("/pokemon/99999999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon '99999999999' não encontrado."


def test_buscar_pokemon_nome_invalido():
    response = client.get("/pokemon/PedroVilas")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pokémon 'PedroVilas' não encontrado."

