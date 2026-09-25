

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyEightType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    USER_GROUP = "user_group"

    def visit(self, user_group: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyEightType.USER_GROUP:
            return user_group()
