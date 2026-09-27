

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id import EventId
from ...types.href_event import HrefEvent
from ...types.timestamp_res_event import TimestampResEvent


class CreateEventResponse(UniversalBaseModel):
    """
    Create New Event Response Payload Object
    """

    href: typing.Optional[HrefEvent] = None
    id: typing.Optional[EventId] = None
    timestamp: typing.Optional[TimestampResEvent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
