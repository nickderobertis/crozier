

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionMinimumRequirementsContractType(enum.StrEnum):
    """
    O tipo de serviço contratado. A considerar os domínios abaixo:
    1. Coletivo Averbado;
    2. Individual.
    3. Ambas
    """

    COLETIVO = "COLETIVO"
    INDIVIDUAL = "INDIVIDUAL"
    AMBAS = "AMBAS"

    def visit(
        self,
        coletivo: typing.Callable[[], T_Result],
        individual: typing.Callable[[], T_Result],
        ambas: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionMinimumRequirementsContractType.COLETIVO:
            return coletivo()
        if self is SurvivalPensionMinimumRequirementsContractType.INDIVIDUAL:
            return individual()
        if self is SurvivalPensionMinimumRequirementsContractType.AMBAS:
            return ambas()
