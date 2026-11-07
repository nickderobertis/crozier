

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_parent import AgentParent
from .thread_state import ThreadState


class ThreadDoneEvent(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    parent: typing.Optional[AgentParent] = None
    state: ThreadState
    thread_id: str = pydantic.Field()
    """
    Thread that finished.
    """

    title: str = pydantic.Field()
    """
    Human-readable thread title.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
