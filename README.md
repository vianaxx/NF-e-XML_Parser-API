
---
# NFe XML Parser API

Este projeto implementa uma API para o processamento e armazenamento de Notas Fiscais Eletrônicas (NF-e) a partir de arquivos XML. Ele realiza o parsing dos XMLs, extrai dados relevantes como emitente, destinatário, transportadora, produtos e impostos, e salva essas informações em um banco de dados relacional utilizando SQLAlchemy.

---

## Tecnologias

- FastAPI
- SQLAlchemy 2.0
- SQLite
- lxml & xmltodict
- Pydantic
- pytest + httpx

---

## Funcionalidades

- Parser robusto para arquivos XML da NF-e (versão 4.00).
- Modelagem relacional com entidades: Emitente, Destinatário, Transportadora, NF-e, Produto e Imposto.
- Validação para evitar duplicidade de registros (emitente, destinatário, transportadora e NF-e).
- Criação automática ou reutilização de entidades relacionadas ao salvar uma NF-e.
- Relacionamentos via chaves estrangeiras para garantir integridade referencial.
- Exemplo de uso com SQLite, mas pode ser adaptado para outros bancos.

---

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

## Estrutura do Projeto

* `app/`: Código fonte
* `tests/`: Testes automatizados
* `requirements.txt`: Dependências
* `README.md`: Documentação

---
