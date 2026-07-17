

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeTypeRequestAction(enum.StrEnum):
    DESCRIBE_TYPE = "DescribeType"

    def visit(self, describe_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeTypeRequestAction.DESCRIBE_TYPE:
            return describe_type()
