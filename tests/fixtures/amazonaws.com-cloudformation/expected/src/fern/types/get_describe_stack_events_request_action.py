

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackEventsRequestAction(str, enum.Enum):
    DESCRIBE_STACK_EVENTS = "DescribeStackEvents"

    def visit(self, describe_stack_events: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackEventsRequestAction.DESCRIBE_STACK_EVENTS:
            return describe_stack_events()
