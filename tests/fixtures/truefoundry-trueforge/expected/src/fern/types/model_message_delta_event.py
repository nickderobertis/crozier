

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extended_chunk_delta_tool_call import ExtendedChunkDeltaToolCall
from .finish_reason import FinishReason
from .model_message_usage import ModelMessageUsage


class ModelMessageDeltaEvent(UniversalBaseModel):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Incremental assistant text content.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional ISO 8601 event timestamp.
    """

    finish_reason: typing.Optional[FinishReason] = pydantic.Field(default=None)
    """
    Finish reason when this delta completes the stream.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    reasoning_content: typing.Optional[str] = None
    refusal: typing.Optional[str] = pydantic.Field(default=None)
    """
    Incremental refusal text when present.
    """

    thread_id: str = pydantic.Field()
    """
    Thread that emitted this delta.
    """

    tool_calls: typing.Optional[typing.List[ExtendedChunkDeltaToolCall]] = None
    usage: typing.Optional[ModelMessageUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
