

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PushedAuthorizationRequestRequestPurpose(enum.StrEnum):
    ACCOUNT_OPENING = "accountOpening"
    CREDIT_ASSESSMENT = "creditAssessment"
    COMPLIANCE = "compliance"
    CUSTOMER_UPDATE = "customerUpdate"

    def visit(
        self,
        account_opening: typing.Callable[[], T_Result],
        credit_assessment: typing.Callable[[], T_Result],
        compliance: typing.Callable[[], T_Result],
        customer_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PushedAuthorizationRequestRequestPurpose.ACCOUNT_OPENING:
            return account_opening()
        if self is PushedAuthorizationRequestRequestPurpose.CREDIT_ASSESSMENT:
            return credit_assessment()
        if self is PushedAuthorizationRequestRequestPurpose.COMPLIANCE:
            return compliance()
        if self is PushedAuthorizationRequestRequestPurpose.CUSTOMER_UPDATE:
            return customer_update()
