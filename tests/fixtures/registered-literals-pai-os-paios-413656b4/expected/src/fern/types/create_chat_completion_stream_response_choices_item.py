

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta
from .create_chat_completion_stream_response_choices_item_finish_reason import (
    CreateChatCompletionStreamResponseChoicesItemFinishReason,
)
from .create_chat_completion_stream_response_choices_item_logprobs import (
    CreateChatCompletionStreamResponseChoicesItemLogprobs,
)


class CreateChatCompletionStreamResponseChoicesItem(UniversalBaseModel):
    delta: ChatCompletionStreamResponseDelta
    logprobs: typing.Optional[CreateChatCompletionStreamResponseChoicesItemLogprobs] = pydantic.Field(default=None)
    """
    Log probability information for the choice.
    """

    finish_reason: typing.Optional[CreateChatCompletionStreamResponseChoicesItemFinishReason] = pydantic.Field(
        default=None
    )
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
