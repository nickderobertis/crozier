

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceBootType(enum.StrEnum):
    V0 = "V0"
    V2 = "V2"

    def visit(self, v0: typing.Callable[[], T_Result], v2: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceBootType.V0:
            return v0()
        if self is ServiceBootType.V2:
            return v2()
