

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_stream_event_message import ChatStreamEventMessage


class ChatStreamEvent(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model name used for this stream event
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When this chunk was created (ISO 8601)
    """

    message: typing.Optional[ChatStreamEventMessage] = None
    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True for the final event in the stream
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
