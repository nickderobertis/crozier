

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CanalOrigen(enum.StrEnum):
    """
    Canal de origen por el cual se recibió la solicitud
    """

    CSU = "CSU"
    EMAIL = "EMAIL"
    WEB = "WEB"
    SAC = "SAC"
    TELEFONICO = "TELEFONICO"
    PRESENCIAL = "PRESENCIAL"

    def visit(
        self,
        csu: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        web: typing.Callable[[], T_Result],
        sac: typing.Callable[[], T_Result],
        telefonico: typing.Callable[[], T_Result],
        presencial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CanalOrigen.CSU:
            return csu()
        if self is CanalOrigen.EMAIL:
            return email()
        if self is CanalOrigen.WEB:
            return web()
        if self is CanalOrigen.SAC:
            return sac()
        if self is CanalOrigen.TELEFONICO:
            return telefonico()
        if self is CanalOrigen.PRESENCIAL:
            return presencial()
