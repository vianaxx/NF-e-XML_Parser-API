from decimal import Decimal, InvalidOperation

from app.schemas.produto import ProdutoCreate
from app.services.parse_impostos import _parse_impostos


def _parse_produto(item: dict) -> ProdutoCreate:
    """
    Faz o parse dos dados de um produto individual.

    :param item: Dicionário com os dados do produto.
    :return: Objeto ProdutoCreate com impostos associados.
    """
    prod = item.get("prod", {})
    impostos = _parse_impostos(item.get("imposto", {}))

    try:
        return ProdutoCreate(
            codigo=prod.get("cProd"),
            descricao=prod.get("xProd"),
            quantidade=Decimal(prod.get("qCom", "0")),
            valor_unitario=Decimal(prod.get("vUnCom", "0")),
            valor_total=Decimal(prod.get("vProd", "0")),
            impostos=impostos
        )
    except InvalidOperation as e:
        raise ValueError(f"Erro ao converter valores numéricos do produto: {e}")