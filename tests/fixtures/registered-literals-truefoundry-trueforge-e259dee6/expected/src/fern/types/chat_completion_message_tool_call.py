

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_tool_call_function import ChatCompletionMessageToolCallFunction
from .chat_completion_message_tool_call_type import ChatCompletionMessageToolCallType


class ChatCompletionMessageToolCall(UniversalBaseModel):
    function: ChatCompletionMessageToolCallFunction
    id: str = pydantic.Field()
    """
    Tool call id.
    """

    type: ChatCompletionMessageToolCallType = pydantic.Field()
    """
    Tool call type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
