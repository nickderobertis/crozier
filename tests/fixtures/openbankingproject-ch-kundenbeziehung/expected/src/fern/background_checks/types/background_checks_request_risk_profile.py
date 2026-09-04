

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BackgroundChecksRequestRiskProfile(enum.StrEnum):
    STANDARD = "standard"
    ENHANCED = "enhanced"
    HIGH_RISK = "high_risk"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        enhanced: typing.Callable[[], T_Result],
        high_risk: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BackgroundChecksRequestRiskProfile.STANDARD:
            return standard()
        if self is BackgroundChecksRequestRiskProfile.ENHANCED:
            return enhanced()
        if self is BackgroundChecksRequestRiskProfile.HIGH_RISK:
            return high_risk()
