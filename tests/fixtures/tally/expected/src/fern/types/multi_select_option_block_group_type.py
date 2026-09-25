

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiSelectOptionBlockGroupType(enum.StrEnum):
    MULTI_SELECT = "MULTI_SELECT"

    def visit(self, multi_select: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiSelectOptionBlockGroupType.MULTI_SELECT:
            return multi_select()
