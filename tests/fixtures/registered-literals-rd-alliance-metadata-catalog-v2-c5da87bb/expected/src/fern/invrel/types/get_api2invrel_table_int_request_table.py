

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApi2InvrelTableIntRequestTable(enum.StrEnum):
    M = "m"
    G = "g"

    def visit(self, m: typing.Callable[[], T_Result], g: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApi2InvrelTableIntRequestTable.M:
            return m()
        if self is GetApi2InvrelTableIntRequestTable.G:
            return g()
