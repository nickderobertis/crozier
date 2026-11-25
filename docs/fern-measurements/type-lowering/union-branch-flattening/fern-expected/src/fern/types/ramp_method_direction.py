

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RampMethodDirection(enum.StrEnum):
    INBOUND = "inbound"

    def visit(self, inbound: typing.Callable[[], T_Result]) -> T_Result:
        if self is RampMethodDirection.INBOUND:
            return inbound()
