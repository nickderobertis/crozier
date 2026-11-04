

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionInvestimentFundTypePerformanceFee(enum.StrEnum):
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:
       - Tipo de taxa de performance
    """

    DIRETAMENTE = "DIRETAMENTE"
    INDIRETAMENTE = "INDIRETAMENTE"
    NAO_APLICA = "NAO_APLICA"

    def visit(
        self,
        diretamente: typing.Callable[[], T_Result],
        indiretamente: typing.Callable[[], T_Result],
        nao_aplica: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionInvestimentFundTypePerformanceFee.DIRETAMENTE:
            return diretamente()
        if self is SurvivalPensionInvestimentFundTypePerformanceFee.INDIRETAMENTE:
            return indiretamente()
        if self is SurvivalPensionInvestimentFundTypePerformanceFee.NAO_APLICA:
            return nao_aplica()
