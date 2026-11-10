

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartnerEndCustomerFlowdownStatus(enum.StrEnum):
    """
    The status of the addendum to the Plaid MSA ("flowdown") for the end customer.
    """

    NOT_STARTED = "NOT_STARTED"
    IN_REVIEW = "IN_REVIEW"
    NEGOTIATION = "NEGOTIATION"
    COMPLETE = "COMPLETE"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_review: typing.Callable[[], T_Result],
        negotiation: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PartnerEndCustomerFlowdownStatus.NOT_STARTED:
            return not_started()
        if self is PartnerEndCustomerFlowdownStatus.IN_REVIEW:
            return in_review()
        if self is PartnerEndCustomerFlowdownStatus.NEGOTIATION:
            return negotiation()
        if self is PartnerEndCustomerFlowdownStatus.COMPLETE:
            return complete()
