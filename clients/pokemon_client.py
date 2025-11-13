import requests

from typing import Any, Dict, Optional

class PokemonClient:
    def __init__(self, base_url: str = "https://pokeapi.co/api/v2", timeout: int = 10):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout


    def get_pokemons_by_name(self, nome: str) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/pokemon/{nome.lower()}"
        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            return None
        resp.raise_for_status()


    def get_pokemons(self, limit: int = 100, offset: int = 0) -> Dict[str, Any]:
        url = f"{self.base_url}/pokemon"
        resp = self.session.get(url, params={"limit": limit, "offset": offset}, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()
    

    def get_pokemons_by_type(self, tipo: str) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/type/{tipo.lower()}"
        resp = self.session.get(url, timeout=self.timeout)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            return None
        resp.raise_for_status()