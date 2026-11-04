

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InsurancePensionEnumFinancialRegime(enum.StrEnum):
    """
    Listagem de regime financeiro para cada combinação de modalidade/cobertura do produto indicando:
      1. Repartição simples
      2. Repartição Capitais Cobertura
      3. Capitalização
    """

    REPARTICAO_SIMPLES = "REPARTICAO_SIMPLES"
    REPARTICAO_CAPITAIS = "REPARTICAO_CAPITAIS"
    CAPITALIZACAO = "CAPITALIZACAO"

    def visit(
        self,
        reparticao_simples: typing.Callable[[], T_Result],
        reparticao_capitais: typing.Callable[[], T_Result],
        capitalizacao: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InsurancePensionEnumFinancialRegime.REPARTICAO_SIMPLES:
            return reparticao_simples()
        if self is InsurancePensionEnumFinancialRegime.REPARTICAO_CAPITAIS:
            return reparticao_capitais()
        if self is InsurancePensionEnumFinancialRegime.CAPITALIZACAO:
            return capitalizacao()
