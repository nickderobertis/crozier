

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackInstanceRequestAction(enum.StrEnum):
    DESCRIBE_STACK_INSTANCE = "DescribeStackInstance"

    def visit(self, describe_stack_instance: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackInstanceRequestAction.DESCRIBE_STACK_INSTANCE:
            return describe_stack_instance()
