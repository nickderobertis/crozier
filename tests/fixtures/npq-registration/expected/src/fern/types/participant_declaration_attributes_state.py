

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationAttributesState(enum.StrEnum):
    """
    Indicates the state of this payment declaration
    """

    SUBMITTED = "submitted"
    ELIGIBLE = "eligible"
    PAYABLE = "payable"
    PAID = "paid"
    VOIDED = "voided"
    INELIGIBLE = "ineligible"
    AWAITING_CLAWBACK = "awaiting_clawback"
    CLAWED_BACK = "clawed_back"

    def visit(
        self,
        submitted: typing.Callable[[], T_Result],
        eligible: typing.Callable[[], T_Result],
        payable: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        ineligible: typing.Callable[[], T_Result],
        awaiting_clawback: typing.Callable[[], T_Result],
        clawed_back: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantDeclarationAttributesState.SUBMITTED:
            return submitted()
        if self is ParticipantDeclarationAttributesState.ELIGIBLE:
            return eligible()
        if self is ParticipantDeclarationAttributesState.PAYABLE:
            return payable()
        if self is ParticipantDeclarationAttributesState.PAID:
            return paid()
        if self is ParticipantDeclarationAttributesState.VOIDED:
            return voided()
        if self is ParticipantDeclarationAttributesState.INELIGIBLE:
            return ineligible()
        if self is ParticipantDeclarationAttributesState.AWAITING_CLAWBACK:
            return awaiting_clawback()
        if self is ParticipantDeclarationAttributesState.CLAWED_BACK:
            return clawed_back()
