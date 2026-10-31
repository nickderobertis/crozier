

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_items_item_price_definition import (
    FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition,
)
from .fulfillment_simulation_external_marketplace_response_items_item_price_tags_item import (
    FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem,
)


class FulfillmentSimulationExternalMarketplaceResponseItemsItem(UniversalBaseModel):
    availability: typing.Optional[str] = pydantic.Field(default=None)
    """
    Availability.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the item.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="List price in cents."),
    ] = None
    """
    List price in cents.
    """

    measurement_unit: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="measurementUnit"),
        pydantic.Field(alias="measurementUnit", description="Measurement unit."),
    ] = None
    """
    Measurement unit.
    """

    offerings: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Array containing offering information.
    """

    parent_assembly_binding: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentAssemblyBinding"),
        pydantic.Field(alias="parentAssemblyBinding", description="Parent assembly binding."),
    ] = None
    """
    Parent assembly binding.
    """

    parent_item_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="parentItemIndex"),
        pydantic.Field(alias="parentItemIndex", description="Parent item index."),
    ] = None
    """
    Parent item index.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Price in cents.
    """

    price_definition: typing_extensions.Annotated[
        typing.Optional[FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition],
        FieldMetadata(alias="priceDefinition"),
        pydantic.Field(alias="priceDefinition", description="Price information for all units of a specific item."),
    ] = None
    """
    Price information for all units of a specific item.
    """

    price_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem]],
        FieldMetadata(alias="priceTags"),
        pydantic.Field(
            alias="priceTags",
            description="Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.",
        ),
    ] = None
    """
    Array of price tags, each of which, modifies the price in some way, like discounts or rates that apply to the item in the context of the order.
    """

    price_valid_until: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priceValidUntil"),
        pydantic.Field(alias="priceValidUntil", description="Price expiration date and time."),
    ] = None
    """
    Price expiration date and time.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The quantity of the item the cart.
    """

    request_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="requestIndex"),
        pydantic.Field(alias="requestIndex", description="Request index information."),
    ] = None
    """
    Request index information.
    """

    reward_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardValue"),
        pydantic.Field(alias="rewardValue", description="Reward value in cents."),
    ] = None
    """
    Reward value in cents.
    """

    seller: typing.Optional[str] = pydantic.Field(default=None)
    """
    The seller responsible for the SKU.
    """

    seller_chain: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sellerChain"),
        pydantic.Field(
            alias="sellerChain",
            description="Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.",
        ),
    ] = None
    """
    Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.
    """

    selling_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sellingPrice"),
        pydantic.Field(
            alias="sellingPrice",
            description="Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead.",
        ),
    ] = None
    """
    Selling price in cents. Note that this field may be subject to rounding discrepancies. We recommend retrieving data from the `priceDefinition` data structure instead.
    """

    tax: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tax value in cents.
    """

    unit_multiplier: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unitMultiplier"),
        pydantic.Field(alias="unitMultiplier", description="Unit multiplier."),
    ] = None
    """
    Unit multiplier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
