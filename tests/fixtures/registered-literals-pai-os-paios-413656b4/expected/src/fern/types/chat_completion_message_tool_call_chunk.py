

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_tool_call_chunk_function import ChatCompletionMessageToolCallChunkFunction
from .chat_completion_message_tool_call_chunk_type import ChatCompletionMessageToolCallChunkType


class ChatCompletionMessageToolCallChunk(UniversalBaseModel):
    index: int
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tool call.
    """

    type: typing.Optional[ChatCompletionMessageToolCallChunkType] = pydantic.Field(default=None)
    """
    The type of the tool. Currently, only `function` is supported.
    """

    function: typing.Optional[ChatCompletionMessageToolCallChunkFunction] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
