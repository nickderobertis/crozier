

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem,
)


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem(
    UniversalBaseModel
):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Item ID.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="List price in cents."),
    ] = None
    """
    List price in cents.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Price in cents.
    """

    seller: typing.Optional[str] = pydantic.Field(default=None)
    """
    Seller.
    """

    seller_chain: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="sellerChain"),
        pydantic.Field(
            alias="sellerChain",
            description="Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.",
        ),
    ] = None
    """
    Sellers involved in the chain. The list should contain only one seller, unless it is a [Multilevel Omnichannel Inventory](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) order.
    """

    slas: typing.Optional[
        typing.List[
            FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem
        ]
    ] = pydantic.Field(default=None)
    """
    Information on available SLAs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
