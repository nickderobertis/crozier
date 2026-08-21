

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Prioridad(enum.StrEnum):
    """
    Nivel de prioridad asignado a la solicitud
    """

    ALTA = "ALTA"
    MEDIA = "MEDIA"
    BAJA = "BAJA"

    def visit(
        self,
        alta: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        baja: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Prioridad.ALTA:
            return alta()
        if self is Prioridad.MEDIA:
            return media()
        if self is Prioridad.BAJA:
            return baja()
