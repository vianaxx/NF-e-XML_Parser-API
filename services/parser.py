import xmltodict
from datetime import datetime
from decimal import Decimal

def parse_nfe_xml(xml_str: str) -> dict:
    """
    Recebe XML NF-e como string e retorna dict estruturado
    com dados principais para persistência.
    """
    try:
        doc = xmltodict.parse(xml_str)
    except Exception as e:
        raise ValueError(f"XML inválido: {e}")

    nfe = doc.get("nfeProc") or doc.get("NFe") or doc
    infNFe = nfe.get("NFe", {}).get("infNFe") or nfe.get("infNFe")
    if not infNFe:
        raise ValueError("Não foi possível localizar o elemento infNFe")

    ide = infNFe.get("ide", {})
    emit = infNFe.get("emit", {})
    dest = infNFe.get("dest", {})
    det = infNFe.get("det", [])

    # Se só um produto, det pode ser dict em vez de lista
    if isinstance(det, dict):
        det = [det]

    produtos = []
    for item in det:
        prod = item.get("prod", {})
        produtos.append({
            "codigo": prod.get("cProd"),
            "descricao": prod.get("xProd"),
            "quantidade": Decimal(prod.get("qCom", "0")),
            "valor_unitario": Decimal(prod.get("vUnCom", "0")),
            "valor_total": Decimal(prod.get("vProd", "0")),
        })

    transp = infNFe.get("transp", {}).get("transporta", {})

    transportadora = None
    if transp:
        transportadora = {
            "cnpj": transp.get("CNPJ"),
            "cpf": transp.get("CPF"),
            "nome": transp.get("xNome"),
            "ie": transp.get("IE"),
            "endereco": None  # geralmente não vem diretamente, pode precisar ser obtido de outro lugar
        }


    data_emissao = ide.get("dhEmi") or ide.get("dEmi")
    if data_emissao and "T" in data_emissao:
        data_emissao = datetime.fromisoformat(data_emissao)
    elif data_emissao:
        data_emissao = datetime.strptime(data_emissao, "%Y-%m-%d")

    return {
        "chave_acesso": infNFe.get("@Id", "").replace("NFe", ""),
        "numero": ide.get("nNF"),
        "serie": ide.get("serie"),
        "data_emissao": data_emissao,
        "cnpj_emitente": emit.get("CNPJ"),
        "nome_emitente": emit.get("xNome"),
        "cnpj_destinatario": dest.get("CNPJ") or dest.get("CPF"),
        "nome_destinatario": dest.get("xNome"),
        "valor_total": Decimal(infNFe.get("total", {}).get("ICMSTot", {}).get("vNF", "0")),
        "produtos": produtos,
        "transportadora": transportadora,

    }
