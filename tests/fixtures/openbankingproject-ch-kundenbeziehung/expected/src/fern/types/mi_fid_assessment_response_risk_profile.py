

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MiFidAssessmentResponseRiskProfile(enum.StrEnum):
    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"

    def visit(
        self,
        conservative: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        aggressive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MiFidAssessmentResponseRiskProfile.CONSERVATIVE:
            return conservative()
        if self is MiFidAssessmentResponseRiskProfile.MODERATE:
            return moderate()
        if self is MiFidAssessmentResponseRiskProfile.AGGRESSIVE:
            return aggressive()
