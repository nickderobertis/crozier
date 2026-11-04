

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetSurvivalPensionContractDataModality(enum.StrEnum):
    """
    1. Contribuição Variável;
    2. Benefício Definido.
    """

    CONTRIBUICAO_VARIAVEL = "CONTRIBUICAO_VARIAVEL"
    BENEFICIO_DEFINIDO = "BENEFICIO_DEFINIDO"

    def visit(
        self, contribuicao_variavel: typing.Callable[[], T_Result], beneficio_definido: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetSurvivalPensionContractDataModality.CONTRIBUICAO_VARIAVEL:
            return contribuicao_variavel()
        if self is GetSurvivalPensionContractDataModality.BENEFICIO_DEFINIDO:
            return beneficio_definido()
