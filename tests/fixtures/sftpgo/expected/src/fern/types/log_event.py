

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_protocols import EventProtocols
from .log_event_type import LogEventType


class LogEvent(UniversalBaseModel):
    id: typing.Optional[str] = None
    timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    unix timestamp in nanoseconds
    """

    event: typing.Optional[LogEventType] = None
    protocol: typing.Optional[EventProtocols] = None
    username: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    message: typing.Optional[str] = None
    role: typing.Optional[str] = None
    instance_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
