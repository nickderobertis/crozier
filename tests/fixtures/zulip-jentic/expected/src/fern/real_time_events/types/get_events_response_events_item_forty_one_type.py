

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyOneType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    UPDATE_MESSAGE_FLAGS = "update_message_flags"

    def visit(self, update_message_flags: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyOneType.UPDATE_MESSAGE_FLAGS:
            return update_message_flags()
