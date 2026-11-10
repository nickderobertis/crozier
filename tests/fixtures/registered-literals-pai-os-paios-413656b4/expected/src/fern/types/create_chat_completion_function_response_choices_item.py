

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_response_message import ChatCompletionResponseMessage
from .create_chat_completion_function_response_choices_item_finish_reason import (
    CreateChatCompletionFunctionResponseChoicesItemFinishReason,
)


class CreateChatCompletionFunctionResponseChoicesItem(UniversalBaseModel):
    finish_reason: CreateChatCompletionFunctionResponseChoicesItemFinishReason = pydantic.Field()
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, or `function_call` if the model called a function.
    """

    index: int = pydantic.Field()
    """
    The index of the choice in the list of choices.
    """

    message: ChatCompletionResponseMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
