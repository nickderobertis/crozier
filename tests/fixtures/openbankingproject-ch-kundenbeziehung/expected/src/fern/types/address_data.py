

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .address_data_previous_addresses_item import AddressDataPreviousAddressesItem


class AddressData(UniversalBaseModel):
    residential_address: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="residentialAddress"), pydantic.Field(alias="residentialAddress")
    ] = None
    mailing_address: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="mailingAddress"), pydantic.Field(alias="mailingAddress")
    ] = None
    business_address: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="businessAddress"), pydantic.Field(alias="businessAddress")
    ] = None
    previous_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[AddressDataPreviousAddressesItem]],
        FieldMetadata(alias="previousAddresses"),
        pydantic.Field(alias="previousAddresses"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
