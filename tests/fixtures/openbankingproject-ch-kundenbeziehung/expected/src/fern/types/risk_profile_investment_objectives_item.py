

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileInvestmentObjectivesItem(enum.StrEnum):
    CAPITAL_PRESERVATION = "capital_preservation"
    INCOME = "income"
    GROWTH = "growth"
    SPECULATION = "speculation"

    def visit(
        self,
        capital_preservation: typing.Callable[[], T_Result],
        income: typing.Callable[[], T_Result],
        growth: typing.Callable[[], T_Result],
        speculation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileInvestmentObjectivesItem.CAPITAL_PRESERVATION:
            return capital_preservation()
        if self is RiskProfileInvestmentObjectivesItem.INCOME:
            return income()
        if self is RiskProfileInvestmentObjectivesItem.GROWTH:
            return growth()
        if self is RiskProfileInvestmentObjectivesItem.SPECULATION:
            return speculation()
