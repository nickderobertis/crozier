

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class V1RefundType(str, enum.Enum):
    """ """

    FULL = "FULL"
    PARTIAL = "PARTIAL"

    def visit(self, full: typing.Callable[[], T_Result], partial: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1RefundType.FULL:
            return full()
        if self is V1RefundType.PARTIAL:
            return partial()
