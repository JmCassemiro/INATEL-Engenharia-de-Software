# Pokédex FastAPI

Uma aplicação simples de Pokédex usando **FastAPI** no backend e HTML/CSS/JS no frontend, consumindo dados da [PokeAPI](https://pokeapi.co/).

O projeto permite:
- Buscar informações de um Pokémon específico (nome, ID, tipos).  
- Listar vários Pokémon por página (padrão 100 por página).  
- Navegar entre páginas de forma rápida.

---

## Tecnologias utilizadas

- Python 3.12+  
- FastAPI  
- Requests  
- Pipenv (gerenciamento de dependências)  
- HTML / CSS / JS (frontend simples)

---

## Estrutura do projeto

.
├── main.py # Backend FastAPI
├── templates/
│ └── index.html # Frontend
├── static/
│ └── style.css # CSS
├── Pipfile # Pipenv
├── Pipfile.lock
├── .gitignore
└── README.md

yaml
Copiar
Editar

---

## Pré-requisitos

- Python 3.12 ou superior  
- Pipenv instalado:  
```bash
pip install pipenv
Instalação e execução
1️⃣ Clonar o repositório

bash
Copiar
Editar
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>
2️⃣ Criar o ambiente virtual e instalar dependências

bash
Copiar
Editar
pipenv install
Isso vai ler o Pipfile e instalar todas as dependências (fastapi, uvicorn, requests, etc.).

3️⃣ Ativar o ambiente virtual

bash
Copiar
Editar
pipenv shell
4️⃣ Executar a aplicação FastAPI

bash
Copiar
Editar
uvicorn main:app --reload
A aplicação vai rodar em http://127.0.0.1:8000

O --reload reinicia o servidor automaticamente ao alterar o código.

Acessando o frontend
Abra o arquivo templates/index.html no navegador.

Ele vai consumir os endpoints do backend automaticamente.

Endpoints disponíveis
GET /pokemon/{nome} → retorna informações de um Pokémon específico

GET /pokemon?limit=100&offset=0 → retorna uma lista de Pokémon com paginação

Configurações adicionais
Para alterar o número de Pokémon por página, basta modificar o parâmetro limit no endpoint ou no JS do frontend.

Para alterar a configuração do Flake8, use o arquivo .flake8.

O .gitignore já ignora caches Python, virtualenvs e arquivos temporários.

Boas práticas
Use o ambiente virtual do Pipenv sempre que executar o projeto.

Execute o backend antes de abrir o frontend, para garantir que os dados sejam carregados.

Rodar flake8 . no projeto ajuda a manter o código limpo e seguindo PEP8.