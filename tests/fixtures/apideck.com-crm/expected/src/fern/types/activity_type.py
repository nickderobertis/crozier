

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActivityType(enum.StrEnum):
    CALL = "call"
    MEETING = "meeting"
    EMAIL = "email"
    NOTE = "note"
    TASK = "task"
    DEADLINE = "deadline"
    SEND_LETTER = "send-letter"
    SEND_QUOTE = "send-quote"
    OTHER = "other"

    def visit(
        self,
        call: typing.Callable[[], T_Result],
        meeting: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        note: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        deadline: typing.Callable[[], T_Result],
        send_letter: typing.Callable[[], T_Result],
        send_quote: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActivityType.CALL:
            return call()
        if self is ActivityType.MEETING:
            return meeting()
        if self is ActivityType.EMAIL:
            return email()
        if self is ActivityType.NOTE:
            return note()
        if self is ActivityType.TASK:
            return task()
        if self is ActivityType.DEADLINE:
            return deadline()
        if self is ActivityType.SEND_LETTER:
            return send_letter()
        if self is ActivityType.SEND_QUOTE:
            return send_quote()
        if self is ActivityType.OTHER:
            return other()
