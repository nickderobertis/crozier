

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InsurancePensionEnumIndemnifiablePeriodType(enum.StrEnum):
    """
    Listagem do pagamento para cada benefício:
      1. Quantidade determinada de parcelas;
      2. Até o fim de ciclo determinado.
    Se for pagamento único, esse campo não se aplica (retorna vazio).
    """

    QUANTIDADE_DETERMINADA_PARCELAS = "QUANTIDADE_DETERMINADA_PARCELAS"
    FIM_CICLO_DETERMINADO = "FIM_CICLO_DETERMINADO"

    def visit(
        self,
        quantidade_determinada_parcelas: typing.Callable[[], T_Result],
        fim_ciclo_determinado: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InsurancePensionEnumIndemnifiablePeriodType.QUANTIDADE_DETERMINADA_PARCELAS:
            return quantidade_determinada_parcelas()
        if self is InsurancePensionEnumIndemnifiablePeriodType.FIM_CICLO_DETERMINADO:
            return fim_ciclo_determinado()
