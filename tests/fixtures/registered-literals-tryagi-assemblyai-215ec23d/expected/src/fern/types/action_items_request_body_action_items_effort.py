

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionItemsRequestBodyActionItemsEffort(enum.StrEnum):
    LOW = "low"
    MEDIUM = "medium"

    def visit(self, low: typing.Callable[[], T_Result], medium: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActionItemsRequestBodyActionItemsEffort.LOW:
            return low()
        if self is ActionItemsRequestBodyActionItemsEffort.MEDIUM:
            return medium()
