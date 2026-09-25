

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemNineType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    HAS_ZOOM_TOKEN = "has_zoom_token"

    def visit(self, has_zoom_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemNineType.HAS_ZOOM_TOKEN:
            return has_zoom_token()
