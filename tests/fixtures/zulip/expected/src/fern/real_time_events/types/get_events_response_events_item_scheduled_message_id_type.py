

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemScheduledMessageIdType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    SCHEDULED_MESSAGES = "scheduled_messages"

    def visit(self, scheduled_messages: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemScheduledMessageIdType.SCHEDULED_MESSAGES:
            return scheduled_messages()
