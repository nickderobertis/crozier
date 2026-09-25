

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThreeType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    SUBSCRIPTION = "subscription"

    def visit(self, subscription: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThreeType.SUBSCRIPTION:
            return subscription()
