

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class BusinessAppointmentSettings(UniversalBaseModel):
    """
    The service appointment settings, including where and how the service is provided.
    """

    alignment_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time unit of the service duration for bookings.
    """

    any_team_member_booking_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether a customer can choose from all available time slots and have a staff member assigned
    automatically (`true`) or not (`false`).
    """

    cancellation_fee_money: typing.Optional[Money] = None
    cancellation_policy: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cancellation policy adopted by the seller.
    """

    cancellation_policy_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The free-form text of the seller's cancellation policy.
    """

    cancellation_window_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    The cut-off time in seconds for allowing clients to cancel or reschedule an appointment.
    """

    location_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Types of the location allowed for bookings.
    """

    max_appointments_per_day_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of daily appointments per team member or per location.
    """

    max_appointments_per_day_limit_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates whether the daily appointment limit applies to team members or to
    business locations.
    """

    max_booking_lead_time_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum lead time in seconds before a service can be booked. Bookings must be created at most this far ahead of the booking's starting time.
    """

    min_booking_lead_time_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum lead time in seconds before a service can be booked. Bookings must be created at least this far ahead of the booking's starting time.
    """

    multiple_service_booking_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether a customer can book multiple services in a single online booking.
    """

    skip_booking_flow_staff_selection: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether customers has an assigned staff member (`true`) or can select s staff member of their choice (`false`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
