

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .booking_backup import BookingBackup
from .booking_booked_by import BookingBookedBy


class Booking(UniversalBaseModel):
    dome: str = pydantic.Field()
    """
    Dome booked.
    """

    booked_by: typing_extensions.Annotated[
        typing.Optional[BookingBookedBy],
        FieldMetadata(alias="bookedBy"),
        pydantic.Field(alias="bookedBy", description="Who booked the time."),
    ] = None
    """
    Who booked the time.
    """

    backup: typing.Optional[BookingBackup] = None
    slot: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier of an observing slot.
    """

    nights: typing.Optional[int] = pydantic.Field(default=None)
    """
    Nights requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
