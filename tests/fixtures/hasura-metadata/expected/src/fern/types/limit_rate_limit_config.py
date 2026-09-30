

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rate_limit_config import RateLimitConfig


class LimitRateLimitConfig(UniversalBaseModel):
    global_: typing_extensions.Annotated[RateLimitConfig, FieldMetadata(alias="global"), pydantic.Field(alias="global")]
    per_role: typing.Optional[typing.Dict[str, RateLimitConfig]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
