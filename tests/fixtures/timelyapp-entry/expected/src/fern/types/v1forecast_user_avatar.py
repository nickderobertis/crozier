

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ForecastUserAvatar(UniversalBaseModel):
    large_retina: typing.Optional[str] = None
    large: typing.Optional[str] = None
    medium_retina: typing.Optional[str] = None
    medium: typing.Optional[str] = None
    timeline: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
