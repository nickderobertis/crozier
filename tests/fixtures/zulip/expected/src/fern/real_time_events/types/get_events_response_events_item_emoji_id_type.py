

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemEmojiIdType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    REALM_EMOJI = "realm_emoji"

    def visit(self, realm_emoji: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemEmojiIdType.REALM_EMOJI:
            return realm_emoji()
