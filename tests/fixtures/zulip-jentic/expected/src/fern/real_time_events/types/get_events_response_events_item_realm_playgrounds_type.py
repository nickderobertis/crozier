

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemRealmPlaygroundsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_PLAYGROUNDS = "realm_playgrounds"

    def visit(self, realm_playgrounds: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemRealmPlaygroundsType.REALM_PLAYGROUNDS:
            return realm_playgrounds()
