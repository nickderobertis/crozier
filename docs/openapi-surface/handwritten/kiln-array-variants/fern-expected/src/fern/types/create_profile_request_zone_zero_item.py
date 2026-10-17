

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProfileRequestZoneZeroItem(enum.StrEnum):
    UPPER = "upper"

    def visit(self, upper: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProfileRequestZoneZeroItem.UPPER:
            return upper()
