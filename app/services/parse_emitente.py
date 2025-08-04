from app.schemas.emitente import EmitenteCreate


def _parse_emitente(emit: dict) -> EmitenteCreate:
    """
    Faz o parse dos dados do emitente da NF-e.

    :param emit: Dicionário contendo os dados do emitente.
    :return: Objeto EmitenteCreate com os dados mapeados.
    """
    end = emit.get("enderEmit", {})
    return EmitenteCreate(
        cnpj=emit.get("CNPJ", ""),
        nome=emit.get("xNome", ""),
        fantasia=emit.get("xFant"),
        ie=emit.get("IE"),
        crt=emit.get("CRT"),
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
