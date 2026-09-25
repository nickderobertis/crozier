

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QuoteDepositOptionTypeOne(enum.StrEnum):
    FIXED = "FIXED"

    def visit(self, fixed: typing.Callable[[], T_Result]) -> T_Result:
        if self is QuoteDepositOptionTypeOne.FIXED:
            return fixed()
