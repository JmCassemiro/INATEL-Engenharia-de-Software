from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from services import pokemon_service

router = APIRouter(prefix="/pokemon", tags=["pokemon"])

@router.get("/")
def listar_pokemons(limit: int = 100, offset: int = 0):
    return pokemon_service.listar_pokemons(limit, offset)


@router.get("/{nome}")
def buscar_pokemon(nome: str):
    return pokemon_service.buscar_pokemon(nome)


@router.get("/tipo/{tipo}")
def listar_pokemons_por_tipo(tipo: str, limit: int = 20, offset: int = 0):
    return pokemon_service.listar_pokemons_por_tipo(tipo, limit, offset)
