

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FullDataRequestPurpose(enum.StrEnum):
    ACCOUNT_OPENING = "accountOpening"
    CREDIT_ASSESSMENT = "creditAssessment"
    COMPLIANCE = "compliance"

    def visit(
        self,
        account_opening: typing.Callable[[], T_Result],
        credit_assessment: typing.Callable[[], T_Result],
        compliance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FullDataRequestPurpose.ACCOUNT_OPENING:
            return account_opening()
        if self is FullDataRequestPurpose.CREDIT_ASSESSMENT:
            return credit_assessment()
        if self is FullDataRequestPurpose.COMPLIANCE:
            return compliance()
