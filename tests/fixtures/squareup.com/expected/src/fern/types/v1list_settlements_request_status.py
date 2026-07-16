

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1ListSettlementsRequestStatus(str, enum.Enum):
    """ """

    SENT = "SENT"
    FAILED = "FAILED"

    def visit(self, sent: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ListSettlementsRequestStatus.SENT:
            return sent()
        if self is V1ListSettlementsRequestStatus.FAILED:
            return failed()
