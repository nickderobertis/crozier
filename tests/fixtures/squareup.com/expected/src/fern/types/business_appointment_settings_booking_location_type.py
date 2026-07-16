

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BusinessAppointmentSettingsBookingLocationType(str, enum.Enum):
    """
    Types of location where service is provided.
    """

    BUSINESS_LOCATION = "BUSINESS_LOCATION"
    CUSTOMER_LOCATION = "CUSTOMER_LOCATION"
    PHONE = "PHONE"

    def visit(
        self,
        business_location: typing.Callable[[], T_Result],
        customer_location: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BusinessAppointmentSettingsBookingLocationType.BUSINESS_LOCATION:
            return business_location()
        if self is BusinessAppointmentSettingsBookingLocationType.CUSTOMER_LOCATION:
            return customer_location()
        if self is BusinessAppointmentSettingsBookingLocationType.PHONE:
            return phone()
