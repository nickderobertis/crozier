

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_available_delivery_windows import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows,
)
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_delivery_ids_item import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem,
)
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_delivery_window import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow,
)
from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_pickup_store_info import (
    FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo,
)


class FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem(
    UniversalBaseModel
):
    available_delivery_windows: typing_extensions.Annotated[
        typing.Optional[
            FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows
        ],
        FieldMetadata(alias="availableDeliveryWindows"),
        pydantic.Field(
            alias="availableDeliveryWindows",
            description="This object contains information about the delivery window available to the shopper.",
        ),
    ] = None
    """
    This object contains information about the delivery window available to the shopper.
    """

    delivery_channel: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deliveryChannel"),
        pydantic.Field(alias="deliveryChannel", description="Delivery channel."),
    ] = None
    """
    Delivery channel.
    """

    delivery_ids: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem
            ]
        ],
        FieldMetadata(alias="deliveryIds"),
        pydantic.Field(alias="deliveryIds", description="Information on each delivery ID."),
    ] = None
    """
    Information on each delivery ID.
    """

    delivery_window: typing_extensions.Annotated[
        typing.Optional[
            FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow
        ],
        FieldMetadata(alias="deliveryWindow"),
        pydantic.Field(
            alias="deliveryWindow",
            description="In case of scheduled delivery, this object will contain information on the delivery window selected by the shopper.",
        ),
    ] = None
    """
    In case of scheduled delivery, this object will contain information on the delivery window selected by the shopper.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    SLA ID.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="List price in cents."),
    ] = None
    """
    List price in cents.
    """

    lock_ttl: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lockTTL"),
        pydantic.Field(alias="lockTTL", description="Estimate date of delivery."),
    ] = None
    """
    Estimate date of delivery.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    SLA name.
    """

    pickup_distance: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="pickupDistance"),
        pydantic.Field(alias="pickupDistance", description="Pickup point distance."),
    ] = None
    """
    Pickup point distance.
    """

    pickup_point_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pickupPointId"),
        pydantic.Field(alias="pickupPointId", description="Pickup point ID."),
    ] = None
    """
    Pickup point ID.
    """

    pickup_store_info: typing_extensions.Annotated[
        typing.Optional[
            FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo
        ],
        FieldMetadata(alias="pickupStoreInfo"),
        pydantic.Field(alias="pickupStoreInfo", description="Information on the pickup store."),
    ] = None
    """
    Information on the pickup store.
    """

    polygon_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="polygonName"),
        pydantic.Field(alias="polygonName", description="Polygon name."),
    ] = None
    """
    Polygon name.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Price in cents.
    """

    shipping_estimate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shippingEstimate"),
        pydantic.Field(
            alias="shippingEstimate",
            description='Shipping estimate. For instance, "three business days" will be represented as `3bd`.',
        ),
    ] = None
    """
    Shipping estimate. For instance, "three business days" will be represented as `3bd`.
    """

    shipping_estimate_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shippingEstimateDate"),
        pydantic.Field(alias="shippingEstimateDate", description="Shipping estimate date."),
    ] = None
    """
    Shipping estimate date.
    """

    tax: typing.Optional[int] = pydantic.Field(default=None)
    """
    Tax in cents.
    """

    transit_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transitTime"),
        pydantic.Field(
            alias="transitTime",
            description='Transit time. For instance, "three business days" is represented as `3bd`.',
        ),
    ] = None
    """
    Transit time. For instance, "three business days" is represented as `3bd`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
