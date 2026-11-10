

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_token_logprob import ChatCompletionTokenLogprob


class CreateChatCompletionStreamResponseChoicesItemLogprobs(UniversalBaseModel):
    """
    Log probability information for the choice.
    """

    content: typing.Optional[typing.List[ChatCompletionTokenLogprob]] = pydantic.Field(default=None)
    """
    A list of message content tokens with log probability information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
