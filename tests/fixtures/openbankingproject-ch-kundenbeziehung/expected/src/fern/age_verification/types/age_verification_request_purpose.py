

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgeVerificationRequestPurpose(enum.StrEnum):
    CROSS_INDUSTRY_AGE_GATE = "cross_industry_age_gate"
    REGULATORY_COMPLIANCE = "regulatory_compliance"

    def visit(
        self,
        cross_industry_age_gate: typing.Callable[[], T_Result],
        regulatory_compliance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgeVerificationRequestPurpose.CROSS_INDUSTRY_AGE_GATE:
            return cross_industry_age_gate()
        if self is AgeVerificationRequestPurpose.REGULATORY_COMPLIANCE:
            return regulatory_compliance()
