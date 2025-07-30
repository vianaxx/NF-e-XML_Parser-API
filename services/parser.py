import xmltodict
from datetime import datetime
from decimal import Decimal


def parse_nfe_xml(xml_str: str) -> dict:
    """
    Recebe XML NF-e como string e retorna dict estruturado
    com dados principais para persistência, incluindo produtos e impostos.
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
        print("\n=== IMPOSTO BRUTO ===")
        print(item.get("imposto"))

        # 🧾 Extrair impostos por produto
        impostos = []
        imposto_tag = item.get("imposto", {})
        for imposto_tipo, imposto_valores in imposto_tag.items():  # ICMS, IPI, PIS, COFINS...
            if isinstance(imposto_valores, dict):
                for grupo, dados in imposto_valores.items():  # ICMS10, IPITrib, PISAliq...
                    if isinstance(dados, dict):
                        for chave, valor in dados.items():
                            if chave.startswith("v") and valor:  # vICMS, vIPI, etc.
                                try:
                                    impostos.append({
                                        "tipo": imposto_tipo,
                                        "grupo": grupo,
                                        "chave": chave,
                                        "valor": Decimal(valor)
                                    })
                                except Exception:
                                    continue


        produtos.append({
            "codigo": prod.get("cProd"),
            "descricao": prod.get("xProd"),
            "quantidade": Decimal(prod.get("qCom", "0")),
            "valor_unitario": Decimal(prod.get("vUnCom", "0")),
            "valor_total": Decimal(prod.get("vProd", "0")),
            "impostos": impostos
        })

    # 🚚 Transportadora (opcional)
    transp = infNFe.get("transp", {}).get("transporta", {})
    transportadora = None
    if transp:
        transportadora = {
            "cnpj": transp.get("CNPJ"),
            "cpf": transp.get("CPF"),
            "nome": transp.get("xNome"),
            "ie": transp.get("IE"),
            "endereco": None  # Pode ser adaptado no futuro
        }

    # 🏭 Emitente
    emitente = {
        "cnpj": emit.get("CNPJ"),
        "nome": emit.get("xNome"),
        "endereco": emit.get("xLgr"),
        "ie": emit.get("IE"),

    }

    # 🧾 Destinatário
    destinatario = {
        "cnpj": dest.get("CNPJ"),
        "nome": dest.get("xNome"),
        "ie": dest.get("IE"),
        "endereco": None  # Pode ser detalhado depois
    }

    # 📆 Data de emissão
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
        "valor_total": Decimal(infNFe.get("total", {}).get("ICMSTot", {}).get("vNF", "0")),
        "produtos": produtos,
        "transportadora": transportadora,
        "emitente": emitente,
        "destinatario": destinatario
    }
