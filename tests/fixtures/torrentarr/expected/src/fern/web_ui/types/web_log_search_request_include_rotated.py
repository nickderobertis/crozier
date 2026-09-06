

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WebLogSearchRequestIncludeRotated(enum.StrEnum):
    ZERO = "0"
    ONE = "1"

    def visit(self, zero: typing.Callable[[], T_Result], one: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebLogSearchRequestIncludeRotated.ZERO:
            return zero()
        if self is WebLogSearchRequestIncludeRotated.ONE:
            return one()
