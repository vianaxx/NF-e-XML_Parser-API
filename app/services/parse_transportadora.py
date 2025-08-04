from typing import Optional

from app.schemas.transportadora import TransportadoraCreate


def _parse_transportadora(transp: dict) -> Optional[TransportadoraCreate]:
    """
    Faz o parse dos dados da transportadora, se existirem.

    :param transp: Dicionário contendo os dados da transportadora.
    :return: Objeto TransportadoraCreate ou None.
    """
    if not transp:
        return None
    return TransportadoraCreate(
        cnpj=transp.get("CNPJ"),
        cpf=transp.get("CPF"),
        nome=transp.get("xNome"),
        ie=transp.get("IE"),
        endereco=None  # Endereço não incluído no XML
    )
