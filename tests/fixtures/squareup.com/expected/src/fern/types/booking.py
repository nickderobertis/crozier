

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .appointment_segment import AppointmentSegment


class Booking(UniversalBaseModel):
    """
    Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
    at a given location to a requesting customer in one or more appointment segments.
    """

    appointment_segments: typing.Optional[typing.List[AppointmentSegment]] = pydantic.Field(default=None)
    """
    A list of appointment segments for this booking.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp specifying the creation time of this booking, in RFC 3339 format.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [Customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) object representing the customer attending this booking
    """

    customer_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    The free-text field for the customer to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a relevant [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID of this object representing a booking.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) object representing the location where the booked service is provided.
    """

    seller_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    The free-text field for the seller to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a specific [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance.
    This field should not be visible to customers.
    """

    start_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp specifying the starting time of this booking, in RFC 3339 format.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the booking, describing where the booking stands with respect to the booking state machine.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp specifying the most recent update time of this booking, in RFC 3339 format.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The revision number for the booking used for optimistic concurrency.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
