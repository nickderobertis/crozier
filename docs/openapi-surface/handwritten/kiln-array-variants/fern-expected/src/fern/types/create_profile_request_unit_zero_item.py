

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProfileRequestUnitZeroItem(enum.StrEnum):
    CELSIUS = "celsius"

    def visit(self, celsius: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProfileRequestUnitZeroItem.CELSIUS:
            return celsius()
