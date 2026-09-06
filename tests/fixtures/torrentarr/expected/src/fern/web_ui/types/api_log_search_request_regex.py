

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiLogSearchRequestRegex(enum.StrEnum):
    ZERO = "0"
    ONE = "1"

    def visit(self, zero: typing.Callable[[], T_Result], one: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiLogSearchRequestRegex.ZERO:
            return zero()
        if self is ApiLogSearchRequestRegex.ONE:
            return one()
