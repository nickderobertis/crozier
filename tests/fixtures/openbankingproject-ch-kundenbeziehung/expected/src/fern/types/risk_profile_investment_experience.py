

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileInvestmentExperience(enum.StrEnum):
    NONE = "none"
    LIMITED = "limited"
    GOOD = "good"
    EXTENSIVE = "extensive"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        limited: typing.Callable[[], T_Result],
        good: typing.Callable[[], T_Result],
        extensive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileInvestmentExperience.NONE:
            return none()
        if self is RiskProfileInvestmentExperience.LIMITED:
            return limited()
        if self is RiskProfileInvestmentExperience.GOOD:
            return good()
        if self is RiskProfileInvestmentExperience.EXTENSIVE:
            return extensive()
