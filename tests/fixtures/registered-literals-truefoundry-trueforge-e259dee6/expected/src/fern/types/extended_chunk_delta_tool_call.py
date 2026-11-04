

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .chat_completion_chunk_delta_tool_call import ChatCompletionChunkDeltaToolCall
from .tool_info import ToolInfo


class ExtendedChunkDeltaToolCall(ChatCompletionChunkDeltaToolCall):
    provider_specific_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    tool_info: typing.Optional[ToolInfo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
