

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_items_item_price_definition_selling_prices_item import (
    FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem,
)


class FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition(UniversalBaseModel):
    """
    Price information for all units of a specific item.
    """

    calculated_selling_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="calculatedSellingPrice"),
        pydantic.Field(alias="calculatedSellingPrice", description="Item's calculated unitary selling price in cents."),
    ] = None
    """
    Item's calculated unitary selling price in cents.
    """

    selling_prices: typing_extensions.Annotated[
        typing.Optional[
            typing.List[FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem]
        ],
        FieldMetadata(alias="sellingPrices"),
        pydantic.Field(
            alias="sellingPrices",
            description="Array of objects, each containing value (in cents) and quantity for the different rounding instances that can be combined to form the correctly rounded total.",
        ),
    ] = None
    """
    Array of objects, each containing value (in cents) and quantity for the different rounding instances that can be combined to form the correctly rounded total.
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total value for all units of the item in cents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
