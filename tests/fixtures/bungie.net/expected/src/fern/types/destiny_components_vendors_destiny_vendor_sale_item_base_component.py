

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyComponentsVendorsDestinyVendorSaleItemBaseComponent(UniversalBaseModel):
    """
    The base class for Vendor Sale Item data. Has a bunch of character-agnostic state about the item being sold.
    Note that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's "items" property.
    """

    api_purchasable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="apiPurchasable"),
        pydantic.Field(
            alias="apiPurchasable", description="If true, this item can be purchased through the Bungie.net API."
        ),
    ] = None
    """
    If true, this item can be purchased through the Bungie.net API.
    """

    costs: typing.Optional[typing.List[DestinyDestinyItemQuantity]] = pydantic.Field(default=None)
    """
    A summary of the current costs of the item.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.",
        ),
    ] = None
    """
    The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
    """

    override_next_refresh_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="overrideNextRefreshDate"),
        pydantic.Field(
            alias="overrideNextRefreshDate",
            description="If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date.\r\nNote that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.",
        ),
    ] = None
    """
    If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date.
    Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
    """

    override_style_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="overrideStyleItemHash"),
        pydantic.Field(
            alias="overrideStyleItemHash",
            description="If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.\r\nIf you don't do this, certain items whose styles are being overridden by socketed items - such as the \"Recycle Shader\" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.",
        ),
    ] = None
    """
    If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold.
    If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    How much of the item you'll be getting.
    """

    vendor_item_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorItemIndex"),
        pydantic.Field(
            alias="vendorItemIndex",
            description="The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch. \r\nMost systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.",
        ),
    ] = None
    """
    The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch. 
    Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
