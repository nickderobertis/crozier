

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateCartAddressRequestDataAttributes(UniversalBaseModel):
    address_type: typing.Optional[str] = None
    city: typing.Optional[str] = None
    company_in: typing.Optional[str] = None
    company_name: typing.Optional[str] = None
    company_tin: typing.Optional[str] = None
    contact_email: typing.Optional[str] = None
    contact_phone: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    line_one: typing.Optional[str] = None
    postcode: typing.Optional[str] = None
    shipping_option: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
