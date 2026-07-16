

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackResourceDriftsRequestAction(str, enum.Enum):
    DESCRIBE_STACK_RESOURCE_DRIFTS = "DescribeStackResourceDrifts"

    def visit(self, describe_stack_resource_drifts: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackResourceDriftsRequestAction.DESCRIBE_STACK_RESOURCE_DRIFTS:
            return describe_stack_resource_drifts()
