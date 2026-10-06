

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRowRequestPickerZero(enum.StrEnum):
    MORNING = "morning"

    def visit(self, morning: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRowRequestPickerZero.MORNING:
            return morning()
