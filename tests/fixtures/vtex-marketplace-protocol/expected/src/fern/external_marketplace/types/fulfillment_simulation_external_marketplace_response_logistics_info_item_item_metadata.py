

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata_items_item import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem,
)


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata(UniversalBaseModel):
    """
    Item metadata.
    """

    items: typing.Optional[
        typing.List[FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem]
    ] = pydantic.Field(default=None)
    """
    List of objects containing metadata on each item in the order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
