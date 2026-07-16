

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeTypeRequestAction(str, enum.Enum):
    DESCRIBE_TYPE = "DescribeType"

    def visit(self, describe_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeTypeRequestAction.DESCRIBE_TYPE:
            return describe_type()
