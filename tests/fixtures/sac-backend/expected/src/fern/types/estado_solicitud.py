

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EstadoSolicitud(enum.StrEnum):
    """
    Estado actual en el ciclo de vida de la solicitud.
    Transiciones válidas: REGISTRADA → CLASIFICADA → EN_ATENCION → ATENDIDA → CERRADA
    """

    REGISTRADA = "REGISTRADA"
    CLASIFICADA = "CLASIFICADA"
    EN_ATENCION = "EN_ATENCION"
    ATENDIDA = "ATENDIDA"
    CERRADA = "CERRADA"

    def visit(
        self,
        registrada: typing.Callable[[], T_Result],
        clasificada: typing.Callable[[], T_Result],
        en_atencion: typing.Callable[[], T_Result],
        atendida: typing.Callable[[], T_Result],
        cerrada: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EstadoSolicitud.REGISTRADA:
            return registrada()
        if self is EstadoSolicitud.CLASIFICADA:
            return clasificada()
        if self is EstadoSolicitud.EN_ATENCION:
            return en_atencion()
        if self is EstadoSolicitud.ATENDIDA:
            return atendida()
        if self is EstadoSolicitud.CERRADA:
            return cerrada()
