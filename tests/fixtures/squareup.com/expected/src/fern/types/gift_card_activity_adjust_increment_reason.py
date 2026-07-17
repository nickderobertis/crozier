

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardActivityAdjustIncrementReason(enum.StrEnum):
    """ """

    COMPLIMENTARY = "COMPLIMENTARY"
    SUPPORT_ISSUE = "SUPPORT_ISSUE"
    TRANSACTION_VOIDED = "TRANSACTION_VOIDED"

    def visit(
        self,
        complimentary: typing.Callable[[], T_Result],
        support_issue: typing.Callable[[], T_Result],
        transaction_voided: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardActivityAdjustIncrementReason.COMPLIMENTARY:
            return complimentary()
        if self is GiftCardActivityAdjustIncrementReason.SUPPORT_ISSUE:
            return support_issue()
        if self is GiftCardActivityAdjustIncrementReason.TRANSACTION_VOIDED:
            return transaction_voided()
