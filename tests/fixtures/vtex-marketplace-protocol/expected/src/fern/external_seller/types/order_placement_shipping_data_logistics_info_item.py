

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .order_placement_shipping_data_logistics_info_item_delivery_window import (
    OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow,
)


class OrderPlacementShippingDataLogisticsInfoItem(UniversalBaseModel):
    delivery_window: typing_extensions.Annotated[
        typing.Optional[OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow],
        FieldMetadata(alias="deliveryWindow"),
        pydantic.Field(
            alias="deliveryWindow", description="Scheduled delivery window information, in case it applies to the item."
        ),
    ] = None
    """
    Scheduled delivery window information, in case it applies to the item.
    """

    item_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="itemIndex"),
        pydantic.Field(alias="itemIndex", description="Index of the item in the `items` array, starting from 0."),
    ]
    """
    Index of the item in the `items` array, starting from 0.
    """

    lock_ttl: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lockTTL"),
        pydantic.Field(alias="lockTTL", description="Logistics reservation waiting time."),
    ] = None
    """
    Logistics reservation waiting time.
    """

    price: int = pydantic.Field()
    """
    Shipping price for the item. Does not account for the whole order's shipping price.
    """

    selected_sla: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="selectedSla"),
        pydantic.Field(alias="selectedSla", description="Selected shipping option"),
    ]
    """
    Selected shipping option
    """

    shipping_estimate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shippingEstimate"),
        pydantic.Field(alias="shippingEstimate", description="Estimated time until delivery for the item."),
    ] = None
    """
    Estimated time until delivery for the item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
