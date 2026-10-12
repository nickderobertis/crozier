

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Traction(enum.StrEnum):
    OVERHEAD = "overhead"
    BATTERY = "battery"

    def visit(self, overhead: typing.Callable[[], T_Result], battery: typing.Callable[[], T_Result]) -> T_Result:
        if self is Traction.OVERHEAD:
            return overhead()
        if self is Traction.BATTERY:
            return battery()
