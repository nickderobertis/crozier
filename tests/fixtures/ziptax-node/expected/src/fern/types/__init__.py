



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cart_calculate_response_body import CartCalculateResponseBody
    from .create_merchant_response import CreateMerchantResponse
    from .delete_merchant_credentials_response import DeleteMerchantCredentialsResponse
    from .delete_merchant_response import DeleteMerchantResponse
    from .error_detail import ErrorDetail
    from .error_model import ErrorModel
    from .get_merchant_credentials_response import GetMerchantCredentialsResponse
    from .get_merchant_response import GetMerchantResponse
    from .get_merchant_response_status import GetMerchantResponseStatus
    from .health_components import HealthComponents
    from .health_components_dynamo import HealthComponentsDynamo
    from .health_components_taxdata import HealthComponentsTaxdata
    from .health_response import HealthResponse
    from .item import Item
    from .item_status import ItemStatus
    from .metadata_response import MetadataResponse
    from .metrics_response import MetricsResponse
    from .metrics_v60response import MetricsV60Response
    from .refund_item import RefundItem
    from .self_managed_cart_calculate_response_body import SelfManagedCartCalculateResponseBody
    from .self_managed_cart_item_with_tax_response import SelfManagedCartItemWithTaxResponse
    from .self_managed_cart_response import SelfManagedCartResponse
    from .set_merchant_credentials_response import SetMerchantCredentialsResponse
    from .tax_cloud_address import TaxCloudAddress
    from .tax_cloud_address_country_code import TaxCloudAddressCountryCode
    from .tax_cloud_cart import TaxCloudCart
    from .tax_cloud_cart_item import TaxCloudCartItem
    from .tax_cloud_cart_item_with_tax import TaxCloudCartItemWithTax
    from .tax_cloud_cart_item_with_tax_response import TaxCloudCartItemWithTaxResponse
    from .tax_cloud_cart_response import TaxCloudCartResponse
    from .tax_cloud_cert_list_response import TaxCloudCertListResponse
    from .tax_cloud_cert_response import TaxCloudCertResponse
    from .tax_cloud_currency import TaxCloudCurrency
    from .tax_cloud_currency_currency_code import TaxCloudCurrencyCurrencyCode
    from .tax_cloud_discounts import TaxCloudDiscounts
    from .tax_cloud_exempt_state import TaxCloudExemptState
    from .tax_cloud_exemption import TaxCloudExemption
    from .tax_cloud_line_item_discount import TaxCloudLineItemDiscount
    from .tax_cloud_line_item_discount_type import TaxCloudLineItemDiscountType
    from .tax_cloud_order_level_discount import TaxCloudOrderLevelDiscount
    from .tax_cloud_order_level_discount_type import TaxCloudOrderLevelDiscountType
    from .tax_cloud_order_response import TaxCloudOrderResponse
    from .tax_cloud_order_response_kind import TaxCloudOrderResponseKind
    from .tax_cloud_refund_item_response import TaxCloudRefundItemResponse
    from .tax_cloud_refund_response import TaxCloudRefundResponse
    from .tax_cloud_refund_tax import TaxCloudRefundTax
    from .tax_cloud_tax import TaxCloudTax
    from .tic_data import TicData
    from .tic_entry import TicEntry
    from .tic_recommend_prediction import TicRecommendPrediction
    from .tic_recommend_prediction_status import TicRecommendPredictionStatus
    from .tic_recommend_response import TicRecommendResponse
    from .tic_response import TicResponse
    from .tic_search_response import TicSearchResponse
    from .tic_search_result import TicSearchResult
    from .update_merchant_response import UpdateMerchantResponse
    from .update_struct import UpdateStruct
    from .v60address_components import V60AddressComponents
    from .v60address_detail import V60AddressDetail
    from .v60address_detail_incorporated import V60AddressDetailIncorporated
    from .v60base_rate import V60BaseRate
    from .v60base_rate_jur_type import V60BaseRateJurType
    from .v60display_rate import V60DisplayRate
    from .v60metadata import V60Metadata
    from .v60origin_destination import V60OriginDestination
    from .v60origin_destination_value import V60OriginDestinationValue
    from .v60product_detail import V60ProductDetail
    from .v60rate_rule import V60RateRule
    from .v60response import V60Response
    from .v60response_info import V60ResponseInfo
    from .v60service import V60Service
    from .v60service_taxable import V60ServiceTaxable
    from .v60shipping import V60Shipping
    from .v60shipping_extended import V60ShippingExtended
    from .v60shipping_taxable import V60ShippingTaxable
    from .v60tax_summary import V60TaxSummary
    from .v60tax_summary_tax_type import V60TaxSummaryTaxType
    from .v60taxability_code import V60TaxabilityCode
    from .v60taxability_code_rate_action_code import V60TaxabilityCodeRateActionCode
