

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicAutomationConfigEventType(enum.StrEnum):
    """
    The type of automation.
    """

    TOPIC = "topic"

    def visit(self, topic: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopicAutomationConfigEventType.TOPIC:
            return topic()
