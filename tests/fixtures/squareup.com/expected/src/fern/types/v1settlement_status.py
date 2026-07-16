

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1SettlementStatus(enum.StrEnum):
    """ """

    FAILED = "FAILED"
    SENT = "SENT"

    def visit(self, failed: typing.Callable[[], T_Result], sent: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1SettlementStatus.FAILED:
            return failed()
        if self is V1SettlementStatus.SENT:
            return sent()
