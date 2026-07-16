

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1CreateRefundRequestType(str, enum.Enum):
    """ """

    FULL = "FULL"
    PARTIAL = "PARTIAL"

    def visit(self, full: typing.Callable[[], T_Result], partial: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1CreateRefundRequestType.FULL:
            return full()
        if self is V1CreateRefundRequestType.PARTIAL:
            return partial()
