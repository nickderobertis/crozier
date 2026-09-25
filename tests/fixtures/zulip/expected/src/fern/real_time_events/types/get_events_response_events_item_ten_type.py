

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemTenType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    HAS_WEBEX_TOKEN = "has_webex_token"

    def visit(self, has_webex_token: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemTenType.HAS_WEBEX_TOKEN:
            return has_webex_token()
