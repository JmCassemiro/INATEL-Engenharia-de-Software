# Pokédex FastAPI

Uma aplicação simples de Pokédex usando **FastAPI** no backend e HTML/CSS/JS no frontend, consumindo dados da [PokeAPI](https://pokeapi.co/).

## Funcionalidades

- Buscar informações de um Pokémon específico (nome, ID, tipos)
- Listar vários Pokémon por página (padrão: 100 por página)
- Navegar entre páginas de forma rápida

---

## Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- Requests
- Pipenv (gerenciamento de dependências)
- HTML / CSS / JS (frontend simples)

---

## Estrutura do Projeto

```
.
├── main.py              # Backend FastAPI
├── templates/
│   └── index.html       # Frontend
├── static/
│   └── style.css        # CSS
├── Pipfile              # Pipenv
├── Pipfile.lock
├── .gitignore
└── README.md
```

---

## Pré-requisitos

- Python 3.12 ou superior
- Pipenv instalado

```bash
pip install pipenv
```

---

## Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/JmCassemiro/INATEL-Engenharia-de-Software.git
cd <PASTA_DO_PROJETO>
```

### 2️⃣ Criar o ambiente virtual e instalar dependências

```bash
pipenv install
```

### 3️⃣ Ativar o ambiente virtual

```bash
pipenv shell
```

### 4️⃣ Executar a aplicação FastAPI

```bash
uvicorn main:app --reload
```

A aplicação vai rodar em [http://127.0.0.1:8000](http://127.0.0.1:8000)

O parâmetro `--reload` reinicia o servidor automaticamente ao alterar o código.

---

---

## Endpoints Disponíveis

- `GET /pokemon/{nome}` → retorna informações de um Pokémon específico
- `GET /pokemon?limit=100&offset=0` → retorna uma lista de Pokémon com paginação

---

## Configurações Adicionais

- Para alterar o número de Pokémon por página, modifique o parâmetro `limit` no endpoint ou no JS do frontend.
- Para alterar a configuração do Flake8, use o arquivo `.flake8`.
- O `.gitignore` já ignora caches Python, virtualenvs e arquivos temporários.

---

## Boas Práticas

- Use o ambiente virtual do Pipenv sempre que executar o projeto.