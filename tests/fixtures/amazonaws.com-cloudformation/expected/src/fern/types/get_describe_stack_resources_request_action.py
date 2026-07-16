

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackResourcesRequestAction(enum.StrEnum):
    DESCRIBE_STACK_RESOURCES = "DescribeStackResources"

    def visit(self, describe_stack_resources: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackResourcesRequestAction.DESCRIBE_STACK_RESOURCES:
            return describe_stack_resources()
