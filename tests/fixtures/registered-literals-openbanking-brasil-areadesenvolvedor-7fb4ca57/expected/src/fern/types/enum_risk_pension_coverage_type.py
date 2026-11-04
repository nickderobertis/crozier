

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumRiskPensionCoverageType(enum.StrEnum):
    """
    É o conjunto dos riscos cobertos elencados na apólice. (RESOLUÇÃO CNSP Nº 341/2016). Listagem de coberturas incluídas no produto que deve observar a relação discriminada de coberturas, conforme Tabela Tipo de Cobertura.
    """

    MORTE = "MORTE"
    INVALIDEZ = "INVALIDEZ"
    OUTROS = "OUTROS"

    def visit(
        self,
        morte: typing.Callable[[], T_Result],
        invalidez: typing.Callable[[], T_Result],
        outros: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumRiskPensionCoverageType.MORTE:
            return morte()
        if self is EnumRiskPensionCoverageType.INVALIDEZ:
            return invalidez()
        if self is EnumRiskPensionCoverageType.OUTROS:
            return outros()
