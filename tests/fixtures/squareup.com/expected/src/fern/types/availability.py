

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .appointment_segment import AppointmentSegment


class Availability(UniversalBaseModel):
    """
    Describes a slot available for booking, encapsulating appointment segments, the location and starting time.
    """

    appointment_segments: typing.Optional[typing.List[AppointmentSegment]] = pydantic.Field(default=None)
    """
    The list of appointment segments available for booking
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the location available for booking.
    """

    start_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The RFC 3339 timestamp specifying the beginning time of the slot available for booking.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
