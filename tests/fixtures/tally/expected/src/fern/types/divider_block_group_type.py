

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DividerBlockGroupType(enum.StrEnum):
    DIVIDER = "DIVIDER"

    def visit(self, divider: typing.Callable[[], T_Result]) -> T_Result:
        if self is DividerBlockGroupType.DIVIDER:
            return divider()
