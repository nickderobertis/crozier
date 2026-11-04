

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_duration import JsonDuration


class PatchClaimsRequest(UniversalBaseModel):
    audience: typing.Optional[typing.List[str]] = None
    ttl: typing.Optional[JsonDuration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
