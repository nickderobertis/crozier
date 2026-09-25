

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemAlertWordsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    ALERT_WORDS = "alert_words"

    def visit(self, alert_words: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemAlertWordsType.ALERT_WORDS:
            return alert_words()
