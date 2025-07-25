import os

# Estrutura com arquivos dentro das pastas
structure = {
    "nfe_api": {
        "app": {
            "api": {
                "v1": {
                    "endpoints": [
                        "nfe_upload.py",
                        "nfe_query.py"
                    ],
                    "api_v1.py": None
                }
            },
            "core": [
                "config.py",
                "logging.py",
                "errors.py"
            ],
            "db": {
                "models": [
                    "nfe.py",
                    "product.py"
                ],
                "crud": [
                    "nfe.py"
                ],
                "__init__.py": None,
                "base.py": None,
                "session.py": None
            },
            "services": [
                "parser.py",
                "validator.py"
            ],
            "schemas": [
                "nfe.py",
                "product.py"
            ],
            "tests": [
                "test_nfe_upload.py",
                "test_nfe_query.py"
            ],
            "main.py": None
        },
        "alembic": {
            "versions": {}
        },
        "Dockerfile": None,
        "requirements.txt": None,
        "README.md": None
    }
}

def create_structure(base_path, struct):
    if isinstance(struct, dict):
        for key, value in struct.items():
            path = os.path.join(base_path, key)
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            create_structure(path, value)
    elif isinstance(struct, list):
        # lista de arquivos
        for file in struct:
            file_path = os.path.join(base_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    pass  # cria arquivo vazio
    elif struct is None:
        # cria arquivo
        if not os.path.exists(base_path):
            with open(base_path, "w", encoding="utf-8") as f:
                pass

if __name__ == "__main__":
    create_structure(".", structure)
    print("Estrutura de diretórios e arquivos criada com sucesso!")
