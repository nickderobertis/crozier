

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetUpdateStackRequestAction(enum.StrEnum):
    UPDATE_STACK = "UpdateStack"

    def visit(self, update_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateStackRequestAction.UPDATE_STACK:
            return update_stack()
