

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_thread_done_event import BaseThreadDoneEvent
from .thread_state import ThreadState


class ThreadDoneEvent(BaseThreadDoneEvent):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    state: ThreadState

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
