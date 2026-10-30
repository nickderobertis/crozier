

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PlaceFulfillmentOrderRequestShippingDataAddress(UniversalBaseModel):
    """
    Shipping address.
    """

    address_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressId"),
        pydantic.Field(alias="addressId", description="Address ID."),
    ] = None
    """
    Address ID.
    """

    address_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="addressType"),
        pydantic.Field(
            alias="addressType", description="Type of address. For example, `Residential` or `Pickup`, among others."
        ),
    ]
    """
    Type of address. For example, `Residential` or `Pickup`, among others.
    """

    city: str = pydantic.Field()
    """
    City of the shipping address.
    """

    complement: typing.Optional[str] = pydantic.Field(default=None)
    """
    Complement to the shipping address in case it applies.
    """

    country: str = pydantic.Field()
    """
    Three letter ISO code of the country of the shipping address.
    """

    geo_coordinates: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="geoCoordinates"),
        pydantic.Field(
            alias="geoCoordinates",
            description="Array with two strings with geocoordinates, first latitude, then longitude.",
        ),
    ] = None
    """
    Array with two strings with geocoordinates, first latitude, then longitude.
    """

    neighborhood: typing.Optional[str] = pydantic.Field(default=None)
    """
    Neighborhood of the shipping address.
    """

    number: str = pydantic.Field()
    """
    Number of the building, house or apartment in the shipping address.
    """

    postal_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="postalCode"),
        pydantic.Field(alias="postalCode", description="Postal Code. Validation depends on the country."),
    ]
    """
    Postal Code. Validation depends on the country.
    """

    receiver_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="receiverName"),
        pydantic.Field(alias="receiverName", description="Name of the person who is going to receive the order."),
    ]
    """
    Name of the person who is going to receive the order.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Complement that might help locate the shipping address more precisely in case of delivery.
    """

    state: str = pydantic.Field()
    """
    State of the shipping address.
    """

    street: str = pydantic.Field()
    """
    Street of the shipping address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
