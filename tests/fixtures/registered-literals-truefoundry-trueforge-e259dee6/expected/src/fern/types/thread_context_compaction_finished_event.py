

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compaction_trigger import CompactionTrigger
from .completion_usage import CompletionUsage


class ThreadContextCompactionFinishedEvent(UniversalBaseModel):
    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    duration_ms: int = pydantic.Field()
    """
    Wall time of the compaction model call in milliseconds.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    thread_id: str = pydantic.Field()
    """
    Thread whose context was compacted.
    """

    trigger: CompactionTrigger
    usage: CompletionUsage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
