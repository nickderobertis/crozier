

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackSetOperationRequestAction(str, enum.Enum):
    DESCRIBE_STACK_SET_OPERATION = "DescribeStackSetOperation"

    def visit(self, describe_stack_set_operation: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackSetOperationRequestAction.DESCRIBE_STACK_SET_OPERATION:
            return describe_stack_set_operation()
