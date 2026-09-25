

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemTwentyOneType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    ATTACHMENT = "attachment"

    def visit(self, attachment: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemTwentyOneType.ATTACHMENT:
            return attachment()
