

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_info import AgentInfo
from .agent_parent import AgentParent


class ThreadCreatedEvent(UniversalBaseModel):
    agent_info: AgentInfo
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    parent: AgentParent
    thread_id: str = pydantic.Field()
    """
    Id of the new thread.
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
