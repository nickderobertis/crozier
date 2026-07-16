

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostUpdateStackRequestAction(enum.StrEnum):
    UPDATE_STACK = "UpdateStack"

    def visit(self, update_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostUpdateStackRequestAction.UPDATE_STACK:
            return update_stack()
