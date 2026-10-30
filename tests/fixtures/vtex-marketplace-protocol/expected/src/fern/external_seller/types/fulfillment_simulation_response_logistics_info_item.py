

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_response_logistics_info_item_delivery_channels_item import (
    FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem,
)
from .fulfillment_simulation_response_logistics_info_item_slas_item import (
    FulfillmentSimulationResponseLogisticsInfoItemSlasItem,
)


class FulfillmentSimulationResponseLogisticsInfoItem(UniversalBaseModel):
    """
    An explanation about the purpose of this instance.
    """

    delivery_channels: typing_extensions.Annotated[
        typing.List[FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem],
        FieldMetadata(alias="deliveryChannels"),
        pydantic.Field(alias="deliveryChannels", description="Array contains the stock balance for each channel."),
    ]
    """
    Array contains the stock balance for each channel.
    """

    item_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="itemIndex"),
        pydantic.Field(
            alias="itemIndex",
            description="Position of this item in the original array, i.e., in the array that came with the request. This index is what identifies which SKU you are referring to for each object inside the logisticsInfo.",
        ),
    ]
    """
    Position of this item in the original array, i.e., in the array that came with the request. This index is what identifies which SKU you are referring to for each object inside the logisticsInfo.
    """

    quantity: int = pydantic.Field()
    """
    Quantity of the item. The seller should send the quantity that was indicated in the request, or the maximum quantity possible.
    """

    ships_to: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="shipsTo"),
        pydantic.Field(alias="shipsTo", description="ISO 3-digit code of the countries to where the SKU is delivered."),
    ]
    """
    ISO 3-digit code of the countries to where the SKU is delivered.
    """

    slas: typing.List[FulfillmentSimulationResponseLogisticsInfoItemSlasItem] = pydantic.Field()
    """
    Contains the available delivery methods.
    """

    stock_balance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="stockBalance"),
        pydantic.Field(alias="stockBalance", description="Stock balance of the SKU."),
    ]
    """
    Stock balance of the SKU.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
