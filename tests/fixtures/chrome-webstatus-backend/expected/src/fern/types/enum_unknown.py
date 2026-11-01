

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumUnknown(enum.StrEnum):
    """
    Represents an unknown, unsupported, or deprecated enum value.
    """

    UNKNOWN = "unknown"

    def visit(self, unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is EnumUnknown.UNKNOWN:
            return unknown()
