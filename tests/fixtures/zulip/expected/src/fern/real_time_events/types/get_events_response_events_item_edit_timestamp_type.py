

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemEditTimestampType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    UPDATE_MESSAGE = "update_message"

    def visit(self, update_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemEditTimestampType.UPDATE_MESSAGE:
            return update_message()
