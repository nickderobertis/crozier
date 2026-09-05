

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MeLocation(UniversalBaseModel):
    city: typing.Optional[str] = None
    country: typing.Optional[int] = None
    ip_address: typing.Optional[str] = None
    latitude: typing.Optional[str] = None
    longitude: typing.Optional[str] = None
    region: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
