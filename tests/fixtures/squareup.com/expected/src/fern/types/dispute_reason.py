

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DisputeReason(str, enum.Enum):
    """
    The list of possible reasons why a cardholder might initiate a
    dispute with their bank.
    """

    AMOUNT_DIFFERS = "AMOUNT_DIFFERS"
    CANCELLED = "CANCELLED"
    DUPLICATE = "DUPLICATE"
    NO_KNOWLEDGE = "NO_KNOWLEDGE"
    NOT_AS_DESCRIBED = "NOT_AS_DESCRIBED"
    NOT_RECEIVED = "NOT_RECEIVED"
    PAID_BY_OTHER_MEANS = "PAID_BY_OTHER_MEANS"
    CUSTOMER_REQUESTS_CREDIT = "CUSTOMER_REQUESTS_CREDIT"
    EMV_LIABILITY_SHIFT = "EMV_LIABILITY_SHIFT"

    def visit(
        self,
        amount_differs: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        duplicate: typing.Callable[[], T_Result],
        no_knowledge: typing.Callable[[], T_Result],
        not_as_described: typing.Callable[[], T_Result],
        not_received: typing.Callable[[], T_Result],
        paid_by_other_means: typing.Callable[[], T_Result],
        customer_requests_credit: typing.Callable[[], T_Result],
        emv_liability_shift: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisputeReason.AMOUNT_DIFFERS:
            return amount_differs()
        if self is DisputeReason.CANCELLED:
            return cancelled()
        if self is DisputeReason.DUPLICATE:
            return duplicate()
        if self is DisputeReason.NO_KNOWLEDGE:
            return no_knowledge()
        if self is DisputeReason.NOT_AS_DESCRIBED:
            return not_as_described()
        if self is DisputeReason.NOT_RECEIVED:
            return not_received()
        if self is DisputeReason.PAID_BY_OTHER_MEANS:
            return paid_by_other_means()
        if self is DisputeReason.CUSTOMER_REQUESTS_CREDIT:
            return customer_requests_credit()
        if self is DisputeReason.EMV_LIABILITY_SHIFT:
            return emv_liability_shift()
