

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy(enum.StrEnum):
    YEARLY = "Yearly"
    QUARTERLY = "Quarterly"
    MONTHLY = "Monthly"
    WEEKLY = "Weekly"

    def visit(
        self,
        yearly: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy.YEARLY:
            return yearly()
        if self is GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy.QUARTERLY:
            return quarterly()
        if self is GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy.MONTHLY:
            return monthly()
        if self is GetCaseCountAnalyticsByCaseFiledDateRequestGroupBy.WEEKLY:
            return weekly()
