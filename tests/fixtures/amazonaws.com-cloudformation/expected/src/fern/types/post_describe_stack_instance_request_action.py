

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackInstanceRequestAction(str, enum.Enum):
    DESCRIBE_STACK_INSTANCE = "DescribeStackInstance"

    def visit(self, describe_stack_instance: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackInstanceRequestAction.DESCRIBE_STACK_INSTANCE:
            return describe_stack_instance()
