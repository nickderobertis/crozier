

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemDefaultStreamsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    DEFAULT_STREAMS = "default_streams"

    def visit(self, default_streams: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemDefaultStreamsType.DEFAULT_STREAMS:
            return default_streams()
