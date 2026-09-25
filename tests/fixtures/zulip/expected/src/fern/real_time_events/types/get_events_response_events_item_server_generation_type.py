

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemServerGenerationType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    RESTART = "restart"

    def visit(self, restart: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemServerGenerationType.RESTART:
            return restart()
