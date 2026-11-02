

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HandoverAnyOfEnumMode(enum.StrEnum):
    PICKUP = "pickup"

    def visit(self, pickup: typing.Callable[[], T_Result]) -> T_Result:
        if self is HandoverAnyOfEnumMode.PICKUP:
            return pickup()
