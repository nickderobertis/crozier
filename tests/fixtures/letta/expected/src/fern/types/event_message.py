

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_message_event_type import EventMessageEventType


class EventMessage(UniversalBaseModel):
    """
    A message for notifying the developer that an event that has occured (e.g. a compaction). Events are NOT part of the context window.
    """

    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    seq_id: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    event_type: EventMessageEventType
    event_data: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
