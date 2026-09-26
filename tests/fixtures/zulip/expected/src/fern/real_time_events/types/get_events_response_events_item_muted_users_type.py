

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMutedUsersType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    MUTED_USERS = "muted_users"

    def visit(self, muted_users: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMutedUsersType.MUTED_USERS:
            return muted_users()
