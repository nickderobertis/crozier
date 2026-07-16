

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SubscriptionEventInfoCode(str, enum.Enum):
    """
    The possible subscription event info codes.
    """

    LOCATION_NOT_ACTIVE = "LOCATION_NOT_ACTIVE"
    LOCATION_CANNOT_ACCEPT_PAYMENT = "LOCATION_CANNOT_ACCEPT_PAYMENT"
    CUSTOMER_DELETED = "CUSTOMER_DELETED"
    CUSTOMER_NO_EMAIL = "CUSTOMER_NO_EMAIL"
    CUSTOMER_NO_NAME = "CUSTOMER_NO_NAME"

    def visit(
        self,
        location_not_active: typing.Callable[[], T_Result],
        location_cannot_accept_payment: typing.Callable[[], T_Result],
        customer_deleted: typing.Callable[[], T_Result],
        customer_no_email: typing.Callable[[], T_Result],
        customer_no_name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionEventInfoCode.LOCATION_NOT_ACTIVE:
            return location_not_active()
        if self is SubscriptionEventInfoCode.LOCATION_CANNOT_ACCEPT_PAYMENT:
            return location_cannot_accept_payment()
        if self is SubscriptionEventInfoCode.CUSTOMER_DELETED:
            return customer_deleted()
        if self is SubscriptionEventInfoCode.CUSTOMER_NO_EMAIL:
            return customer_no_email()
        if self is SubscriptionEventInfoCode.CUSTOMER_NO_NAME:
            return customer_no_name()
