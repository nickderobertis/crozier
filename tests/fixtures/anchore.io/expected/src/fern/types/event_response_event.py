

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_response_event_resource import EventResponseEventResource
from .event_response_event_source import EventResponseEventSource


class EventResponseEvent(UniversalBaseModel):
    category: typing.Optional[str] = None
    details: typing.Optional[typing.Dict[str, typing.Any]] = None
    level: typing.Optional[str] = None
    message: typing.Optional[str] = None
    resource: typing.Optional[EventResponseEventResource] = None
    source: typing.Optional[EventResponseEventSource] = None
    timestamp: typing.Optional[dt.datetime] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
