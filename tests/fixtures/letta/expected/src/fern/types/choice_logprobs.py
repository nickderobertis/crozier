

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_token_logprob import ChatCompletionTokenLogprob


class ChoiceLogprobs(UniversalBaseModel):
    """
    Log probability information for the choice.
    """

    content: typing.Optional[typing.List[ChatCompletionTokenLogprob]] = None
    refusal: typing.Optional[typing.List[ChatCompletionTokenLogprob]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
