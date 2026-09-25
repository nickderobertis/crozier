

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSeventySevenType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    NAVIGATION_VIEW = "navigation_view"

    def visit(self, navigation_view: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSeventySevenType.NAVIGATION_VIEW:
            return navigation_view()
