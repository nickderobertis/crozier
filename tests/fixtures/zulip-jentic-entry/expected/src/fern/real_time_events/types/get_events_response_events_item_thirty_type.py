

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThirtyType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    DELETE_MESSAGE = "delete_message"

    def visit(self, delete_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThirtyType.DELETE_MESSAGE:
            return delete_message()