_dynamic_imports: typing.Dict[str, str] = {
    "CartCalculateResponseBody": ".cart_calculate_response_body",
    "CreateMerchantResponse": ".create_merchant_response",
    "DeleteMerchantCredentialsResponse": ".delete_merchant_credentials_response",
    "DeleteMerchantResponse": ".delete_merchant_response",
    "ErrorDetail": ".error_detail",
    "ErrorModel": ".error_model",
    "GetMerchantCredentialsResponse": ".get_merchant_credentials_response",
    "GetMerchantResponse": ".get_merchant_response",
    "GetMerchantResponseStatus": ".get_merchant_response_status",
    "HealthComponents": ".health_components",
    "HealthComponentsDynamo": ".health_components_dynamo",
    "HealthComponentsTaxdata": ".health_components_taxdata",
    "HealthResponse": ".health_response",
    "Item": ".item",
    "ItemStatus": ".item_status",
    "MetadataResponse": ".metadata_response",
    "MetricsResponse": ".metrics_response",
    "MetricsV60Response": ".metrics_v60response",
    "RefundItem": ".refund_item",
    "SelfManagedCartCalculateResponseBody": ".self_managed_cart_calculate_response_body",
    "SelfManagedCartItemWithTaxResponse": ".self_managed_cart_item_with_tax_response",
    "SelfManagedCartResponse": ".self_managed_cart_response",
    "SetMerchantCredentialsResponse": ".set_merchant_credentials_response",
    "TaxCloudAddress": ".tax_cloud_address",
    "TaxCloudAddressCountryCode": ".tax_cloud_address_country_code",
    "TaxCloudCart": ".tax_cloud_cart",
    "TaxCloudCartItem": ".tax_cloud_cart_item",
    "TaxCloudCartItemWithTax": ".tax_cloud_cart_item_with_tax",
    "TaxCloudCartItemWithTaxResponse": ".tax_cloud_cart_item_with_tax_response",
    "TaxCloudCartResponse": ".tax_cloud_cart_response",
    "TaxCloudCertListResponse": ".tax_cloud_cert_list_response",
    "TaxCloudCertResponse": ".tax_cloud_cert_response",
    "TaxCloudCurrency": ".tax_cloud_currency",
    "TaxCloudCurrencyCurrencyCode": ".tax_cloud_currency_currency_code",
    "TaxCloudDiscounts": ".tax_cloud_discounts",
    "TaxCloudExemptState": ".tax_cloud_exempt_state",
    "TaxCloudExemption": ".tax_cloud_exemption",
    "TaxCloudLineItemDiscount": ".tax_cloud_line_item_discount",
    "TaxCloudLineItemDiscountType": ".tax_cloud_line_item_discount_type",
    "TaxCloudOrderLevelDiscount": ".tax_cloud_order_level_discount",
    "TaxCloudOrderLevelDiscountType": ".tax_cloud_order_level_discount_type",
    "TaxCloudOrderResponse": ".tax_cloud_order_response",
    "TaxCloudOrderResponseKind": ".tax_cloud_order_response_kind",
    "TaxCloudRefundItemResponse": ".tax_cloud_refund_item_response",
    "TaxCloudRefundResponse": ".tax_cloud_refund_response",
    "TaxCloudRefundTax": ".tax_cloud_refund_tax",
    "TaxCloudTax": ".tax_cloud_tax",
    "TicData": ".tic_data",
    "TicEntry": ".tic_entry",
    "TicRecommendPrediction": ".tic_recommend_prediction",
    "TicRecommendPredictionStatus": ".tic_recommend_prediction_status",
    "TicRecommendResponse": ".tic_recommend_response",
    "TicResponse": ".tic_response",
    "TicSearchResponse": ".tic_search_response",
    "TicSearchResult": ".tic_search_result",
    "UpdateMerchantResponse": ".update_merchant_response",
    "UpdateStruct": ".update_struct",
    "V60AddressComponents": ".v60address_components",
    "V60AddressDetail": ".v60address_detail",
    "V60AddressDetailIncorporated": ".v60address_detail_incorporated",
    "V60BaseRate": ".v60base_rate",
    "V60BaseRateJurType": ".v60base_rate_jur_type",
    "V60DisplayRate": ".v60display_rate",
    "V60Metadata": ".v60metadata",
    "V60OriginDestination": ".v60origin_destination",
    "V60OriginDestinationValue": ".v60origin_destination_value",
    "V60ProductDetail": ".v60product_detail",
    "V60RateRule": ".v60rate_rule",
    "V60Response": ".v60response",
    "V60ResponseInfo": ".v60response_info",
    "V60Service": ".v60service",
    "V60ServiceTaxable": ".v60service_taxable",
    "V60Shipping": ".v60shipping",
    "V60ShippingExtended": ".v60shipping_extended",
    "V60ShippingTaxable": ".v60shipping_taxable",
    "V60TaxSummary": ".v60tax_summary",
    "V60TaxSummaryTaxType": ".v60tax_summary_tax_type",
    "V60TaxabilityCode": ".v60taxability_code",
    "V60TaxabilityCodeRateActionCode": ".v60taxability_code_rate_action_code",
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
    "CartCalculateResponseBody",
    "CreateMerchantResponse",
    "DeleteMerchantCredentialsResponse",
    "DeleteMerchantResponse",
    "ErrorDetail",
    "ErrorModel",
    "GetMerchantCredentialsResponse",
    "GetMerchantResponse",
    "GetMerchantResponseStatus",
    "HealthComponents",
    "HealthComponentsDynamo",
    "HealthComponentsTaxdata",
    "HealthResponse",
    "Item",
    "ItemStatus",
    "MetadataResponse",
    "MetricsResponse",
    "MetricsV60Response",
    "RefundItem",
    "SelfManagedCartCalculateResponseBody",
    "SelfManagedCartItemWithTaxResponse",
    "SelfManagedCartResponse",
    "SetMerchantCredentialsResponse",
    "TaxCloudAddress",
    "TaxCloudAddressCountryCode",
    "TaxCloudCart",
    "TaxCloudCartItem",
    "TaxCloudCartItemWithTax",
    "TaxCloudCartItemWithTaxResponse",
    "TaxCloudCartResponse",
    "TaxCloudCertListResponse",
    "TaxCloudCertResponse",
    "TaxCloudCurrency",
    "TaxCloudCurrencyCurrencyCode",
    "TaxCloudDiscounts",
    "TaxCloudExemptState",
    "TaxCloudExemption",
    "TaxCloudLineItemDiscount",
    "TaxCloudLineItemDiscountType",
    "TaxCloudOrderLevelDiscount",
    "TaxCloudOrderLevelDiscountType",
    "TaxCloudOrderResponse",
    "TaxCloudOrderResponseKind",
    "TaxCloudRefundItemResponse",
    "TaxCloudRefundResponse",
    "TaxCloudRefundTax",
    "TaxCloudTax",
    "TicData",
    "TicEntry",
    "TicRecommendPrediction",
    "TicRecommendPredictionStatus",
    "TicRecommendResponse",
    "TicResponse",
    "TicSearchResponse",
    "TicSearchResult",
    "UpdateMerchantResponse",
    "UpdateStruct",
    "V60AddressComponents",
    "V60AddressDetail",
    "V60AddressDetailIncorporated",
    "V60BaseRate",
    "V60BaseRateJurType",
    "V60DisplayRate",
    "V60Metadata",
    "V60OriginDestination",
    "V60OriginDestinationValue",
    "V60ProductDetail",
    "V60RateRule",
    "V60Response",
    "V60ResponseInfo",
    "V60Service",
    "V60ServiceTaxable",
    "V60Shipping",
    "V60ShippingExtended",
    "V60ShippingTaxable",
    "V60TaxSummary",
    "V60TaxSummaryTaxType",
    "V60TaxabilityCode",
    "V60TaxabilityCodeRateActionCode",
]
