from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/pokemon/{nome}")
def buscar_pokemon(nome: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        tipos = [t["type"]["name"] for t in dados["types"]]
        return {"nome": dados["name"].capitalize(), "id": dados["id"], "tipos": tipos}
    else:
        raise HTTPException(status_code=404, detail=f"Pokémon '{nome}' não encontrado.")


@app.get("/pokemon")
def listar_pokemons(limit: int = 100, offset: int = 0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return {
            "pokemons": [
                {
                    "nome": p["name"].capitalize(),
                    "id": int(p["url"].split("/")[-2])
                }
                for p in dados["results"]
            ],
            "next_offset": offset + limit,
            "previous_offset": max(offset - limit, 0)
        }
    else:
        raise HTTPException(status_code=404, detail="Pokémons não encontrados.")
    
@app.get("/pokemon/tipo/{tipo}")
def listar_pokemons_por_tipo(tipo: str):
    url = f"https://pokeapi.co/api/v2/type/{tipo.lower()}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        pokemons = [
            {
                "nome": p["pokemon"]["name"].capitalize(),
                "url": p["pokemon"]["url"]
            }
            for p in dados["pokemon"]
        ]
        return {"tipo": tipo.capitalize(), "pokemons": pokemons, "quantidade": len(pokemons)}
    else:
        raise HTTPException(status_code=404, detail=f"Tipo '{tipo}' não encontrado.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
