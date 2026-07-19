

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_object import ChatCompletionObject
from .chat_completion_service_tier import ChatCompletionServiceTier
from .choice import Choice
from .completion_usage import CompletionUsage


class ChatCompletion(UniversalBaseModel):
    """
    Represents a chat completion response returned by model, based on the provided input.
    """

    id: str
    choices: typing.List[Choice]
    created: int
    model: str
    object: ChatCompletionObject
    service_tier: typing.Optional[ChatCompletionServiceTier] = None
    system_fingerprint: typing.Optional[str] = None
    usage: typing.Optional[CompletionUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
