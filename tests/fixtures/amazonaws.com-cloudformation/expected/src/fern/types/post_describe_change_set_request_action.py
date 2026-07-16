

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeChangeSetRequestAction(enum.StrEnum):
    DESCRIBE_CHANGE_SET = "DescribeChangeSet"

    def visit(self, describe_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeChangeSetRequestAction.DESCRIBE_CHANGE_SET:
            return describe_change_set()
