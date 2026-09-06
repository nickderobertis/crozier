

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1SteamLoginRequestOpenidMode(enum.StrEnum):
    ID_RES = "id_res"

    def visit(self, id_res: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetV1SteamLoginRequestOpenidMode.ID_RES:
            return id_res()
