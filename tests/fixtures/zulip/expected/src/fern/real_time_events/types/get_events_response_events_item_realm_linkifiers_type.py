

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemRealmLinkifiersType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_LINKIFIERS = "realm_linkifiers"

    def visit(self, realm_linkifiers: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemRealmLinkifiersType.REALM_LINKIFIERS:
            return realm_linkifiers()
