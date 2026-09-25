

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuoteDepositOptionTypeZero(enum.StrEnum):
    PERCENT = "PERCENT"

    def visit(self, percent: typing.Callable[[], T_Result]) -> T_Result:
        if self is QuoteDepositOptionTypeZero.PERCENT:
            return percent()
