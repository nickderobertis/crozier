

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumTerm(enum.StrEnum):
    """
    Define o prazo do plano contratado<br><ol><li>Vitalícia</li><li>Temporária - prazo fixo</li><li>Temporária – intermitente</li></ol>
    """

    VITALICIA = "VITALICIA"
    TEMPORARIA_PRAZO_FIXO = "TEMPORARIA_PRAZO_FIXO"
    TEMPORARIA_INTERMITENTE = "TEMPORARIA_INTERMITENTE"

    def visit(
        self,
        vitalicia: typing.Callable[[], T_Result],
        temporaria_prazo_fixo: typing.Callable[[], T_Result],
        temporaria_intermitente: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumTerm.VITALICIA:
            return vitalicia()
        if self is EnumTerm.TEMPORARIA_PRAZO_FIXO:
            return temporaria_prazo_fixo()
        if self is EnumTerm.TEMPORARIA_INTERMITENTE:
            return temporaria_intermitente()
