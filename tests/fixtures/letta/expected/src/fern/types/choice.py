

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message import ChatCompletionMessage
from .choice_finish_reason import ChoiceFinishReason
from .choice_logprobs import ChoiceLogprobs


class Choice(UniversalBaseModel):
    finish_reason: ChoiceFinishReason
    index: int
    logprobs: typing.Optional[ChoiceLogprobs] = None
    message: ChatCompletionMessage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
