

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_function_tool_call_input_type import ChatCompletionMessageFunctionToolCallInputType
from .openai_types_chat_chat_completion_message_function_tool_call_function import (
    OpenaiTypesChatChatCompletionMessageFunctionToolCallFunction,
)


class ChatCompletionMessageFunctionToolCallInput(UniversalBaseModel):
    """
    A call to a function tool created by the model.
    """

    id: str
    function: OpenaiTypesChatChatCompletionMessageFunctionToolCallFunction
    type: ChatCompletionMessageFunctionToolCallInputType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
