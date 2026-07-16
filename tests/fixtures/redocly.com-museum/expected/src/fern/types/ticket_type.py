

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketType(str, enum.Enum):
    """
    Type of ticket being purchased. Use `general` for regular museum entry and `event` for tickets to special events.
    """

    EVENT = "event"
    GENERAL = "general"

    def visit(self, event: typing.Callable[[], T_Result], general: typing.Callable[[], T_Result]) -> T_Result:
        if self is TicketType.EVENT:
            return event()
        if self is TicketType.GENERAL:
            return general()
