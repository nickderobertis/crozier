

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Types(enum.StrEnum):
    UNKNOWN = "Unknown"

    def visit(self, unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is Types.UNKNOWN:
            return unknown()
