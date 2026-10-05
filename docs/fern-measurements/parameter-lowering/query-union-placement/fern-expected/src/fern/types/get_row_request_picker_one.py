

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRowRequestPickerOne(enum.StrEnum):
    EVENING = "evening"

    def visit(self, evening: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRowRequestPickerOne.EVENING:
            return evening()
