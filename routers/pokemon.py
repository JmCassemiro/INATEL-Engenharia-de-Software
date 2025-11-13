from fastapi import APIRouter, HTTPException
from services import pokemon_service
from fastapi import Query
from typing import Optional

router = APIRouter(prefix="/pokemon", tags=["pokemon"])

@router.get("/")
def listar_pokemons(limit: int = 100, offset: int = 0):
    return pokemon_service.listar_pokemons(limit, offset)

@router.get("/buscar")
def buscar_pokemon_query(nome: Optional[str] = Query(None)):
    # se quer comportamento de "aviso" como erro: lança 400
    if nome is None or not nome.strip():
        raise HTTPException(status_code=400, detail={"mensagem": "Digite o nome de algum Pokémon."})
    return pokemon_service.buscar_pokemon_por_nome(nome)


@router.get("/{nome}")
def buscar_pokemon_path(nome: str):
    return pokemon_service.buscar_pokemon_por_nome(nome)


@router.get("/tipo/{tipo}")
def listar_pokemons_por_tipo(tipo: str, limit: int = 20, offset: int = 0):
    return pokemon_service.listar_pokemons_por_tipo(tipo, limit, offset)
