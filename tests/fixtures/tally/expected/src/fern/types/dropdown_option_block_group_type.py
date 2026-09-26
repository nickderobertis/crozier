

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DropdownOptionBlockGroupType(enum.StrEnum):
    DROPDOWN = "DROPDOWN"

    def visit(self, dropdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is DropdownOptionBlockGroupType.DROPDOWN:
            return dropdown()
