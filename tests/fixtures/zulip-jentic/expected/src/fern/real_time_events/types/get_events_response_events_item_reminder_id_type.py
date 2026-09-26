

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemReminderIdType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REMINDERS = "reminders"

    def visit(self, reminders: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemReminderIdType.REMINDERS:
            return reminders()
