

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileRiskTolerance(enum.StrEnum):
    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"

    def visit(
        self,
        conservative: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        aggressive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileRiskTolerance.CONSERVATIVE:
            return conservative()
        if self is RiskProfileRiskTolerance.MODERATE:
            return moderate()
        if self is RiskProfileRiskTolerance.AGGRESSIVE:
            return aggressive()
