

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetSurvivalPensionContractDataSegment(enum.StrEnum):
    """
    Segmento do qual se trata o produto contratado
    1. Seguro de Pessoas
    2. Previdência
    """

    SEGURO_PESSOAS = "SEGURO_PESSOAS"
    PREVIDENCIA = "PREVIDENCIA"

    def visit(
        self, seguro_pessoas: typing.Callable[[], T_Result], previdencia: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetSurvivalPensionContractDataSegment.SEGURO_PESSOAS:
            return seguro_pessoas()
        if self is GetSurvivalPensionContractDataSegment.PREVIDENCIA:
            return previdencia()
