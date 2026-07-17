

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackSetRequestAction(enum.StrEnum):
    DESCRIBE_STACK_SET = "DescribeStackSet"

    def visit(self, describe_stack_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackSetRequestAction.DESCRIBE_STACK_SET:
            return describe_stack_set()
