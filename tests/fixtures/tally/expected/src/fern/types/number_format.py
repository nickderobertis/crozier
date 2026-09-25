

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NumberFormat(enum.StrEnum):
    NUMBER = "NUMBER"
    CURRENCY = "CURRENCY"
    PERCENTAGE = "PERCENTAGE"

    def visit(
        self,
        number: typing.Callable[[], T_Result],
        currency: typing.Callable[[], T_Result],
        percentage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NumberFormat.NUMBER:
            return number()
        if self is NumberFormat.CURRENCY:
            return currency()
        if self is NumberFormat.PERCENTAGE:
            return percentage()
