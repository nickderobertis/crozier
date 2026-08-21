

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RolUsuario(enum.StrEnum):
    """
    Rol de usuario que determina los permisos
    """

    ADMINISTRADOR = "ADMINISTRADOR"
    GESTOR = "GESTOR"
    SOLICITANTE = "SOLICITANTE"

    def visit(
        self,
        administrador: typing.Callable[[], T_Result],
        gestor: typing.Callable[[], T_Result],
        solicitante: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RolUsuario.ADMINISTRADOR:
            return administrador()
        if self is RolUsuario.GESTOR:
            return gestor()
        if self is RolUsuario.SOLICITANTE:
            return solicitante()
