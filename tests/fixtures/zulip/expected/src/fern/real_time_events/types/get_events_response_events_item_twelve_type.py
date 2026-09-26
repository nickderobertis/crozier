

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemTwelveType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_USER = "realm_user"

    def visit(self, realm_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemTwelveType.REALM_USER:
            return realm_user()
