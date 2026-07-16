

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutShopRequestAddress(UniversalBaseModel):
    country_code: typing.Optional[str] = None
    extended_address: typing.Optional[str] = None
    locality: typing.Optional[str] = None
    name: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    postal_code: typing.Optional[str] = None
    region: typing.Optional[str] = None
    street_address: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
