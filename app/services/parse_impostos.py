from decimal import Decimal
from typing import List

from app.schemas.imposto import ImpostoCreate


def _parse_impostos(imposto_data: dict) -> List[ImpostoCreate]:
    impostos = []

    def extrair_valor(tag: str, grupo: str, chave: str):
        valor = tag.get(chave)
        if valor:
            impostos.append(ImpostoCreate(
                tipo=grupo, grupo=grupo, chave=chave, valor=Decimal(valor)
            ))

    # ICMS
    icms = imposto_data.get("ICMS", {})
    for k, v in icms.items():
        if isinstance(v, dict):
            extrair_valor(v, "ICMS", "vICMS")

    # IPI
    ipi = imposto_data.get("IPI", {})
    if isinstance(ipi, dict):
        extrair_valor(ipi, "IPI", "vIPI")

    # PIS
    pis = imposto_data.get("PIS", {})
    if isinstance(pis, dict):
        extrair_valor(pis, "PIS", "vPIS")

    # COFINS
    cofins = imposto_data.get("COFINS", {})
    if isinstance(cofins, dict):
        extrair_valor(cofins, "COFINS", "vCOFINS")

    return impostos