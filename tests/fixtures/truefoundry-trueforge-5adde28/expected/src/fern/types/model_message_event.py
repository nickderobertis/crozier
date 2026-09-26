

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .finish_reason import FinishReason
from .model_message_event_content import ModelMessageEventContent
from .model_message_event_type import ModelMessageEventType
from .model_message_usage import ModelMessageUsage
from .tool_call import ToolCall


class ModelMessageEvent(UniversalBaseModel):
    content: typing.Optional[ModelMessageEventContent] = pydantic.Field(default=None)
    """
    Assistant message content as text or content parts.
    """

    created_at: str = pydantic.Field()
    """
    ISO 8601 event timestamp.
    """

    finish_reason: typing.Optional[FinishReason] = pydantic.Field(default=None)
    """
    Model finish reason; null when the provider omitted it.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the event (monotonic ULID).
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional participant name.
    """

    reasoning_content: typing.Optional[str] = None
    refusal: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional refusal text.
    """

    thread_id: str = pydantic.Field()
    """
    Thread that emitted this message (`main` for the root agent).
    """

    tool_calls: typing.Optional[typing.List[ToolCall]] = None
    type: ModelMessageEventType = pydantic.Field()
    """
    Complete assistant model message.
    """

    usage: typing.Optional[ModelMessageUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
