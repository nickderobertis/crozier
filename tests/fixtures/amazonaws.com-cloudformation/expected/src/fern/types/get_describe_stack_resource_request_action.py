

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackResourceRequestAction(str, enum.Enum):
    DESCRIBE_STACK_RESOURCE = "DescribeStackResource"

    def visit(self, describe_stack_resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackResourceRequestAction.DESCRIBE_STACK_RESOURCE:
            return describe_stack_resource()
