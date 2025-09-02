from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import home, pokemon

app = FastAPI(title="Pokedex do Jm")


app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(home.router)
app.include_router(pokemon.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
