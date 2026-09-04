

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileInvestmentHorizon(enum.StrEnum):
    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"

    def visit(
        self,
        short: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileInvestmentHorizon.SHORT:
            return short()
        if self is RiskProfileInvestmentHorizon.MEDIUM:
            return medium()
        if self is RiskProfileInvestmentHorizon.LONG:
            return long_()
