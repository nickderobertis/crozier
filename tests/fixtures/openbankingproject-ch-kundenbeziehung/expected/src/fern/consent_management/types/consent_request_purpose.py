

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentRequestPurpose(enum.StrEnum):
    """
    Zweck der Datenverwendung
    """

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
        if self is ConsentRequestPurpose.ACCOUNT_OPENING:
            return account_opening()
        if self is ConsentRequestPurpose.CREDIT_ASSESSMENT:
            return credit_assessment()
        if self is ConsentRequestPurpose.COMPLIANCE:
            return compliance()
        if self is ConsentRequestPurpose.CUSTOMER_UPDATE:
            return customer_update()
