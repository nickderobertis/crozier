

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_response_items_item_offerings_item import (
    FulfillmentSimulationResponseItemsItemOfferingsItem,
)


class FulfillmentSimulationResponseItemsItem(UniversalBaseModel):
    """
    Contains the data about each SKU in the cart.
    """

    id: str = pydantic.Field()
    """
    SKU ID
    """

    list_price: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="listPrice"),
        pydantic.Field(
            alias="listPrice",
            description="List price. It’s the amount presented to the customer as a “previous” price that has been lowered due to a discount. Don’t separate the decimal places. The last two digits are the cents.",
        ),
    ]
    """
    List price. It’s the amount presented to the customer as a “previous” price that has been lowered due to a discount. Don’t separate the decimal places. The last two digits are the cents.
    """

    measurement_unit: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="measurementUnit"),
        pydantic.Field(alias="measurementUnit", description="SKU’s measurement unit."),
    ]
    """
    SKU’s measurement unit.
    """

    merchant_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantName"),
        pydantic.Field(
            alias="merchantName",
            description="Name of the marketplace, used to guide payments. This field should be nulled if the marketplace is responsible for processing payments. Check out our [​​Payments in VTEX marketplaces](https://help.vtex.com/en/tutorial/payments-in-vtex-marketplaces--2kYOfWCZYweJkYl18bw9yD) article to know more.",
        ),
    ]
    """
    Name of the marketplace, used to guide payments. This field should be nulled if the marketplace is responsible for processing payments. Check out our [​​Payments in VTEX marketplaces](https://help.vtex.com/en/tutorial/payments-in-vtex-marketplaces--2kYOfWCZYweJkYl18bw9yD) article to know more.
    """

    offerings: typing.List[FulfillmentSimulationResponseItemsItemOfferingsItem] = pydantic.Field()
    """
    Services that may be offered for this SKU. example are the assembly of a piece of furniture or warranty. In case these information are sent, the following fields are mandatory. If you don’t want to send it, use an empty array.
    """

    price: int = pydantic.Field()
    """
    Actual selling price of the SKU. Don’t separate the decimal places. The last two digits are the cents.
    """

    price_tags: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="priceTags"),
        pydantic.Field(alias="priceTags", description="List with the promotions applied to the SKU."),
    ]
    """
    List with the promotions applied to the SKU.
    """

    price_valid_until: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priceValidUntil"),
        pydantic.Field(
            alias="priceValidUntil",
            description="Expiration date of the SKU price. Example: `2014-03-01T22:58:28.143`. In case you don’t want to send it, use the value null.",
        ),
    ] = None
    """
    Expiration date of the SKU price. Example: `2014-03-01T22:58:28.143`. In case you don’t want to send it, use the value null.
    """

    quantity: int = pydantic.Field()
    """
    Quantity of the item. The seller should send the quantity that was indicated in the request, or the maximum quantity possible.
    """

    request_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="requestIndex"),
        pydantic.Field(alias="requestIndex", description="Position of this item in the original array (request)."),
    ]
    """
    Position of this item in the original array (request).
    """

    seller: str = pydantic.Field()
    """
    ID of the seller as registered in VTEX. You should send the same value that came in the request.
    """

    unit_multiplier: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="unitMultiplier"),
        pydantic.Field(alias="unitMultiplier", description="SKU unit multiplier. The default value is 1."),
    ]
    """
    SKU unit multiplier. The default value is 1.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
