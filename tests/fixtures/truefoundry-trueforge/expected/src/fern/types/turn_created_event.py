

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .turn_input_item import TurnInputItem
from .turn_state_running import TurnStateRunning


class TurnCreatedEvent(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    input: typing.Optional[typing.List[TurnInputItem]] = pydantic.Field(default=None)
    """
    Input items supplied when the turn was created.
    """

    previous_turn_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Prior turn this turn chains from; null for a root turn.
    """

    state: TurnStateRunning
    thread_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Thread that owns the event; null for turn-level lifecycle events.
    """

    turn_id: str = pydantic.Field()
    """
    Id of the newly created turn.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
