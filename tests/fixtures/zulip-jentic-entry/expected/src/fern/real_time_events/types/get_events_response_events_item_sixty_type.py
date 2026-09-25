

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSixtyType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_BOT = "realm_bot"

    def visit(self, realm_bot: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSixtyType.REALM_BOT:
            return realm_bot()
