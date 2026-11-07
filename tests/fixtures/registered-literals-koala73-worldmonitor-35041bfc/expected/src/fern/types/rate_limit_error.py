

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RateLimitError(UniversalBaseModel):
    """
    Returned when a gateway or handler rate limit rejects the request.
    """

    error: str = pydantic.Field()
    """
    Human-readable rate-limit failure reason.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
