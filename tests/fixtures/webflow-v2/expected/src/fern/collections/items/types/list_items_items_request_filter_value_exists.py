

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListItemsItemsRequestFilterValueExists(enum.StrEnum):
    TRUE = "true"
    FALSE = "false"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListItemsItemsRequestFilterValueExists.TRUE:
            return true()
        if self is ListItemsItemsRequestFilterValueExists.FALSE:
            return false()
