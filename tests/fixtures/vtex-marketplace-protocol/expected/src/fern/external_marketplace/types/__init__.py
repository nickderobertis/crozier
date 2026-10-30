



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .fulfillment_simulation_external_marketplace_request_client_profile_data import (
        FulfillmentSimulationExternalMarketplaceRequestClientProfileData,
    )
    from .fulfillment_simulation_external_marketplace_request_items_item import (
        FulfillmentSimulationExternalMarketplaceRequestItemsItem,
    )
    from .fulfillment_simulation_external_marketplace_request_marketing_data import (
        FulfillmentSimulationExternalMarketplaceRequestMarketingData,
    )
    from .fulfillment_simulation_external_marketplace_response import FulfillmentSimulationExternalMarketplaceResponse
    from .fulfillment_simulation_external_marketplace_response_items_item import (
        FulfillmentSimulationExternalMarketplaceResponseItemsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_items_item_price_definition import (
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition,
    )
    from .fulfillment_simulation_external_marketplace_response_items_item_price_definition_selling_prices_item import (
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem,
    )
    from .fulfillment_simulation_external_marketplace_response_items_item_price_tags_item import (
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_delivery_channels_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemDeliveryChannelsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata_items_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem,
    )
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
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_available_delivery_windows import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemAvailableDeliveryWindows,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_delivery_ids_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryIdsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_delivery_window import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryWindow,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_pickup_store_info import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemPickupStoreInfo,
    )
    from .fulfillment_simulation_external_marketplace_response_logistics_info_item_totals_item import (
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_payment_data import (
        FulfillmentSimulationExternalMarketplaceResponsePaymentData,
    )
    from .fulfillment_simulation_external_marketplace_response_payment_data_payment_systems_item import (
        FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem,
    )
    from .fulfillment_simulation_external_marketplace_response_rates_and_benefits_data import (
        FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData,
    )
    from .place_fulfillment_order_request_client_profile_data import PlaceFulfillmentOrderRequestClientProfileData
    from .place_fulfillment_order_request_items_item import PlaceFulfillmentOrderRequestItemsItem
    from .place_fulfillment_order_request_items_item_bundle_items_item import (
        PlaceFulfillmentOrderRequestItemsItemBundleItemsItem,
    )
    from .place_fulfillment_order_request_items_item_item_attachment import (
        PlaceFulfillmentOrderRequestItemsItemItemAttachment,
    )
    from .place_fulfillment_order_request_items_item_price_tags_item import (
        PlaceFulfillmentOrderRequestItemsItemPriceTagsItem,
    )
    from .place_fulfillment_order_request_marketing_data import PlaceFulfillmentOrderRequestMarketingData
    from .place_fulfillment_order_request_shipping_data import PlaceFulfillmentOrderRequestShippingData
    from .place_fulfillment_order_request_shipping_data_address import PlaceFulfillmentOrderRequestShippingDataAddress
    from .place_fulfillment_order_request_shipping_data_logistics_info_item import (
        PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem,
    )
    from .place_fulfillment_order_request_shipping_data_logistics_info_item_delivery_window import (
        PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow,
    )
    from .send_category_mapping_to_vtex_mapper_categories_item import SendCategoryMappingToVtexMapperCategoriesItem
    from .send_category_mapping_to_vtex_mapper_categories_item_children_item import (
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItem,
    )
    from .send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item import (
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem,
    )
    from .send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item_attribute_values_item import (
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "FulfillmentSimulationExternalMarketplaceRequestClientProfileData": ".fulfillment_simulation_external_marketplace_request_client_profile_data",
    "FulfillmentSimulationExternalMarketplaceRequestItemsItem": ".fulfillment_simulation_external_marketplace_request_items_item",
    "FulfillmentSimulationExternalMarketplaceRequestMarketingData": ".fulfillment_simulation_external_marketplace_request_marketing_data",
    "FulfillmentSimulationExternalMarketplaceResponse": ".fulfillment_simulation_external_marketplace_response",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItem": ".fulfillment_simulation_external_marketplace_response_items_item",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition": ".fulfillment_simulation_external_marketplace_response_items_item_price_definition",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem": ".fulfillment_simulation_external_marketplace_response_items_item_price_definition_selling_prices_item",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem": ".fulfillment_simulation_external_marketplace_response_items_item_price_tags_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemDeliveryChannelsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_delivery_channels_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_item_metadata_items_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_available_delivery_windows",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_delivery_ids_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_delivery_window",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_purchase_conditions_item_purchase_conditions_item_slas_item_pickup_store_info",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemAvailableDeliveryWindows": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_available_delivery_windows",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryIdsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_delivery_ids_item",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryWindow": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_delivery_window",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemPickupStoreInfo": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_slas_item_pickup_store_info",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem": ".fulfillment_simulation_external_marketplace_response_logistics_info_item_totals_item",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentData": ".fulfillment_simulation_external_marketplace_response_payment_data",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem": ".fulfillment_simulation_external_marketplace_response_payment_data_payment_systems_item",
    "FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData": ".fulfillment_simulation_external_marketplace_response_rates_and_benefits_data",
    "PlaceFulfillmentOrderRequestClientProfileData": ".place_fulfillment_order_request_client_profile_data",
    "PlaceFulfillmentOrderRequestItemsItem": ".place_fulfillment_order_request_items_item",
    "PlaceFulfillmentOrderRequestItemsItemBundleItemsItem": ".place_fulfillment_order_request_items_item_bundle_items_item",
    "PlaceFulfillmentOrderRequestItemsItemItemAttachment": ".place_fulfillment_order_request_items_item_item_attachment",
    "PlaceFulfillmentOrderRequestItemsItemPriceTagsItem": ".place_fulfillment_order_request_items_item_price_tags_item",
    "PlaceFulfillmentOrderRequestMarketingData": ".place_fulfillment_order_request_marketing_data",
    "PlaceFulfillmentOrderRequestShippingData": ".place_fulfillment_order_request_shipping_data",
    "PlaceFulfillmentOrderRequestShippingDataAddress": ".place_fulfillment_order_request_shipping_data_address",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem": ".place_fulfillment_order_request_shipping_data_logistics_info_item",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow": ".place_fulfillment_order_request_shipping_data_logistics_info_item_delivery_window",
    "SendCategoryMappingToVtexMapperCategoriesItem": ".send_category_mapping_to_vtex_mapper_categories_item",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItem": ".send_category_mapping_to_vtex_mapper_categories_item_children_item",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem": ".send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem": ".send_category_mapping_to_vtex_mapper_categories_item_children_item_specifications_item_attribute_values_item",
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
    "FulfillmentSimulationExternalMarketplaceRequestClientProfileData",
    "FulfillmentSimulationExternalMarketplaceRequestItemsItem",
    "FulfillmentSimulationExternalMarketplaceRequestMarketingData",
    "FulfillmentSimulationExternalMarketplaceResponse",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItem",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemDeliveryChannelsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemAvailableDeliveryWindows",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryIdsItem",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryWindow",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemPickupStoreInfo",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentData",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem",
    "FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData",
    "PlaceFulfillmentOrderRequestClientProfileData",
    "PlaceFulfillmentOrderRequestItemsItem",
    "PlaceFulfillmentOrderRequestItemsItemBundleItemsItem",
    "PlaceFulfillmentOrderRequestItemsItemItemAttachment",
    "PlaceFulfillmentOrderRequestItemsItemPriceTagsItem",
    "PlaceFulfillmentOrderRequestMarketingData",
    "PlaceFulfillmentOrderRequestShippingData",
    "PlaceFulfillmentOrderRequestShippingDataAddress",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow",
    "SendCategoryMappingToVtexMapperCategoriesItem",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItem",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem",
]
