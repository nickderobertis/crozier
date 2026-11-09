

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_response_message import ChatCompletionResponseMessage
from .create_chat_completion_response_choices_item_finish_reason import (
    CreateChatCompletionResponseChoicesItemFinishReason,
)
from .create_chat_completion_response_choices_item_logprobs import CreateChatCompletionResponseChoicesItemLogprobs


class CreateChatCompletionResponseChoicesItem(UniversalBaseModel):
    finish_reason: CreateChatCompletionResponseChoicesItemFinishReason = pydantic.Field()
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    `content_filter` if content was omitted due to a flag from our content filters,
    `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """

    index: int = pydantic.Field()
    """
    The index of the choice in the list of choices.
    """

    message: ChatCompletionResponseMessage
    logprobs: typing.Optional[CreateChatCompletionResponseChoicesItemLogprobs] = pydantic.Field(default=None)
    """
    Log probability information for the choice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
