

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.bundle_items_item import BundleItemsItem
from ...types.item_attachment import ItemAttachment
from .order_placement_items_item_price_tags_item import OrderPlacementItemsItemPriceTagsItem


class OrderPlacementItemsItem(UniversalBaseModel):
    attachments: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Array containing information on attachments.
    """

    bundle_items: typing_extensions.Annotated[
        typing.Optional[typing.List[BundleItemsItem]],
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
        pydantic.Field(alias="freightCommission", description="Freight comission."),
    ] = None
    """
    Freight comission.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    SKU ID.
    """

    is_gift: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isGift"),
        pydantic.Field(alias="isGift", description="`true` if the item is a gift."),
    ] = None
    """
    `true` if the item is a gift.
    """

    items_attachment: typing_extensions.Annotated[
        typing.Optional[typing.List[ItemAttachment]],
        FieldMetadata(alias="itemsAttachment"),
        pydantic.Field(alias="itemsAttachment", description="Attachments sold with the SKU."),
    ] = None
    """
    Attachments sold with the SKU.
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
    SKU price. The last two digits are the cents. For example, $24.99 is represented 2499.
    """

    price_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[OrderPlacementItemsItemPriceTagsItem]],
        FieldMetadata(alias="priceTags"),
        pydantic.Field(
            alias="priceTags",
            description="Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.",
        ),
    ] = None
    """
    Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Quantity of the item.
    """

    seller: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the seller registered in VTEX.
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
