

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_named_tool_choice_function import ChatCompletionNamedToolChoiceFunction
from .chat_completion_named_tool_choice_type import ChatCompletionNamedToolChoiceType


class ChatCompletionNamedToolChoice(UniversalBaseModel):
    """
    Specifies a tool the model should use. Use to force the model to call a specific function.
    """

    type: ChatCompletionNamedToolChoiceType = pydantic.Field()
    """
    The type of the tool. Currently, only `function` is supported.
    """

    function: ChatCompletionNamedToolChoiceFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
