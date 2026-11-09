

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_object import ThreadObject
from .thread_stream_event_event import ThreadStreamEventEvent


class ThreadStreamEvent(UniversalBaseModel):
    """
    Occurs when a new [thread](/docs/api-reference/threads/object) is created.
    """

    event: ThreadStreamEventEvent
    data: ThreadObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
