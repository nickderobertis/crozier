

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemTenType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    INVITES_CHANGED = "invites_changed"

    def visit(self, invites_changed: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemTenType.INVITES_CHANGED:
            return invites_changed()
