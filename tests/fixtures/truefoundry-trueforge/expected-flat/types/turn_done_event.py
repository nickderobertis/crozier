

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .turn_done_event_state import TurnDoneEventState


class TurnDoneEvent(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    state: TurnDoneEventState = pydantic.Field()
    """
    Terminal turn state (done, cancelled, or error).
    """

    thread_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Thread that owns the event; null for turn-level lifecycle events.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
