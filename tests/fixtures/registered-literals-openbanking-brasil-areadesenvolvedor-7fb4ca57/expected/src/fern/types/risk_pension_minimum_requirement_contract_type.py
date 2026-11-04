

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskPensionMinimumRequirementContractType(enum.StrEnum):
    """
    O tipo de serviço contratado. A considerar os domínios abaixo&#58;<br><ol><li>Coletivo Averbado</li><li>Coletivo Instituído</li><li>Individual</li></ol>
    """

    COLETIVO_AVERBADO = "COLETIVO_AVERBADO"
    COLETIVO_INSTITUIDO = "COLETIVO_INSTITUIDO"
    INDIVIDUAL = "INDIVIDUAL"

    def visit(
        self,
        coletivo_averbado: typing.Callable[[], T_Result],
        coletivo_instituido: typing.Callable[[], T_Result],
        individual: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskPensionMinimumRequirementContractType.COLETIVO_AVERBADO:
            return coletivo_averbado()
        if self is RiskPensionMinimumRequirementContractType.COLETIVO_INSTITUIDO:
            return coletivo_instituido()
        if self is RiskPensionMinimumRequirementContractType.INDIVIDUAL:
            return individual()
