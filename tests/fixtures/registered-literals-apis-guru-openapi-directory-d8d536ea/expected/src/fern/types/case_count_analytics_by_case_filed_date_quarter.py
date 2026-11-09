

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseCountAnalyticsByCaseFiledDateQuarter(enum.StrEnum):
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"

    def visit(
        self,
        q1: typing.Callable[[], T_Result],
        q2: typing.Callable[[], T_Result],
        q3: typing.Callable[[], T_Result],
        q4: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseCountAnalyticsByCaseFiledDateQuarter.Q1:
            return q1()
        if self is CaseCountAnalyticsByCaseFiledDateQuarter.Q2:
            return q2()
        if self is CaseCountAnalyticsByCaseFiledDateQuarter.Q3:
            return q3()
        if self is CaseCountAnalyticsByCaseFiledDateQuarter.Q4:
            return q4()
