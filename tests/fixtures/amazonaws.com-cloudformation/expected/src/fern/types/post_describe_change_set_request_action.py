

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeChangeSetRequestAction(str, enum.Enum):
    DESCRIBE_CHANGE_SET = "DescribeChangeSet"

    def visit(self, describe_change_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeChangeSetRequestAction.DESCRIBE_CHANGE_SET:
            return describe_change_set()
