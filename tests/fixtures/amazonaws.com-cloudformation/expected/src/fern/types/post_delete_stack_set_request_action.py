

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeleteStackSetRequestAction(enum.StrEnum):
    DELETE_STACK_SET = "DeleteStackSet"

    def visit(self, delete_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDeleteStackSetRequestAction.DELETE_STACK_SET:
            return delete_stack_set()
