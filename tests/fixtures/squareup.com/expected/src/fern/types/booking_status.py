

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BookingStatus(enum.StrEnum):
    """
    Supported booking statuses.
    """

    PENDING = "PENDING"
    CANCELLED_BY_CUSTOMER = "CANCELLED_BY_CUSTOMER"
    CANCELLED_BY_SELLER = "CANCELLED_BY_SELLER"
    DECLINED = "DECLINED"
    ACCEPTED = "ACCEPTED"
    NO_SHOW = "NO_SHOW"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        cancelled_by_customer: typing.Callable[[], T_Result],
        cancelled_by_seller: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
        no_show: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BookingStatus.PENDING:
            return pending()
        if self is BookingStatus.CANCELLED_BY_CUSTOMER:
            return cancelled_by_customer()
        if self is BookingStatus.CANCELLED_BY_SELLER:
            return cancelled_by_seller()
        if self is BookingStatus.DECLINED:
            return declined()
        if self is BookingStatus.ACCEPTED:
            return accepted()
        if self is BookingStatus.NO_SHOW:
            return no_show()
