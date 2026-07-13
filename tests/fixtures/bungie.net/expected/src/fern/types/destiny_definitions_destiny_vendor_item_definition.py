

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_creation_entry_level_definition import (
    DestinyDefinitionsDestinyItemCreationEntryLevelDefinition,
)
from .destiny_definitions_destiny_vendor_item_quantity import DestinyDefinitionsDestinyVendorItemQuantity
from .destiny_definitions_destiny_vendor_item_socket_override import DestinyDefinitionsDestinyVendorItemSocketOverride
from .destiny_definitions_destiny_vendor_sale_item_action_block_definition import (
    DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition,
)


class DestinyDefinitionsDestinyVendorItemDefinition(UniversalBaseModel):
    """
    This represents an item being sold by the vendor.
    """

    action: typing.Optional[DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition] = pydantic.Field(default=None)
    """
    The action to be performed when purchasing the item, if it's not just "buy".
    """

    category_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="categoryIndex")] = (
        pydantic.Field(default=None)
    )
    """
    The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item.
    """

    creation_levels: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemCreationEntryLevelDefinition]],
        FieldMetadata(alias="creationLevels"),
    ] = pydantic.Field(default=None)
    """
    The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities.
    """

    currencies: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorItemQuantity]] = pydantic.Field(default=None)
    """
    This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately.
    The somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data.
    """

    display_category: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayCategory")] = (
        pydantic.Field(default=None)
    )
    """
    The string identifier for the category selling this item.
    """

    display_category_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="displayCategoryIndex")
    ] = pydantic.Field(default=None)
    """
    This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually)
    """

    exclusivity: typing.Optional[int] = pydantic.Field(default=None)
    """
    If this item can only be purchased by a given platform, this indicates the platform to which it is restricted.
    """

    expiration_tooltip: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="expirationTooltip")] = (
        pydantic.Field(default=None)
    )
    """
    If this item can expire, this is the tooltip message to show with its expiration info.
    """

    failure_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="failureIndexes")
    ] = pydantic.Field(default=None)
    """
    An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item.
    """

    inventory_bucket_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="inventoryBucketHash")
    ] = pydantic.Field(default=None)
    """
    The inventory bucket into which this item will be placed upon purchase.
    """

    is_crm: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isCrm")] = pydantic.Field(
        default=None
    )
    """
    If this sale can only be performed as the result of receiving a CRM offer, this is true.
    """

    is_offer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isOffer")] = pydantic.Field(
        default=None
    )
    """
    If this sale can only be performed as the result of an offer check, this is true.
    """

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier of the item being sold (DestinyInventoryItemDefinition).
    Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity.
    """

    maximum_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maximumLevel")] = (
        pydantic.Field(default=None)
    )
    """
    The maximum character level at which this item is available for sale.
    """

    minimum_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minimumLevel")] = (
        pydantic.Field(default=None)
    )
    """
    The minimum character level at which this item is available for sale.
    """

    original_category_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="originalCategoryIndex")
    ] = pydantic.Field(default=None)
    """
    Same as above, but for the original category indexes.
    """

    purchasable_scope: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="purchasableScope")] = (
        pydantic.Field(default=None)
    )
    """
    Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not.
    See DestinyGatingScope's documentation for more information.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount you will recieve of the item described in itemHash if you make the purchase.
    """

    redirect_to_sale_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="redirectToSaleIndexes")
    ] = pydantic.Field(default=None)
    """
    If this is populated, the purchase of this item should redirect to purchasing these other items instead.
    """

    refund_policy: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="refundPolicy")] = (
        pydantic.Field(default=None)
    )
    """
    If this item can be refunded, this is the policy for what will be refundd, how, and in what time period.
    """

    refund_time_limit: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="refundTimeLimit")] = (
        pydantic.Field(default=None)
    )
    """
    The amount of time before refundability of the newly purchased item will expire.
    """

    socket_overrides: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorItemSocketOverride]],
        FieldMetadata(alias="socketOverrides"),
    ] = None
    sort_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sortValue")] = pydantic.Field(
        default=None
    )
    """
    *if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go.
    """

    unpurchasable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this item is some sort of dummy sale item that cannot actually be purchased. It may be a display only item, or some fluff left by a content designer for testing purposes, or something that got disabled because it was a terrible idea. You get the picture. We won't know *why* it can't be purchased, only that it can't be. Sorry.
    This is also only whether it's unpurchasable as a static property according to game content. There are other reasons why an item may or may not be purchasable at runtime, so even if this isn't set to True you should trust the runtime value for this sale item over the static definition if this is unset.
    """

    vendor_item_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorItemIndex")] = (
        pydantic.Field(default=None)
    )
    """
    The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data.
    """

    visibility_scope: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="visibilityScope")] = (
        pydantic.Field(default=None)
    )
    """
    The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information.
    This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
