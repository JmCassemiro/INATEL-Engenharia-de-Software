## Erros encontrados nos testes após PR

Durante a integração de um Pull Request, houve uma regressão no arquivo `services/pokemon_service.py` (linha 13).  
Isso fez com que dois testes falhassem:

- `test_buscar_pokemon_id`
- `test_buscar_pokemon_nome`

### Log do erro

AssertionError: assert 'Charmander' == 'Bulbasaur'
AssertionError: assert 'Charmander' == 'Pikachu'


### Causa
O PR alterou a lógica de busca de Pokémon, retornando **Charmander** como resultado padrão.  

### Solução
Ajustamos a lógica no `pokemon_service.py` para restaurar o comportamento correto, garantindo que os testes voltassem a passar.
