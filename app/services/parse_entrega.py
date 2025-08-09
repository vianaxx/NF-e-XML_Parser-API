from app.schemas.entrega import EntregaCreate


def _parse_entrega(entrega: dict) -> EntregaCreate:
    """
    Faz o parse dos dados do destinatário da NF-e.

    :param entrega: Dicionário contendo os dados do destinatário.
    :return: Objeto DestinatarioCreate com os dados mapeados.
    """
    return EntregaCreate(
        cnpj=entrega.get("CNPJ", ""),
        nome=entrega.get("xNome", ""),
        ie=entrega.get("IE"),
        endereco=entrega.get("xLgr"),
        numero=entrega.get("nro"),
        bairro=entrega.get("xBairro"),
        municipio=entrega.get("xMun"),
        codigo_municipio=entrega.get("cMun"),
        uf=entrega.get("UF"),
        cep=entrega.get("CEP"),
        codigo_pais=entrega.get("cPais"),
        pais=entrega.get("xPais"),
    )
