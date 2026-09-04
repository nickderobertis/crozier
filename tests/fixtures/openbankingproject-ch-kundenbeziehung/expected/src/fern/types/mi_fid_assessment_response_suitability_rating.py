

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MiFidAssessmentResponseSuitabilityRating(enum.StrEnum):
    SUITABLE = "suitable"
    SUITABLE_WITH_RESTRICTIONS = "suitable_with_restrictions"
    NOT_SUITABLE = "not_suitable"

    def visit(
        self,
        suitable: typing.Callable[[], T_Result],
        suitable_with_restrictions: typing.Callable[[], T_Result],
        not_suitable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MiFidAssessmentResponseSuitabilityRating.SUITABLE:
            return suitable()
        if self is MiFidAssessmentResponseSuitabilityRating.SUITABLE_WITH_RESTRICTIONS:
            return suitable_with_restrictions()
        if self is MiFidAssessmentResponseSuitabilityRating.NOT_SUITABLE:
            return not_suitable()
