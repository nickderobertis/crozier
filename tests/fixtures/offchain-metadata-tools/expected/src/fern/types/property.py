

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .property_decimals import PropertyDecimals
from .property_description import PropertyDescription
from .property_logo import PropertyLogo
from .property_name import PropertyName
from .property_ticker import PropertyTicker
from .property_url import PropertyUrl


class Property(UniversalBaseModel):
    subject: typing.Any
    policy: typing.Optional[typing.Any] = None
    name: typing.Optional[PropertyName] = None
    description: typing.Optional[PropertyDescription] = None
    url: typing.Optional[PropertyUrl] = None
    ticker: typing.Optional[PropertyTicker] = None
    decimals: typing.Optional[PropertyDecimals] = None
    logo: typing.Optional[PropertyLogo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
