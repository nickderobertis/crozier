



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        FulfillmentSimulationExternalMarketplaceRequestClientProfileData,
        FulfillmentSimulationExternalMarketplaceRequestItemsItem,
        FulfillmentSimulationExternalMarketplaceRequestMarketingData,
        FulfillmentSimulationExternalMarketplaceResponse,
        FulfillmentSimulationExternalMarketplaceResponseItemsItem,
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition,
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem,
        FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemDeliveryChannelsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemAvailableDeliveryWindows,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryIdsItem,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryWindow,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemPickupStoreInfo,
        FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem,
        FulfillmentSimulationExternalMarketplaceResponsePaymentData,
        FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem,
        FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData,
        PlaceFulfillmentOrderRequestClientProfileData,
        PlaceFulfillmentOrderRequestItemsItem,
        PlaceFulfillmentOrderRequestItemsItemBundleItemsItem,
        PlaceFulfillmentOrderRequestItemsItemItemAttachment,
        PlaceFulfillmentOrderRequestItemsItemPriceTagsItem,
        PlaceFulfillmentOrderRequestMarketingData,
        PlaceFulfillmentOrderRequestShippingData,
        PlaceFulfillmentOrderRequestShippingDataAddress,
        PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem,
        PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow,
        SendCategoryMappingToVtexMapperCategoriesItem,
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItem,
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem,
        SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "FulfillmentSimulationExternalMarketplaceRequestClientProfileData": ".types",
    "FulfillmentSimulationExternalMarketplaceRequestItemsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceRequestMarketingData": ".types",
    "FulfillmentSimulationExternalMarketplaceResponse": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinition": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceDefinitionSellingPricesItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseItemsItemPriceTagsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemDeliveryChannelsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadata": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemItemMetadataItemsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditions": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemAvailableDeliveryWindows": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryIdsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemDeliveryWindow": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemPurchaseConditionsItemPurchaseConditionsItemSlasItemPickupStoreInfo": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemAvailableDeliveryWindows": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryIdsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemDeliveryWindow": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemSlasItemPickupStoreInfo": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseLogisticsInfoItemTotalsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentData": ".types",
    "FulfillmentSimulationExternalMarketplaceResponsePaymentDataPaymentSystemsItem": ".types",
    "FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData": ".types",
    "PlaceFulfillmentOrderRequestClientProfileData": ".types",
    "PlaceFulfillmentOrderRequestItemsItem": ".types",
    "PlaceFulfillmentOrderRequestItemsItemBundleItemsItem": ".types",
    "PlaceFulfillmentOrderRequestItemsItemItemAttachment": ".types",
    "PlaceFulfillmentOrderRequestItemsItemPriceTagsItem": ".types",
    "PlaceFulfillmentOrderRequestMarketingData": ".types",
    "PlaceFulfillmentOrderRequestShippingData": ".types",
    "PlaceFulfillmentOrderRequestShippingDataAddress": ".types",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItem": ".types",
    "PlaceFulfillmentOrderRequestShippingDataLogisticsInfoItemDeliveryWindow": ".types",
    "SendCategoryMappingToVtexMapperCategoriesItem": ".types",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItem": ".types",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItem": ".types",
    "SendCategoryMappingToVtexMapperCategoriesItemChildrenItemSpecificationsItemAttributeValuesItem": ".types",
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
