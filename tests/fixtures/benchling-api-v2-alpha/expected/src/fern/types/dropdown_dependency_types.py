

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DropdownDependencyTypes(enum.StrEnum):
    DROPDOWN = "dropdown"

    def visit(self, dropdown: typing.Callable[[], T_Result]) -> T_Result:
        if self is DropdownDependencyTypes.DROPDOWN:
            return dropdown()
