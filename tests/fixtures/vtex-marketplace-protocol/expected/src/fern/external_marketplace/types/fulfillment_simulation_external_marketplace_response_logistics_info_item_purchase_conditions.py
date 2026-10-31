

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem,
)


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions(UniversalBaseModel):
    """
    Purchase conditions information.
    """

    item_purchase_conditions: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem
            ]
        ],
        FieldMetadata(alias="itemPurchaseConditions"),
        pydantic.Field(
            alias="itemPurchaseConditions",
            description="List of objects containing purchase condition information on each item in the order.",
        ),
    ] = None
    """
    List of objects containing purchase condition information on each item in the order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
