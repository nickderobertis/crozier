

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .place_fulfillment_order_request_items_item_bundle_items_item import (
    PlaceFulfillmentOrderRequestItemsItemBundleItemsItem,
)
from .place_fulfillment_order_request_items_item_item_attachment import (
    PlaceFulfillmentOrderRequestItemsItemItemAttachment,
)
from .place_fulfillment_order_request_items_item_price_tags_item import (
    PlaceFulfillmentOrderRequestItemsItemPriceTagsItem,
)


class PlaceFulfillmentOrderRequestItemsItem(UniversalBaseModel):
    attachments: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array containing information on attachments.
    """

    bundle_items: typing_extensions.Annotated[
        typing.Optional[typing.List[PlaceFulfillmentOrderRequestItemsItemBundleItemsItem]],
        FieldMetadata(alias="bundleItems"),
        pydantic.Field(
            alias="bundleItems", description="Information on services sold along with the SKU. Example: a gift package."
        ),
    ] = None
    """
    Information on services sold along with the SKU. Example: a gift package.
    """

    commission: typing.Optional[int] = pydantic.Field(default=None)
    """
    Comission.
    """

    freight_commission: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="freightCommission"),
        pydantic.Field(alias="freightCommission", description="Freight comission"),
    ] = None
    """
    Freight comission
    """

    id: str = pydantic.Field()
    """
    The SKU ID.
    """

    is_gift: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isGift"),
        pydantic.Field(alias="isGift", description="Indicates whether the order is a gift."),
    ] = None
    """
    Indicates whether the order is a gift.
    """

    item_attachment: typing_extensions.Annotated[
        typing.Optional[PlaceFulfillmentOrderRequestItemsItemItemAttachment],
        FieldMetadata(alias="itemAttachment"),
        pydantic.Field(alias="itemAttachment", description="Item attachment."),
    ] = None
    """
    Item attachment.
    """

    measurement_unit: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="measurementUnit"),
        pydantic.Field(alias="measurementUnit", description="SKU measurement unit."),
    ] = None
    """
    SKU measurement unit.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Item price within the context of the order without separating cents. For example, $24.99 is represented `2499`.
    """

    price_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[PlaceFulfillmentOrderRequestItemsItemPriceTagsItem]],
        FieldMetadata(alias="priceTags"),
        pydantic.Field(
            alias="priceTags",
            description="Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.",
        ),
    ] = None
    """
    Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
    """

    quantity: int = pydantic.Field()
    """
    The quantity of items of this specific SKU in the cart to be simulated.
    """

    seller: str = pydantic.Field()
    """
    The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin.
    """

    unit_multiplier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unitMultiplier"),
        pydantic.Field(alias="unitMultiplier", description="SKU unit multiplier."),
    ] = None
    """
    SKU unit multiplier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
