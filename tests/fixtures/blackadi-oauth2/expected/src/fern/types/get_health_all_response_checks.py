

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_health_all_response_checks_authlete import GetHealthAllResponseChecksAuthlete
from .get_health_all_response_checks_redis import GetHealthAllResponseChecksRedis


class GetHealthAllResponseChecks(UniversalBaseModel):
    redis: typing.Optional[GetHealthAllResponseChecksRedis] = None
    authlete: typing.Optional[GetHealthAllResponseChecksAuthlete] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
