

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_address_type import AddressAddressType


class Address(UniversalBaseModel):
    street: str = pydantic.Field()
    """
    Straße und Hausnummer
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressLine2"),
        pydantic.Field(alias="addressLine2", description="Adresszusatz"),
    ] = None
    """
    Adresszusatz
    """

    postal_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode", description="Postleitzahl")
    ]
    """
    Postleitzahl
    """

    city: str = pydantic.Field()
    """
    Ort
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Kanton/Region
    """

    country: str = pydantic.Field()
    """
    Land (ISO 3166-1)
    """

    address_type: typing_extensions.Annotated[
        typing.Optional[AddressAddressType], FieldMetadata(alias="addressType"), pydantic.Field(alias="addressType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
