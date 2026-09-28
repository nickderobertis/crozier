

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyZeroType(enum.StrEnum):
    BINARY = "BINARY"

    def visit(self, binary: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyZeroType.BINARY:
            return binary()
