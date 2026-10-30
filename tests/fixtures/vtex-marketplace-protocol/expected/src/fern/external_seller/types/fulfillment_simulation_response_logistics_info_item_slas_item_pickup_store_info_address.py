

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress(UniversalBaseModel):
    """
    Address data of the pickup point.
    """

    address_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="addressId"),
        pydantic.Field(alias="addressId", description="Identifies the pickup point."),
    ]
    """
    Identifies the pickup point.
    """

    address_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="addressType"),
        pydantic.Field(alias="addressType", description="The possible value is pickup."),
    ]
    """
    The possible value is pickup.
    """

    city: str = pydantic.Field()
    """
    Pickup point's city.
    """

    complement: str = pydantic.Field()
    """
    Complement of the pickup point address.
    """

    country: str = pydantic.Field()
    """
    3-digit ISO code of the country where the pickup point is located.
    """

    geo_coordinates: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="geoCoordinates"),
        pydantic.Field(alias="geoCoordinates", description="Contains the geographic coordinates of the pickup point."),
    ]
    """
    Contains the geographic coordinates of the pickup point.
    """

    neighborhood: str = pydantic.Field()
    """
    Neighborhood where the pickup point is located.
    """

    number: str = pydantic.Field()
    """
    Address number of the pickup point.
    """

    postal_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="postalCode"),
        pydantic.Field(
            alias="postalCode",
            description="Postal code of the pickup point. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.",
        ),
    ]
    """
    Postal code of the pickup point. This field is mandatory, for shopping carts simulations, where both Country and Postal Code are required. This field should be sent as `null` for storefront simulations, where the information is not necessary.
    """

    receiver_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="receiverName"),
        pydantic.Field(
            alias="receiverName", description="Name of the person who will receive the product. May be sent as `null`."
        ),
    ] = None
    """
    Name of the person who will receive the product. May be sent as `null`.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    A reference for the pickup point address. 
    """

    state: str = pydantic.Field()
    """
    Pickup point's state.
    """

    street: str = pydantic.Field()
    """
    Street where the pickup point is located.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
