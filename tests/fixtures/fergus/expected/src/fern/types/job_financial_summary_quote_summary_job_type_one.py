

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobFinancialSummaryQuoteSummaryJobTypeOne(enum.StrEnum):
    ESTIMATE = "Estimate"

    def visit(self, estimate: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobFinancialSummaryQuoteSummaryJobTypeOne.ESTIMATE:
            return estimate()
