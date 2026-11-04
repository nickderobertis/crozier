

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResponseInProgressStreamingEventResponseUsageInputTokensDetails(UniversalBaseModel):
    """
    A breakdown of input token usage that was recorded.
    """

    cached_tokens: int = pydantic.Field()
    """
    The number of input tokens that were served from cache.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
