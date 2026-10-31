



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .fulfillment_simulation_response import FulfillmentSimulationResponse
    from .fulfillment_simulation_response_items_item import FulfillmentSimulationResponseItemsItem
    from .fulfillment_simulation_response_items_item_offerings_item import (
        FulfillmentSimulationResponseItemsItemOfferingsItem,
    )
    from .fulfillment_simulation_response_logistics_info_item import FulfillmentSimulationResponseLogisticsInfoItem
    from .fulfillment_simulation_response_logistics_info_item_delivery_channels_item import (
        FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem,
    )
    from .fulfillment_simulation_response_logistics_info_item_slas_item import (
        FulfillmentSimulationResponseLogisticsInfoItemSlasItem,
    )
    from .fulfillment_simulation_response_logistics_info_item_slas_item_available_delivery_windows_item import (
        FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem,
    )
    from .fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info import (
        FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo,
    )
    from .fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info_address import (
        FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress,
    )
    from .order_placement_client_profile_data import OrderPlacementClientProfileData
    from .order_placement_items_item import OrderPlacementItemsItem
    from .order_placement_items_item_price_tags_item import OrderPlacementItemsItemPriceTagsItem
    from .order_placement_marketing_data import OrderPlacementMarketingData
    from .order_placement_shipping_data import OrderPlacementShippingData
    from .order_placement_shipping_data_address import OrderPlacementShippingDataAddress
    from .order_placement_shipping_data_logistics_info_item import OrderPlacementShippingDataLogisticsInfoItem
    from .order_placement_shipping_data_logistics_info_item_delivery_window import (
        OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow,
    )
    from .send_invoice_request_items_item import SendInvoiceRequestItemsItem
    from .update_tracking_status_request_events_item import UpdateTrackingStatusRequestEventsItem
_dynamic_imports: typing.Dict[str, str] = {
    "FulfillmentSimulationResponse": ".fulfillment_simulation_response",
    "FulfillmentSimulationResponseItemsItem": ".fulfillment_simulation_response_items_item",
    "FulfillmentSimulationResponseItemsItemOfferingsItem": ".fulfillment_simulation_response_items_item_offerings_item",
    "FulfillmentSimulationResponseLogisticsInfoItem": ".fulfillment_simulation_response_logistics_info_item",
    "FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem": ".fulfillment_simulation_response_logistics_info_item_delivery_channels_item",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItem": ".fulfillment_simulation_response_logistics_info_item_slas_item",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem": ".fulfillment_simulation_response_logistics_info_item_slas_item_available_delivery_windows_item",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo": ".fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress": ".fulfillment_simulation_response_logistics_info_item_slas_item_pickup_store_info_address",
    "OrderPlacementClientProfileData": ".order_placement_client_profile_data",
    "OrderPlacementItemsItem": ".order_placement_items_item",
    "OrderPlacementItemsItemPriceTagsItem": ".order_placement_items_item_price_tags_item",
    "OrderPlacementMarketingData": ".order_placement_marketing_data",
    "OrderPlacementShippingData": ".order_placement_shipping_data",
    "OrderPlacementShippingDataAddress": ".order_placement_shipping_data_address",
    "OrderPlacementShippingDataLogisticsInfoItem": ".order_placement_shipping_data_logistics_info_item",
    "OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow": ".order_placement_shipping_data_logistics_info_item_delivery_window",
    "SendInvoiceRequestItemsItem": ".send_invoice_request_items_item",
    "UpdateTrackingStatusRequestEventsItem": ".update_tracking_status_request_events_item",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "FulfillmentSimulationResponse",
    "FulfillmentSimulationResponseItemsItem",
    "FulfillmentSimulationResponseItemsItemOfferingsItem",
    "FulfillmentSimulationResponseLogisticsInfoItem",
    "FulfillmentSimulationResponseLogisticsInfoItemDeliveryChannelsItem",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItem",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfo",
    "FulfillmentSimulationResponseLogisticsInfoItemSlasItemPickupStoreInfoAddress",
    "OrderPlacementClientProfileData",
    "OrderPlacementItemsItem",
    "OrderPlacementItemsItemPriceTagsItem",
    "OrderPlacementMarketingData",
    "OrderPlacementShippingData",
    "OrderPlacementShippingDataAddress",
    "OrderPlacementShippingDataLogisticsInfoItem",
    "OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow",
    "SendInvoiceRequestItemsItem",
    "UpdateTrackingStatusRequestEventsItem",
]
