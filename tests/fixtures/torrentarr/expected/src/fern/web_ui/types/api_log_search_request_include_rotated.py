

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiLogSearchRequestIncludeRotated(enum.StrEnum):
    ZERO = "0"
    ONE = "1"

    def visit(self, zero: typing.Callable[[], T_Result], one: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiLogSearchRequestIncludeRotated.ZERO:
            return zero()
        if self is ApiLogSearchRequestIncludeRotated.ONE:
            return one()
