

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSixtySevenType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM = "realm"

    def visit(self, realm: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSixtySevenType.REALM:
            return realm()
