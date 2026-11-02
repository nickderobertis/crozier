

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HandoverOneOfEnumMode(enum.StrEnum):
    PICKUP = "pickup"

    def visit(self, pickup: typing.Callable[[], T_Result]) -> T_Result:
        if self is HandoverOneOfEnumMode.PICKUP:
            return pickup()
