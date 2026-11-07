

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .openai_types_chat_chat_completion_message_custom_tool_call_param_custom import (
    OpenaiTypesChatChatCompletionMessageCustomToolCallParamCustom,
)


class ChatCompletionMessageCustomToolCallParam(UniversalBaseModel):
    """
    A call to a custom tool created by the model.
    """

    id: str
    custom: OpenaiTypesChatChatCompletionMessageCustomToolCallParamCustom

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
