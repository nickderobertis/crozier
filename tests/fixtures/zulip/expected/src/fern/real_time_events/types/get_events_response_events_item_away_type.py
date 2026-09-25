

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemAwayType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    USER_STATUS = "user_status"

    def visit(self, user_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemAwayType.USER_STATUS:
            return user_status()
