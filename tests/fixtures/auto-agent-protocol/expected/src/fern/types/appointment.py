

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .appointment_appointment_type import AppointmentAppointmentType


class Appointment(UniversalBaseModel):
    """
    An appointment request piggybacked on a `lead.submit.request`. The vehicle reference for the appointment is IMPLICIT — it is whatever is in the parent `vehicle_of_interest` (or `trade_in` for a trade-in appraisal). A standalone sales or service visit can omit any vehicle.
    """

    appointment_type: AppointmentAppointmentType = pydantic.Field()
    """
    Kind of appointment the buyer is requesting.
    """

    appointment_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Requested start time of the appointment as an ISO 8601 / RFC 3339 timestamp that MUST include a timezone offset (Z or ±HH:MM), e.g. '2026-05-03T11:00:00-07:00'. Optional — when omitted, the dealer follows up to schedule a time.
    """

    duration_minutes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Expected appointment duration in minutes. If omitted, the dealer applies its default for `appointment_type`.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text note from the buyer (e.g. 'I'd like to bring my partner', 'parking instructions please').
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
