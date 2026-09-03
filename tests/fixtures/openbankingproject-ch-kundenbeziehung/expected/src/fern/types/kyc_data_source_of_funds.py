

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KycDataSourceOfFunds(enum.StrEnum):
    SALARY = "salary"
    BUSINESS_INCOME = "business_income"
    INHERITANCE = "inheritance"
    INVESTMENT_RETURNS = "investment_returns"
    OTHER = "other"

    def visit(
        self,
        salary: typing.Callable[[], T_Result],
        business_income: typing.Callable[[], T_Result],
        inheritance: typing.Callable[[], T_Result],
        investment_returns: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KycDataSourceOfFunds.SALARY:
            return salary()
        if self is KycDataSourceOfFunds.BUSINESS_INCOME:
            return business_income()
        if self is KycDataSourceOfFunds.INHERITANCE:
            return inheritance()
        if self is KycDataSourceOfFunds.INVESTMENT_RETURNS:
            return investment_returns()
        if self is KycDataSourceOfFunds.OTHER:
            return other()
