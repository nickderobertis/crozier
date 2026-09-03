

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MiFidAssessmentRequestInvestmentExperience(enum.StrEnum):
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
        if self is MiFidAssessmentRequestInvestmentExperience.NONE:
            return none()
        if self is MiFidAssessmentRequestInvestmentExperience.LIMITED:
            return limited()
        if self is MiFidAssessmentRequestInvestmentExperience.GOOD:
            return good()
        if self is MiFidAssessmentRequestInvestmentExperience.EXTENSIVE:
            return extensive()
