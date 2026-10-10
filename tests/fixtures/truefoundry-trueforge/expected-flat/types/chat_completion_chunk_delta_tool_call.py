

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_chunk_delta_tool_call_function import ChatCompletionChunkDeltaToolCallFunction
from .chat_completion_chunk_delta_tool_call_type import ChatCompletionChunkDeltaToolCallType


class ChatCompletionChunkDeltaToolCall(UniversalBaseModel):
    function: typing.Optional[ChatCompletionChunkDeltaToolCallFunction] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tool call id (may arrive across multiple deltas).
    """

    index: int = pydantic.Field()
    """
    Index of this tool call in the streaming delta array.
    """

    type: typing.Optional[ChatCompletionChunkDeltaToolCallType] = pydantic.Field(default=None)
    """
    Tool call type when present on this delta.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
