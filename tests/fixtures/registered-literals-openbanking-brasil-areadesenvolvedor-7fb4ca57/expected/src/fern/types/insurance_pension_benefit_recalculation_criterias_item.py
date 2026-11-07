

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InsurancePensionBenefitRecalculationCriteriasItem(enum.StrEnum):
    INDICE = "INDICE"
    VINCULADO_SALDO_DEVEDOR = "VINCULADO_SALDO_DEVEDOR"
    VARIAVEL_ACORDO_CRITERIO_ESPECIFICO = "VARIAVEL_ACORDO_CRITERIO_ESPECIFICO"

    def visit(
        self,
        indice: typing.Callable[[], T_Result],
        vinculado_saldo_devedor: typing.Callable[[], T_Result],
        variavel_acordo_criterio_especifico: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InsurancePensionBenefitRecalculationCriteriasItem.INDICE:
            return indice()
        if self is InsurancePensionBenefitRecalculationCriteriasItem.VINCULADO_SALDO_DEVEDOR:
            return vinculado_saldo_devedor()
        if self is InsurancePensionBenefitRecalculationCriteriasItem.VARIAVEL_ACORDO_CRITERIO_ESPECIFICO:
            return variavel_acordo_criterio_especifico()
