

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TipoSolicitud(enum.StrEnum):
    """
    Tipo de solicitud académica
    """

    REGISTRO = "REGISTRO"
    HOMOLOGACION = "HOMOLOGACION"
    CANCELACION = "CANCELACION"
    CUPOS = "CUPOS"
    CONSULTA = "CONSULTA"

    def visit(
        self,
        registro: typing.Callable[[], T_Result],
        homologacion: typing.Callable[[], T_Result],
        cancelacion: typing.Callable[[], T_Result],
        cupos: typing.Callable[[], T_Result],
        consulta: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TipoSolicitud.REGISTRO:
            return registro()
        if self is TipoSolicitud.HOMOLOGACION:
            return homologacion()
        if self is TipoSolicitud.CANCELACION:
            return cancelacion()
        if self is TipoSolicitud.CUPOS:
            return cupos()
        if self is TipoSolicitud.CONSULTA:
            return consulta()
