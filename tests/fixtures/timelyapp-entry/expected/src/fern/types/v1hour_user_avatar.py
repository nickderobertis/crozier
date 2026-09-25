

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1HourUserAvatar(UniversalBaseModel):
    large_retina: str
    large: str
    medium_retina: str
    medium: str
    small_retina: typing.Optional[str] = None
    small: typing.Optional[str] = None
    timeline: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
