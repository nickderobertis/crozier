

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CallNotificationParametersCallStatus(enum.StrEnum):
    """
    Call's current status
    """

    RINGING = "ringing"
    EARLY_MEDIA = "early-media"
    ANSWER = "answer"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

    def visit(
        self,
        ringing: typing.Callable[[], T_Result],
        early_media: typing.Callable[[], T_Result],
        answer: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CallNotificationParametersCallStatus.RINGING:
            return ringing()
        if self is CallNotificationParametersCallStatus.EARLY_MEDIA:
            return early_media()
        if self is CallNotificationParametersCallStatus.ANSWER:
            return answer()
        if self is CallNotificationParametersCallStatus.IN_PROGRESS:
            return in_progress()
        if self is CallNotificationParametersCallStatus.COMPLETED:
            return completed()
