

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .events_get_response_data_events_item_involved_object import EventsGetResponseDataEventsItemInvolvedObject


class EventsGetResponseDataEventsItem(UniversalBaseModel):
    last_timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastTimestamp"),
        pydantic.Field(alias="lastTimestamp", description="Last time the event occurred"),
    ] = None
    """
    Last time the event occurred
    """

    type: str = pydantic.Field()
    """
    Event type (Normal, Warning)
    """

    reason: str = pydantic.Field()
    """
    Short reason for the event
    """

    message: str = pydantic.Field()
    """
    Human-readable description
    """

    involved_object: typing_extensions.Annotated[
        EventsGetResponseDataEventsItemInvolvedObject,
        FieldMetadata(alias="involvedObject"),
        pydantic.Field(alias="involvedObject", description="Object this event is about"),
    ]
    """
    Object this event is about
    """

    count: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of times this event has occurred
    """

    first_timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstTimestamp"),
        pydantic.Field(alias="firstTimestamp", description="First time the event occurred"),
    ] = None
    """
    First time the event occurred
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
