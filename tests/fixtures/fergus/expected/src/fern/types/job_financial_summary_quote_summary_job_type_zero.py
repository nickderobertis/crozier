

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobFinancialSummaryQuoteSummaryJobTypeZero(enum.StrEnum):
    QUOTE = "Quote"

    def visit(self, quote: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobFinancialSummaryQuoteSummaryJobTypeZero.QUOTE:
            return quote()
