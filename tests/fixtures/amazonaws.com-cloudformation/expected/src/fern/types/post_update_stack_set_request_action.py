

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostUpdateStackSetRequestAction(enum.StrEnum):
    UPDATE_STACK_SET = "UpdateStackSet"

    def visit(self, update_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostUpdateStackSetRequestAction.UPDATE_STACK_SET:
            return update_stack_set()
