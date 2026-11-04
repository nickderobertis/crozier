

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .openai_types_chat_chat_completion_message_function_tool_call_param_function import (
    OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction,
)


class ChatCompletionMessageFunctionToolCallParam(UniversalBaseModel):
    """
    A call to a function tool created by the model.
    """

    id: str
    function: OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
