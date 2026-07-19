

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScType(enum.StrEnum):
    NATIVE = "NATIVE"
    MAPPED = "MAPPED"

    def visit(self, native: typing.Callable[[], T_Result], mapped: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScType.NATIVE:
            return native()
        if self is ScType.MAPPED:
            return mapped()
