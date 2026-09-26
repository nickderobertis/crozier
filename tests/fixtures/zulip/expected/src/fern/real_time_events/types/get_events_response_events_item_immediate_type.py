

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemImmediateType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    WEB_RELOAD_CLIENT = "web_reload_client"

    def visit(self, web_reload_client: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemImmediateType.WEB_RELOAD_CLIENT:
            return web_reload_client()
