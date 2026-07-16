

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1CreateRefundRequestType(enum.StrEnum):
    """ """

    FULL = "FULL"
    PARTIAL = "PARTIAL"

    def visit(self, full: typing.Callable[[], T_Result], partial: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1CreateRefundRequestType.FULL:
            return full()
        if self is V1CreateRefundRequestType.PARTIAL:
            return partial()
