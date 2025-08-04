import xmltodict
from datetime import datetime
from decimal import Decimal
from app.schemas.nfe import NFeCreate
from app.schemas.emitente import EmitenteCreate
from app.schemas.destinatario import DestinatarioCreate
from app.schemas.transportadora import TransportadoraCreate
from app.schemas.produto import ProdutoCreate
from app.schemas.imposto import ImpostoCreate
from typing import List, Optional


def parse_nfe_xml(xml_str: str) -> NFeCreate:
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
    ender_emit = emit.get("enderEmit", {})
    dest = infNFe.get("dest", {})
    ender_dest = dest.get("enderDest", {})
    det = infNFe.get("det", [])

    if isinstance(det, dict):
        det = [det]

    # Emitente
    emitente = EmitenteCreate(
        cnpj=emit.get("CNPJ", ""),
        nome=emit.get("xNome", ""),
        fantasia=emit.get("xFant"),
        ie=emit.get("IE"),
        crt=emit.get("CRT"),
        endereco=ender_emit.get("xLgr"),
        numero=ender_emit.get("nro"),
        bairro=ender_emit.get("xBairro"),
        municipio=ender_emit.get("xMun"),
        codigo_municipio=ender_emit.get("cMun"),
        uf=ender_emit.get("UF"),
        cep=ender_emit.get("CEP"),
        codigo_pais=ender_emit.get("cPais"),
        pais=ender_emit.get("xPais"),
    )

    # Destinatario
    destinatario = DestinatarioCreate(
        cnpj=dest.get("CNPJ", ""),
        nome=dest.get("xNome", ""),
        ie=dest.get("IE"),
        endereco=ender_dest.get("xLgr"),
        numero=ender_dest.get("nro"),
        bairro=ender_dest.get("xBairro"),
        municipio=ender_dest.get("xMun"),
        codigo_municipio=ender_dest.get("cMun"),
        uf=ender_dest.get("UF"),
        cep=ender_dest.get("CEP"),
        codigo_pais=ender_dest.get("cPais"),
        pais=ender_dest.get("xPais"),
    )

    # Transportadora (opcional)
    transp = infNFe.get("transp", {}).get("transporta", {})
    transportadora = None
    if transp:
        transportadora = TransportadoraCreate(
            cnpj=transp.get("CNPJ"),
            cpf=transp.get("CPF"),
            nome=transp.get("xNome"),
            ie=transp.get("IE"),
            endereco=None
        )

    # Produtos e Impostos
    produtos: List[ProdutoCreate] = []
    for item in det:
        prod = item.get("prod", {})
        imposto_data = item.get("imposto", {})

        # Impostos (simplificado)
        impostos: List[ImpostoCreate] = []

        # ICMS
        icms = imposto_data.get("ICMS", {})
        if icms:
            for k, v in icms.items():
                if isinstance(v, dict):
                    valor = v.get("vICMS")
                    if valor:
                        impostos.append(ImpostoCreate(tipo="ICMS", grupo=k, chave="vICMS", valor=Decimal(valor)))

        # IPI
        ipi = imposto_data.get("IPI", {})
        if ipi:
            valor = ipi.get("vIPI")
            if valor:
                impostos.append(ImpostoCreate(tipo="IPI", grupo="IPI", chave="vIPI", valor=Decimal(valor)))

        # PIS
        pis = imposto_data.get("PIS", {})
        if pis:
            valor = pis.get("vPIS")
            if valor:
                impostos.append(ImpostoCreate(tipo="PIS", grupo="PIS", chave="vPIS", valor=Decimal(valor)))

        # COFINS
        cofins = imposto_data.get("COFINS", {})
        if cofins:
            valor = cofins.get("vCOFINS")
            if valor:
                impostos.append(ImpostoCreate(tipo="COFINS", grupo="COFINS", chave="vCOFINS", valor=Decimal(valor)))

        produto = ProdutoCreate(
            codigo=prod.get("cProd"),
            descricao=prod.get("xProd"),
            quantidade=Decimal(prod.get("qCom", "0")),
            valor_unitario=Decimal(prod.get("vUnCom", "0")),
            valor_total=Decimal(prod.get("vProd", "0")),
            impostos=impostos
        )
        produtos.append(produto)

    chave_acesso = infNFe.get("@Id", "")
    if chave_acesso.startswith("NFe"):
        chave_acesso = chave_acesso[3:]

    nfe_create = NFeCreate(
        chave_acesso=chave_acesso,
        numero=ide.get("nNF", ""),
        serie=ide.get("serie", ""),
        data_emissao=datetime.strptime(ide.get("dhEmi", ide.get("dEmi", "")), "%Y-%m-%dT%H:%M:%S%z") if ide.get(
            "dhEmi") else datetime.strptime(ide.get("dEmi", ""), "%Y-%m-%d"),
        valor_total=Decimal(infNFe.get("total", {}).get("ICMSTot", {}).get("vNF", "0")),
        produtos=produtos,
        transportadora=transportadora,
        emitente=emitente,
        destinatario=destinatario,
    )

    return nfe_create
