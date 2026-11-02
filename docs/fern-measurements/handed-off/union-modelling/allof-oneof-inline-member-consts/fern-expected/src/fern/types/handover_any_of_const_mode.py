

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HandoverAnyOfConstMode(enum.StrEnum):
    PICKUP = "pickup"

    def visit(self, pickup: typing.Callable[[], T_Result]) -> T_Result:
        if self is HandoverAnyOfConstMode.PICKUP:
            return pickup()
