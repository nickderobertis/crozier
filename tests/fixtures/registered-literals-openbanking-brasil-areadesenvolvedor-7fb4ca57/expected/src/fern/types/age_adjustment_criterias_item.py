

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgeAdjustmentCriteriasItem(enum.StrEnum):
    """
    Critério escolhido para reenquadramento etário
      1. Após período em anos
      2. A cada período em anos
      3. Por mudança de faixa etária
      4. Não aplicável
    """

    APOS_PERIODO_ANOS = "APOS_PERIODO_ANOS"
    CADA_PERIODO_ANOS = "CADA_PERIODO_ANOS"
    MUDANCA_FAIXA_ETARIA = "MUDANCA_FAIXA_ETARIA"
    NAO_APLICAVEL = "NAO_APLICAVEL"

    def visit(
        self,
        apos_periodo_anos: typing.Callable[[], T_Result],
        cada_periodo_anos: typing.Callable[[], T_Result],
        mudanca_faixa_etaria: typing.Callable[[], T_Result],
        nao_aplicavel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgeAdjustmentCriteriasItem.APOS_PERIODO_ANOS:
            return apos_periodo_anos()
        if self is AgeAdjustmentCriteriasItem.CADA_PERIODO_ANOS:
            return cada_periodo_anos()
        if self is AgeAdjustmentCriteriasItem.MUDANCA_FAIXA_ETARIA:
            return mudanca_faixa_etaria()
        if self is AgeAdjustmentCriteriasItem.NAO_APLICAVEL:
            return nao_aplicavel()
