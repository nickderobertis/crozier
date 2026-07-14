

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_response_event import EventResponseEvent


class EventResponse(UniversalBaseModel):
    """
    A record of occurance of an asynchronous event triggered either by system or by user activity
    """

    created_at: typing.Optional[dt.datetime] = None
    event: typing.Optional[EventResponseEvent] = None
    generated_uuid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
