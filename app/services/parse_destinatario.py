from app.schemas.destinatario import DestinatarioCreate


def _parse_destinatario(dest: dict) -> DestinatarioCreate:
    """
    Faz o parse dos dados do destinatário da NF-e.

    :param dest: Dicionário contendo os dados do destinatário.
    :return: Objeto DestinatarioCreate com os dados mapeados.
    """
    end = dest.get("enderDest", {})
    return DestinatarioCreate(
        cnpj=dest.get("CNPJ", ""),
        nome=dest.get("xNome", ""),
        ie=dest.get("IE"),
        endereco=end.get("xLgr"),
        numero=end.get("nro"),
        bairro=end.get("xBairro"),
        municipio=end.get("xMun"),
        codigo_municipio=end.get("cMun"),
        uf=end.get("UF"),
        cep=end.get("CEP"),
        codigo_pais=end.get("cPais"),
        pais=end.get("xPais"),
    )