

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .geo_coordinates import GeoCoordinates


class SelectedAddress(UniversalBaseModel):
    """
    List with the delivery addresses selected for the order. We currently only support a single delivery address.
    """

    address_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="addressId"),
        pydantic.Field(
            alias="addressId",
            description="String with the address identifier. Optional for `delivery` type orders, and required for `pickup-in-point` orders.",
        ),
    ]
    """
    String with the address identifier. Optional for `delivery` type orders, and required for `pickup-in-point` orders.
    """

    address_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="addressType"),
        pydantic.Field(
            alias="addressType",
            description="String with the address type. The field supports the values: `residential`, `commercial`, `pickup`.",
        ),
    ]
    """
    String with the address type. The field supports the values: `residential`, `commercial`, `pickup`.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the city’s name.
    """

    complement: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the address' complement, like building name, or extra number.
    """

    country: str = pydantic.Field()
    """
    String with the state's name, filled in with three letter code.
    """

    geo_coordinates: typing_extensions.Annotated[
        typing.Optional[GeoCoordinates], FieldMetadata(alias="geoCoordinates"), pydantic.Field(alias="geoCoordinates")
    ] = None
    neighborhood: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the neighborhood's name.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the street's number.
    """

    postal_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="postalCode"),
        pydantic.Field(alias="postalCode", description="String with the address' postal code."),
    ]
    """
    String with the address' postal code.
    """

    receiver_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="receiverName"),
        pydantic.Field(
            alias="receiverName", description="String with the name of the person responsible for receiving the order."
        ),
    ]
    """
    String with the name of the person responsible for receiving the order.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the state's name, filled in with two letter code.
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    String with the street's name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
