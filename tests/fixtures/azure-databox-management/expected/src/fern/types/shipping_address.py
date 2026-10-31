

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .shipping_address_address_type import ShippingAddressAddressType


class ShippingAddress(UniversalBaseModel):
    """
    Shipping address where customer wishes to receive the device.
    """

    address_type: typing_extensions.Annotated[
        typing.Optional[ShippingAddressAddressType],
        FieldMetadata(alias="addressType"),
        pydantic.Field(alias="addressType", description="Type of address."),
    ] = None
    """
    Type of address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the City.
    """

    company_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="companyName"),
        pydantic.Field(alias="companyName", description="Name of the company."),
    ] = None
    """
    Name of the company.
    """

    country: str = pydantic.Field()
    """
    Name of the Country.
    """

    postal_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode", description="Postal code.")
    ]
    """
    Postal code.
    """

    state_or_province: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stateOrProvince"),
        pydantic.Field(alias="stateOrProvince", description="Name of the State or Province."),
    ] = None
    """
    Name of the State or Province.
    """

    street_address1: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="streetAddress1"),
        pydantic.Field(alias="streetAddress1", description="Street Address line 1."),
    ]
    """
    Street Address line 1.
    """

    street_address2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="streetAddress2"),
        pydantic.Field(alias="streetAddress2", description="Street Address line 2."),
    ] = None
    """
    Street Address line 2.
    """

    street_address3: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="streetAddress3"),
        pydantic.Field(alias="streetAddress3", description="Street Address line 3."),
    ] = None
    """
    Street Address line 3.
    """

    zip_extended_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="zipExtendedCode"),
        pydantic.Field(alias="zipExtendedCode", description="Extended Zip Code."),
    ] = None
    """
    Extended Zip Code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
