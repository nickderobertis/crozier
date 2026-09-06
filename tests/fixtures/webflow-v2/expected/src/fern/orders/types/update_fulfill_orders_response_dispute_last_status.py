

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFulfillOrdersResponseDisputeLastStatus(enum.StrEnum):
    """
    If an order was disputed by the customer, then this key will be set with the [dispute's status](https://stripe.com/docs/api#dispute_object-status).
    """

    WARNING_NEEDS_RESPONSE = "warning_needs_response"
    WARNING_UNDER_REVIEW = "warning_under_review"
    WARNING_CLOSED = "warning_closed"
    NEEDS_RESPONSE = "needs_response"
    UNDER_REVIEW = "under_review"
    CHARGE_REFUNDED = "charge_refunded"
    WON = "won"
    LOST = "lost"

    def visit(
        self,
        warning_needs_response: typing.Callable[[], T_Result],
        warning_under_review: typing.Callable[[], T_Result],
        warning_closed: typing.Callable[[], T_Result],
        needs_response: typing.Callable[[], T_Result],
        under_review: typing.Callable[[], T_Result],
        charge_refunded: typing.Callable[[], T_Result],
        won: typing.Callable[[], T_Result],
        lost: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.WARNING_NEEDS_RESPONSE:
            return warning_needs_response()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.WARNING_UNDER_REVIEW:
            return warning_under_review()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.WARNING_CLOSED:
            return warning_closed()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.NEEDS_RESPONSE:
            return needs_response()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.UNDER_REVIEW:
            return under_review()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.CHARGE_REFUNDED:
            return charge_refunded()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.WON:
            return won()
        if self is UpdateFulfillOrdersResponseDisputeLastStatus.LOST:
            return lost()
