

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeStacksRequestAction(enum.StrEnum):
    DESCRIBE_STACKS = "DescribeStacks"

    def visit(self, describe_stacks: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStacksRequestAction.DESCRIBE_STACKS:
            return describe_stacks()
