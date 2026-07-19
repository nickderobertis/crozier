

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_input import CustomInput
from .openai_types_chat_chat_completion_message_function_tool_call_param_function import (
    OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction,
)


class ChatCompletionAssistantMessageParamToolCallsItem_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    id: str
    function: OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionAssistantMessageParamToolCallsItem_Custom(UniversalBaseModel):
    type: typing.Literal["custom"] = "custom"
    id: str
    custom: CustomInput

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionAssistantMessageParamToolCallsItem = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionAssistantMessageParamToolCallsItem_Function,
        ChatCompletionAssistantMessageParamToolCallsItem_Custom,
    ],
    pydantic.Field(discriminator="type"),
]
