

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFiftyFiveType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_DOMAINS = "realm_domains"

    def visit(self, realm_domains: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFiftyFiveType.REALM_DOMAINS:
            return realm_domains()
