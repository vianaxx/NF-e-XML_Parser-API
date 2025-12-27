# 🇧🇷 NF-e XML Parser API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-grey?style=flat-square)

Uma API robusta e de alta performance para processamento, validação e armazenamento de Notas Fiscais Eletrônicas (NF-e) a partir de arquivos XML. O projeto foi construído seguindo princípios de **Clean Architecture** e **S.O.L.I.D**, garantindo modularidade, facilidade de manutenção e escalabilidade.

---

## 🚀 Funcionalidades

- **Parsing Inteligente**: Extração eficiente de dados de XMLs da NF-e (v4.00) utilizando `xmltodict`.
- **Modelagem Relacional**: Estrutura de banco de dados normalizada com entidades para `Emitente`, `Destinatário`, `Transportadora`, `Produtos` e `Impostos`.
- **Transações Atômicas**: Integridade de dados garantida. Se uma parte do salvamento falhar, nada é persistido.
- **Validação de Dados**: Uso de Pydantic para validar schemas de entrada e saída.
- **Idempotência**: Verifica duplicidades antes de inserir, evitando registros redundantes de entidades.

---

## 🛠️ Stack Tecnológica

- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) - Moderno, rápido e com documentação automática.
- **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) - Mapeamento objeto-relacional poderoso.
- **Banco de Dados**: SQLite (padrão) / Extensível para PostgreSQL/MySQL.
- **Parsing**: `xmltodict` e `lxml`.
- **Testes**: `pytest` e `httpx`.

---

## 📂 Estrutura do Projeto

O projeto segue uma estrutura modular clara:

```
app/
├── api/          # Rotas e endpoints da API
├── core/         # Configurações globais (env vars)
├── db/           # Configuração do banco e modelos ORM
│   ├── crud/     # Camada de acesso a dados (Repository pattern)
│   └── models/   # Definição das tabelas
├── schemas/      # Modelos Pydantic (Request/Response)
├── services/     # Regras de negócio e lógicas de parsing isoladas
└── tests/        # Testes de integração e unitários
```

---

## ⚡ Como Rodar

### Pré-requisitos
- Python 3.10 ou superior
- Pip

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/vianaxx/NF-e-XML_Parser-API.git
   cd NF-e-XML_Parser-API
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuração**
   O projeto usa um arquivo `.env` para configurações. Cria um arquivo `.env` na raiz (ou renomeie um exemplo) se necessário. Por padrão, ele usará um banco SQLite local.

### Executando a APIService

```bash
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: **http://127.0.0.1:8000/docs**

---

## 🧪 Testes

Para rodar a suíte de testes automatizados:

```bash
pytest
```

---

## 🔌 Endpoints Principais

### `POST /api/nfe/upload`
Envia um arquivo XML para processamento.

- **Request**: `multipart/form-data`, campo `file` (arquivo .xml).
- **Response**:
  ```json
  {
    "message": "Nota fiscal processada com sucesso"
  }
  ```

---
