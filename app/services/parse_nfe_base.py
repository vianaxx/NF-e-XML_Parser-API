from datetime import datetime


def _extrair_chave(inf_nfe: dict) -> str:
    chave = inf_nfe.get("@Id", "")
    return chave[3:] if chave.startswith("NFe") else chave


def _extrair_data_emissao(ide: dict) -> datetime:
    if "dhEmi" in ide:
        return datetime.strptime(ide["dhEmi"], "%Y-%m-%dT%H:%M:%S%z")
    elif "dEmi" in ide:
        return datetime.strptime(ide["dEmi"], "%Y-%m-%d")
    raise ValueError("Data de emissão não encontrada")