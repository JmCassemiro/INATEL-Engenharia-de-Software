from typing import Dict, Optional 
from fastapi import HTTPException 

from clients.pokemon_client import PokemonClient

client: PokemonClient = PokemonClient()


def buscar_pokemon_por_nome(nome: str) -> Optional[Dict]:
    if not nome or not nome.strip():
        raise HTTPException(status_code=400, detail="Nome do Pokémon não pode ser vazio.")
    data = client.get_pokemons_by_name(nome)
    if not data:
        raise HTTPException(status_code=404, detail=f"Pokémon '{nome}' não encontrado.")
    tipos = [t['type']['name'] for t in data.get('types', [])]
    return {"nome": data['name'].capitalize(), "id": data['id'], "tipos": tipos}


def listar_pokemons(limit: int = 100, offset: int = 0) -> Dict:
    if limit <= 0 or offset < 0:
        raise HTTPException(status_code=400, detail="Parâmetros inválidos: limit deve ser > 0 e offset >= 0.")
    data = client.get_pokemons(limit=limit, offset=offset)
    results = data.get("results", [])
    pokemons = [
        {"nome": p["name"].capitalize(), "id": int(p["url"].split("/")[-2])}
        for p in results
    ]
    # next_offset só quando houver mais itens no endpoint (simplificado)
    next_offset = offset + limit if len(results) == limit else None
    previous_offset = max(offset - limit, 0) if offset > 0 else None
    return {"pokemons": pokemons, "next_offset": next_offset, "previous_offset": previous_offset}


def listar_pokemons_por_tipo(tipo: str, limit: int = 20, offset: int = 0) -> Dict:
    if limit <= 0 or offset < 0:
        raise HTTPException(status_code=404, detail="Parâmetros inválidos: limit deve ser > 0 e offset >= 0.")
    data = client.get_pokemons_by_type(tipo)
    if not data:
        # tipo não encontrado → lançar exceção HTTP 404
        raise HTTPException(status_code=404, detail=f"Tipo '{tipo}' não encontrado.")
    pokemons_totais = [
        {"nome": p["pokemon"]["name"].capitalize(), "id": int(p["pokemon"]["url"].split("/")[-2])}
        for p in data.get("pokemon", [])
    ]
    pokemons = pokemons_totais[offset: offset + limit]
    next_offset = offset + limit if offset + limit < len(pokemons_totais) else None
    previous_offset = max(offset - limit, 0) if offset > 0 else None
    return {"tipo": tipo.capitalize(), "pokemons": pokemons, "quantidade_total": len(pokemons_totais), "next_offset": next_offset, "previous_offset": previous_offset}