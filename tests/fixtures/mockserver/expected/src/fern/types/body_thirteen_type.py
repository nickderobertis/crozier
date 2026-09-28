

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyThirteenType(enum.StrEnum):
    BINARY = "BINARY"

    def visit(self, binary: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyThirteenType.BINARY:
            return binary()
