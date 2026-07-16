

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackResourcesRequestAction(str, enum.Enum):
    DESCRIBE_STACK_RESOURCES = "DescribeStackResources"

    def visit(self, describe_stack_resources: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackResourcesRequestAction.DESCRIBE_STACK_RESOURCES:
            return describe_stack_resources()
