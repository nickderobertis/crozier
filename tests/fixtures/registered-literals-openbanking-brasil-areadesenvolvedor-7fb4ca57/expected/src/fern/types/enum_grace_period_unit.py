

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumGracePeriodUnit(enum.StrEnum):
    """
    Informar o critério de carência para a cobertura&#58;<br><ol><li>Dias</li><li>Meses</li><li>Não se aplica</li></ol>
    """

    DIAS = "DIAS"
    MESES = "MESES"
    NAO_APLICA = "NAO_APLICA"

    def visit(
        self,
        dias: typing.Callable[[], T_Result],
        meses: typing.Callable[[], T_Result],
        nao_aplica: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumGracePeriodUnit.DIAS:
            return dias()
        if self is EnumGracePeriodUnit.MESES:
            return meses()
        if self is EnumGracePeriodUnit.NAO_APLICA:
            return nao_aplica()
