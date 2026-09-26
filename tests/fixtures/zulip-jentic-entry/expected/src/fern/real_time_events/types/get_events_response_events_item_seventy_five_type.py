

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSeventyFiveType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    SAVED_SNIPPETS = "saved_snippets"

    def visit(self, saved_snippets: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSeventyFiveType.SAVED_SNIPPETS:
            return saved_snippets()
