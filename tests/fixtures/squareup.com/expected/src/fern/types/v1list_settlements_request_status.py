

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListSettlementsRequestStatus(enum.StrEnum):
    """ """

    SENT = "SENT"
    FAILED = "FAILED"

    def visit(self, sent: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ListSettlementsRequestStatus.SENT:
            return sent()
        if self is V1ListSettlementsRequestStatus.FAILED:
            return failed()
