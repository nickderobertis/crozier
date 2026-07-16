

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_dates import EventDates
from .event_description import EventDescription
from .event_id import EventId
from .event_location import EventLocation
from .event_name import EventName
from .event_price import EventPrice


class SpecialEvent(UniversalBaseModel):
    event_id: typing_extensions.Annotated[typing.Optional[EventId], FieldMetadata(alias="eventId")] = None
    name: EventName
    location: EventLocation
    event_description: typing_extensions.Annotated[EventDescription, FieldMetadata(alias="eventDescription")]
    dates: EventDates
    price: EventPrice

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
