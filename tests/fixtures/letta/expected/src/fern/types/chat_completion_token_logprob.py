

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .top_logprob import TopLogprob


class ChatCompletionTokenLogprob(UniversalBaseModel):
    token: str
    bytes: typing.Optional[typing.List[int]] = None
    logprob: float
    top_logprobs: typing.List[TopLogprob]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
