

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_response_logistics_info_item_slas_item_available_delivery_windows_item import (
    FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem,
)
from .fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info import (
    FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo,
)


class FulfillmentSimulationResponseLogisticsInfoItemSlasItem(UniversalBaseModel):
    """
    Object with delivery methods information.
    """

    available_delivery_windows: typing_extensions.Annotated[
        typing.List[FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem],
        FieldMetadata(alias="availableDeliveryWindows"),
        pydantic.Field(
            alias="availableDeliveryWindows", description="Contains the delivery windows available for the SLA."
        ),
    ]
    """
    Contains the delivery windows available for the SLA.
    """

    delivery_channel: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="deliveryChannel"),
        pydantic.Field(
            alias="deliveryChannel",
            description="Type of delivery channel. The values that are possible are: `pickup-in-point` for pickup point and `delivery` for regular delivery.",
        ),
    ]
    """
    Type of delivery channel. The values that are possible are: `pickup-in-point` for pickup point and `delivery` for regular delivery.
    """

    id: str = pydantic.Field()
    """
    Identifier of the delivery method.
    """

    name: str = pydantic.Field()
    """
    Name of the delivery method.
    """

    pickup_store_info: typing_extensions.Annotated[
        typing.Optional[FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo],
        FieldMetadata(alias="pickupStoreInfo"),
        pydantic.Field(
            alias="pickupStoreInfo",
            description="Contains the data about the pickup point. If you don’t want to send this, use the value `null`.",
        ),
    ] = None
    """
    Contains the data about the pickup point. If you don’t want to send this, use the value `null`.
    """

    price: int = pydantic.Field()
    """
    Delivery price. The two last digits are the cents.
    """

    shipping_estimate: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="shippingEstimate"),
        pydantic.Field(
            alias="shippingEstimate",
            description="Time estimated for the delivery. Possible suffixes are `bd` for *business day* , `h` for *hours*, and `m` for *minutes*.",
        ),
    ]
    """
    Time estimated for the delivery. Possible suffixes are `bd` for *business day* , `h` for *hours*, and `m` for *minutes*.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
