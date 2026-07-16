

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackInstanceRequestAction(enum.StrEnum):
    DESCRIBE_STACK_INSTANCE = "DescribeStackInstance"

    def visit(self, describe_stack_instance: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackInstanceRequestAction.DESCRIBE_STACK_INSTANCE:
            return describe_stack_instance()
