

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRiskPensionContractDataOtherGuaranteedValuesItem(enum.StrEnum):
    """
    1. Saldamento
    2. Benefício Prolongado
    3. Não se aplica
    """

    SALDAMENTO = "SALDAMENTO"
    BENEFICIO_PROLONGADO = "BENEFICIO_PROLONGADO"
    NAO_APLICA = "NAO_APLICA"

    def visit(
        self,
        saldamento: typing.Callable[[], T_Result],
        beneficio_prolongado: typing.Callable[[], T_Result],
        nao_aplica: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRiskPensionContractDataOtherGuaranteedValuesItem.SALDAMENTO:
            return saldamento()
        if self is GetRiskPensionContractDataOtherGuaranteedValuesItem.BENEFICIO_PROLONGADO:
            return beneficio_prolongado()
        if self is GetRiskPensionContractDataOtherGuaranteedValuesItem.NAO_APLICA:
            return nao_aplica()
