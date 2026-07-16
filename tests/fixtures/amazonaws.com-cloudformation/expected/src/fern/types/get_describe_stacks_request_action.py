

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeStacksRequestAction(str, enum.Enum):
    DESCRIBE_STACKS = "DescribeStacks"

    def visit(self, describe_stacks: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStacksRequestAction.DESCRIBE_STACKS:
            return describe_stacks()
