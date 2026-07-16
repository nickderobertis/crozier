

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostCreateStackSetRequestAction(enum.StrEnum):
    CREATE_STACK_SET = "CreateStackSet"

    def visit(self, create_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCreateStackSetRequestAction.CREATE_STACK_SET:
            return create_stack_set()
