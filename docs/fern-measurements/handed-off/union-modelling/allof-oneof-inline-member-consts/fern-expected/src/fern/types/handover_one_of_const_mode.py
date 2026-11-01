

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HandoverOneOfConstMode(enum.StrEnum):
    PICKUP = "pickup"

    def visit(self, pickup: typing.Callable[[], T_Result]) -> T_Result:
        if self is HandoverOneOfConstMode.PICKUP:
            return pickup()
