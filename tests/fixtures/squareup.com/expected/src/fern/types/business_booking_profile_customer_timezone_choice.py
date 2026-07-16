

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BusinessBookingProfileCustomerTimezoneChoice(enum.StrEnum):
    """
    Choices of customer-facing time zone used for bookings.
    """

    BUSINESS_LOCATION_TIMEZONE = "BUSINESS_LOCATION_TIMEZONE"
    CUSTOMER_CHOICE = "CUSTOMER_CHOICE"

    def visit(
        self, business_location_timezone: typing.Callable[[], T_Result], customer_choice: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BusinessBookingProfileCustomerTimezoneChoice.BUSINESS_LOCATION_TIMEZONE:
            return business_location_timezone()
        if self is BusinessBookingProfileCustomerTimezoneChoice.CUSTOMER_CHOICE:
            return customer_choice()
