

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CopperKind(enum.StrEnum):
    COPPER = "copper"

    def visit(self, copper: typing.Callable[[], T_Result]) -> T_Result:
        if self is CopperKind.COPPER:
            return copper()
