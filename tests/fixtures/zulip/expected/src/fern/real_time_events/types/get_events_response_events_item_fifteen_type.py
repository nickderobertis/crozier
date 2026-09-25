

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFifteenType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    STREAM = "stream"

    def visit(self, stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFifteenType.STREAM:
            return stream()
