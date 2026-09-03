

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileInvestmentKnowledge(enum.StrEnum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    PROFESSIONAL = "professional"

    def visit(
        self,
        basic: typing.Callable[[], T_Result],
        intermediate: typing.Callable[[], T_Result],
        advanced: typing.Callable[[], T_Result],
        professional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileInvestmentKnowledge.BASIC:
            return basic()
        if self is RiskProfileInvestmentKnowledge.INTERMEDIATE:
            return intermediate()
        if self is RiskProfileInvestmentKnowledge.ADVANCED:
            return advanced()
        if self is RiskProfileInvestmentKnowledge.PROFESSIONAL:
            return professional()
