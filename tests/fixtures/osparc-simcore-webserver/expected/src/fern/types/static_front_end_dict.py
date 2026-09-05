

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .country_info_dict import CountryInfoDict
from .third_party_info_dict import ThirdPartyInfoDict


class StaticFrontEndDict(UniversalBaseModel):
    third_party_references: typing.List[ThirdPartyInfoDict]
    countries: typing.List[CountryInfoDict]
    issues: typing.Optional[typing.Any] = None
    vendor: typing.Optional[typing.Any] = None
    manuals: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
