

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDescribeStackEventsRequestAction(enum.StrEnum):
    DESCRIBE_STACK_EVENTS = "DescribeStackEvents"

    def visit(self, describe_stack_events: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDescribeStackEventsRequestAction.DESCRIBE_STACK_EVENTS:
            return describe_stack_events()
