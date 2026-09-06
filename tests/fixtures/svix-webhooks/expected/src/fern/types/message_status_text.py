

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageStatusText(enum.StrEnum):
    SUCCESS = "success"
    PENDING = "pending"
    FAIL = "fail"
    SENDING = "sending"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        sending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageStatusText.SUCCESS:
            return success()
        if self is MessageStatusText.PENDING:
            return pending()
        if self is MessageStatusText.FAIL:
            return fail()
        if self is MessageStatusText.SENDING:
            return sending()
