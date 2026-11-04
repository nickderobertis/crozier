

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .top_log_prob import TopLogProb


class LogProb(UniversalBaseModel):
    """
    The log probability of a token.
    """

    token: str
    logprob: float
    bytes: typing.List[int]
    top_logprobs: typing.List[TopLogProb]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
