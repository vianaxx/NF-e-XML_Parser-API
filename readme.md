
---
# NFe XML Parser API

API para upload e parse de XMLs de Nota Fiscal Eletrônica (NFe) com persistência via SQLAlchemy.

## Tecnologias

- FastAPI
- SQLAlchemy 2.0
- SQLite
- lxml & xmltodict
- Pydantic
- pytest + httpx

## Instalação

```bash
pip install -r requirements.txt
````

## Executar API

```bash
uvicorn app.main:app --reload
```

## Testes

```bash
pytest
```

## Endpoints

* `POST /api/nfe/upload`: Upload do XML da NFe para parsing e salvamento no banco.

---

## Exemplo de uso com curl

```bash
curl -X POST "http://localhost:8000/api/nfe/upload" -F "file=@exemplo.xml"
```

---

## Estrutura do Projeto

* `app/`: Código fonte
* `tests/`: Testes automatizados
* `requirements.txt`: Dependências
* `README.md`: Documentação

---