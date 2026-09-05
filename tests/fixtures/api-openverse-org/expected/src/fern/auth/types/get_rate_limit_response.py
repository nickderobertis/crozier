

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetRateLimitResponse(UniversalBaseModel):
    rate_limit_model: typing.Optional[str] = None
    requests_this_minute: typing.Optional[int] = None
    requests_today: typing.Optional[int] = None
    verified: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
