

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScaleType(enum.StrEnum):
    """
    Defines how scaling operations will be executed.
    """

    MANUAL = "manual"
    STANDARD = "standard"

    def visit(self, manual: typing.Callable[[], T_Result], standard: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScaleType.MANUAL:
            return manual()
        if self is ScaleType.STANDARD:
            return standard()
