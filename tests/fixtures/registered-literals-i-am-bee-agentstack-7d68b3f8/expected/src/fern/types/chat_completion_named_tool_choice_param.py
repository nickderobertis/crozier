

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_named_tool_choice_param_type import ChatCompletionNamedToolChoiceParamType
from .openai_types_chat_chat_completion_named_tool_choice_param_function import (
    OpenaiTypesChatChatCompletionNamedToolChoiceParamFunction,
)


class ChatCompletionNamedToolChoiceParam(UniversalBaseModel):
    """
    Specifies a tool the model should use.

    Use to force the model to call a specific function.
    """

    function: OpenaiTypesChatChatCompletionNamedToolChoiceParamFunction
    type: ChatCompletionNamedToolChoiceParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
