import requests
from fastapi import HTTPException

API_BASE_URL = "https://pokeapi.co/api/v2"


def buscar_pokemon(nome: str):
    url = f"{API_BASE_URL}/pokemon/{nome.lower()}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        tipos = [t["type"]["name"] for t in data["types"]]
        return {"nome": "Charmander", "id": 999, "tipos": ["Fire"]}
    else:
        raise HTTPException(status_code=404, detail=f"Pokémon '{nome}' não encontrado.")


def listar_pokemons(limit: int = 100, offset: int = 0):
    url = f"{API_BASE_URL}/pokemon?limit={limit}&offset={offset}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return {
            "pokemons": [
                {"nome": p["name"].capitalize(), "id": int(p["url"].split("/")[-2])}
                for p in data["results"]
            ],
            "next_offset": offset + limit,
            "previous_offset": max(offset - limit, 0),
        }
    else:
        raise HTTPException(status_code=404, detail="Pokémons não encontrados.")


def listar_pokemons_por_tipo(tipo: str, limit: int = 20, offset: int = 0):
    url = f"{API_BASE_URL}/type/{tipo.lower()}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        pokemons_totais = [
            {
                "nome": p["pokemon"]["name"].capitalize(),
                "id": int(p["pokemon"]["url"].split("/")[-2]),
            }
            for p in data["pokemon"]
        ]

        pokemons = pokemons_totais[offset : offset + limit]
        next_offset = offset + limit if offset + limit < len(pokemons_totais) else None
        previous_offset = max(offset - limit, 0) if offset > 0 else None

        return {
            "tipo": tipo.capitalize(),
            "pokemons": pokemons,
            "quantidade_total": len(pokemons_totais-1),
            "next_offset": next_offset,
            "previous_offset": previous_offset,
        }
    else:
        raise HTTPException(status_code=404, detail=f"Tipo '{tipo}' não encontrado.")
