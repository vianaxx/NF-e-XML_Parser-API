import xmltodict
from decimal import Decimal

from app.schemas.nfe import NFeCreate
from app.services.parse_destinatario import _parse_destinatario
from app.services.parse_emitente import _parse_emitente
from app.services.parse_nfe_base import _extrair_chave, _extrair_data_emissao
from app.services.parse_produto import _parse_produto
from app.services.parse_transportadora import _parse_transportadora


def parse_nfe_xml(xml_str: str) -> NFeCreate:
    """
    Faz o parse do XML de uma NF-e e retorna uma instância de NFeCreate.

    :param xml_str: Conteúdo do XML da NF-e como string.
    :return: Objeto NFeCreate com os dados extraídos.
    :raises ValueError: Se o XML estiver malformado ou faltando campos esperados.
    """
    try:
        doc = xmltodict.parse(xml_str)
    except Exception as e:
        raise ValueError(f"XML inválido: {e}")

    nfe = doc.get("nfeProc") or doc.get("NFe") or doc
    inf_nfe = nfe.get("NFe", {}).get("infNFe") or nfe.get("infNFe")
    if not inf_nfe:
        raise ValueError("Elemento 'infNFe' não encontrado")

    ide = inf_nfe.get("ide", {})
    emit = inf_nfe.get("emit", {})
    dest = inf_nfe.get("dest", {})
    det = inf_nfe.get("det", [])
    transp = inf_nfe.get("transp", {}).get("transporta", {})

    if isinstance(det, dict):
        det = [det]

    try:
        return NFeCreate(
            chave_acesso=_extrair_chave(inf_nfe),
            numero=ide.get("nNF", ""),
            serie=ide.get("serie", ""),
            data_emissao=_extrair_data_emissao(ide),
            valor_total=Decimal(inf_nfe.get("total", {}).get("ICMSTot", {}).get("vNF", "0")),
            emitente=_parse_emitente(emit),
            destinatario=_parse_destinatario(dest),
            transportadora=_parse_transportadora(transp),
            produtos=[_parse_produto(item) for item in det],
        )
    except Exception as e:
        raise ValueError(f"Erro ao processar dados da NF-e: {e}")









