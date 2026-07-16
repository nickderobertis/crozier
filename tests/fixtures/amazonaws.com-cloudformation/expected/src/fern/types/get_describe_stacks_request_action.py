

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDescribeStacksRequestAction(enum.StrEnum):
    DESCRIBE_STACKS = "DescribeStacks"

    def visit(self, describe_stacks: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStacksRequestAction.DESCRIBE_STACKS:
            return describe_stacks()
