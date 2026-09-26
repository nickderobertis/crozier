

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolEntryFloor(enum.StrEnum):
    AUTO = "auto"
    MANUAL = "manual"

    def visit(self, auto: typing.Callable[[], T_Result], manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToolEntryFloor.AUTO:
            return auto()
        if self is ToolEntryFloor.MANUAL:
            return manual()
