

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResponseResourceUsageOutputTokensDetails(UniversalBaseModel):
    """
    A breakdown of output token usage that was recorded.
    """

    reasoning_tokens: int = pydantic.Field()
    """
    The number of output tokens that were attributed to reasoning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
