

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeleteStackSetRequestAction(enum.StrEnum):
    DELETE_STACK_SET = "DeleteStackSet"

    def visit(self, delete_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeleteStackSetRequestAction.DELETE_STACK_SET:
            return delete_stack_set()
