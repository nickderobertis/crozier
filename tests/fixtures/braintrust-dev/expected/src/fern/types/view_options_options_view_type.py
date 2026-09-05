

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ViewOptionsOptionsViewType(enum.StrEnum):
    MONITOR = "monitor"

    def visit(self, monitor: typing.Callable[[], T_Result]) -> T_Result:
        if self is ViewOptionsOptionsViewType.MONITOR:
            return monitor()
