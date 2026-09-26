

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMutedTopicsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    MUTED_TOPICS = "muted_topics"

    def visit(self, muted_topics: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMutedTopicsType.MUTED_TOPICS:
            return muted_topics()
