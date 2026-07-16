

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .business_appointment_settings import BusinessAppointmentSettings


class BusinessBookingProfile(UniversalBaseModel):
    """ """

    allow_user_cancel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether customers can cancel or reschedule their own bookings (`true`) or not (`false`).
    """

    booking_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the seller is open for booking.
    """

    booking_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    The policy for the seller to automatically accept booking requests (`ACCEPT_ALL`) or not (`REQUIRES_ACCEPTANCE`).
    """

    business_appointment_settings: typing.Optional[BusinessAppointmentSettings] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The RFC 3339 timestamp specifying the booking's creation time.
    """

    customer_timezone_choice: typing.Optional[str] = pydantic.Field(default=None)
    """
    The choice of customer's time zone information of a booking.
    The Square online booking site and all notifications to customers uses either the seller location’s time zone
    or the time zone the customer chooses at booking.
    """

    seller_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller, obtainable using the Merchants API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
