

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackResourceRequestAction(enum.StrEnum):
    DESCRIBE_STACK_RESOURCE = "DescribeStackResource"

    def visit(self, describe_stack_resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackResourceRequestAction.DESCRIBE_STACK_RESOURCE:
            return describe_stack_resource()
