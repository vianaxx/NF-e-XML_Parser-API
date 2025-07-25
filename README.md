# NF-e XML Parser API

API RESTful desenvolvida em FastAPI para importar, extrair e consultar dados de pedidos a partir de arquivos XML da Nota Fiscal Eletrônica (NF-e).

## O que foi feito até agora

- Estrutura modular do projeto, separando camadas de API, banco de dados, serviços, schemas e configuração.
- Configuração do banco SQLite com SQLAlchemy ORM, modelos para NF-e e produtos relacionados.
- Endpoint para upload de arquivos XML contendo NF-e.
- Parser XML robusto utilizando `xmltodict` para extrair os principais dados da NF-e:
  - Chave de acesso, número, série, data de emissão.
  - Dados do emitente e destinatário.
  - Lista de produtos, quantidades e valores.
- Criação automática das tabelas no banco na inicialização da aplicação.
- Validação de dados com Pydantic schemas para garantir integridade e padronização.
- Projeto estruturado para fácil manutenção e expansão.

## O que está planejado / próximos passos

- Persistência dos dados extraídos no banco de dados com transações seguras.
- Desenvolvimento de rotas para consulta das NF-e armazenadas, com filtros por chave, CNPJ, data etc.
- Implementação de testes automatizados (unitários e de integração) para garantir qualidade.
- Validação do XML contra o esquema oficial NF-e (XSD).
- Tratamento global e consistente de erros e exceções.
- Migrações de banco de dados com Alembic para versionamento do schema.
- Suporte a bancos mais robustos (PostgreSQL, MySQL).
- Configuração e uso de variáveis de ambiente para diferentes ambientes (dev, prod).
- Melhoria na segurança do upload (limite de tamanho, validação).
- Documentação detalhada da API com exemplos e descrição dos endpoints.

---

## Como rodar localmente

1. Clone o repositório:

```bash
git clone  https://github.com/vianaxx/NF-e-XML_Parser-API
cd NF-e-XML_Parser-API
````

2. Crie e ative um ambiente virtual Python:

```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Rode a aplicação:

```bash
uvicorn main:app --reload
```

5. Acesse a documentação interativa da API em:

```
http://127.0.0.1:8000/docs
```

---

## Tecnologias e bibliotecas utilizadas

* Python 3.11+
* FastAPI
* Uvicorn (servidor ASGI)
* SQLAlchemy (ORM)
* SQLite (banco de dados local)
* Pydantic (validação e schemas)
* xmltodict (parsing XML)

---

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue ou envie um pull request.

---

**Desenvolvido com ❤️ por \[Seu Nome / Seu GitHub]**
