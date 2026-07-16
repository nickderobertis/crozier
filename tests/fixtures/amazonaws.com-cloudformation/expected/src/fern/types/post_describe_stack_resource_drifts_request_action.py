

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackResourceDriftsRequestAction(enum.StrEnum):
    DESCRIBE_STACK_RESOURCE_DRIFTS = "DescribeStackResourceDrifts"

    def visit(self, describe_stack_resource_drifts: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackResourceDriftsRequestAction.DESCRIBE_STACK_RESOURCE_DRIFTS:
            return describe_stack_resource_drifts()
