

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rate_limit_config_unique_params import RateLimitConfigUniqueParams


class RateLimitConfig(UniversalBaseModel):
    max_reqs_per_min: float
    unique_params: typing.Optional[RateLimitConfigUniqueParams] = pydantic.Field(default=None)
    """
    This would be either fixed value "IP" or a list of Session variables
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
