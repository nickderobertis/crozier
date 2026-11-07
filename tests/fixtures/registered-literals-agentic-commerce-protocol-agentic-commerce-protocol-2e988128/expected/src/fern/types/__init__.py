



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .affiliate_attribution import AffiliateAttribution
    from .affiliate_attribution_metadata import AffiliateAttributionMetadata
    from .affiliate_attribution_metadata_value import AffiliateAttributionMetadataValue
    from .affiliate_attribution_source import AffiliateAttributionSource
    from .affiliate_attribution_source_type import AffiliateAttributionSourceType
    from .affiliate_attribution_touchpoint import AffiliateAttributionTouchpoint
    from .authentication_metadata import AuthenticationMetadata
    from .authentication_metadata_acquirer_details import AuthenticationMetadataAcquirerDetails
    from .authentication_metadata_channel import AuthenticationMetadataChannel
    from .authentication_metadata_channel_browser import AuthenticationMetadataChannelBrowser
    from .authentication_metadata_channel_type import AuthenticationMetadataChannelType
    from .authentication_metadata_directory_server import AuthenticationMetadataDirectoryServer
    from .authentication_metadata_flow_preference import AuthenticationMetadataFlowPreference
    from .authentication_metadata_flow_preference_challenge import AuthenticationMetadataFlowPreferenceChallenge
    from .authentication_metadata_flow_preference_challenge_type import (
        AuthenticationMetadataFlowPreferenceChallengeType,
    )
    from .authentication_metadata_flow_preference_type import AuthenticationMetadataFlowPreferenceType
    from .authentication_result import AuthenticationResult
    from .authentication_result_outcome import AuthenticationResultOutcome
    from .authentication_result_outcome_details import AuthenticationResultOutcomeDetails
    from .authentication_result_outcome_details_electronic_commerce_indicator import (
        AuthenticationResultOutcomeDetailsElectronicCommerceIndicator,
    )
    from .buyer import Buyer
    from .checkout_session import CheckoutSession
    from .checkout_session_base import CheckoutSessionBase
    from .checkout_session_base_fulfillment_options_item import (
        CheckoutSessionBaseFulfillmentOptionsItem,
        CheckoutSessionBaseFulfillmentOptionsItem_Digital,
        CheckoutSessionBaseFulfillmentOptionsItem_Shipping,
    )
    from .checkout_session_base_messages_item import (
        CheckoutSessionBaseMessagesItem,
        CheckoutSessionBaseMessagesItem_Error,
        CheckoutSessionBaseMessagesItem_Info,
    )
    from .checkout_session_base_status import CheckoutSessionBaseStatus
    from .checkout_session_with_order import CheckoutSessionWithOrder
    from .custom_attribute import CustomAttribute
    from .disclosure import Disclosure
    from .disclosure_content_type import DisclosureContentType
    from .disclosure_type import DisclosureType
    from .error import Error
    from .error_type import ErrorType
    from .fulfillment_details import FulfillmentDetails
    from .fulfillment_option_digital import FulfillmentOptionDigital
    from .fulfillment_option_shipping import FulfillmentOptionShipping
    from .intent_trace import IntentTrace
    from .intent_trace_metadata_value import IntentTraceMetadataValue
    from .intent_trace_reason_code import IntentTraceReasonCode
    from .item import Item
    from .line_item import LineItem
    from .link import Link
    from .link_type import LinkType
    from .marketplace_seller_details import MarketplaceSellerDetails
    from .message_error import MessageError
    from .message_error_code import MessageErrorCode
    from .message_error_content_type import MessageErrorContentType
    from .message_info import MessageInfo
    from .message_info_content_type import MessageInfoContentType
    from .order import Order
    from .payment_data import PaymentData
    from .payment_data_provider import PaymentDataProvider
    from .payment_method import PaymentMethod
    from .payment_method_supported_card_networks_item import PaymentMethodSupportedCardNetworksItem
    from .payment_method_type import PaymentMethodType
    from .payment_provider import PaymentProvider
    from .payment_provider_provider import PaymentProviderProvider
    from .selected_digital_fulfillment_option import SelectedDigitalFulfillmentOption
    from .selected_fulfillment_option import SelectedFulfillmentOption
    from .selected_fulfillment_option_one import SelectedFulfillmentOptionOne
    from .selected_fulfillment_option_one_type import SelectedFulfillmentOptionOneType
    from .selected_fulfillment_option_type import SelectedFulfillmentOptionType
    from .selected_fulfillment_option_zero import SelectedFulfillmentOptionZero
    from .selected_fulfillment_option_zero_type import SelectedFulfillmentOptionZeroType
    from .selected_shipping_fulfillment_option import SelectedShippingFulfillmentOption
    from .total import Total
    from .total_type import TotalType
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "AffiliateAttribution": ".affiliate_attribution",
    "AffiliateAttributionMetadata": ".affiliate_attribution_metadata",
    "AffiliateAttributionMetadataValue": ".affiliate_attribution_metadata_value",
    "AffiliateAttributionSource": ".affiliate_attribution_source",
    "AffiliateAttributionSourceType": ".affiliate_attribution_source_type",
    "AffiliateAttributionTouchpoint": ".affiliate_attribution_touchpoint",
    "AuthenticationMetadata": ".authentication_metadata",
    "AuthenticationMetadataAcquirerDetails": ".authentication_metadata_acquirer_details",
    "AuthenticationMetadataChannel": ".authentication_metadata_channel",
    "AuthenticationMetadataChannelBrowser": ".authentication_metadata_channel_browser",
    "AuthenticationMetadataChannelType": ".authentication_metadata_channel_type",
    "AuthenticationMetadataDirectoryServer": ".authentication_metadata_directory_server",
    "AuthenticationMetadataFlowPreference": ".authentication_metadata_flow_preference",
    "AuthenticationMetadataFlowPreferenceChallenge": ".authentication_metadata_flow_preference_challenge",
    "AuthenticationMetadataFlowPreferenceChallengeType": ".authentication_metadata_flow_preference_challenge_type",
    "AuthenticationMetadataFlowPreferenceType": ".authentication_metadata_flow_preference_type",
    "AuthenticationResult": ".authentication_result",
    "AuthenticationResultOutcome": ".authentication_result_outcome",
    "AuthenticationResultOutcomeDetails": ".authentication_result_outcome_details",
    "AuthenticationResultOutcomeDetailsElectronicCommerceIndicator": ".authentication_result_outcome_details_electronic_commerce_indicator",
    "Buyer": ".buyer",
    "CheckoutSession": ".checkout_session",
    "CheckoutSessionBase": ".checkout_session_base",
    "CheckoutSessionBaseFulfillmentOptionsItem": ".checkout_session_base_fulfillment_options_item",
    "CheckoutSessionBaseFulfillmentOptionsItem_Digital": ".checkout_session_base_fulfillment_options_item",
    "CheckoutSessionBaseFulfillmentOptionsItem_Shipping": ".checkout_session_base_fulfillment_options_item",
    "CheckoutSessionBaseMessagesItem": ".checkout_session_base_messages_item",
    "CheckoutSessionBaseMessagesItem_Error": ".checkout_session_base_messages_item",
    "CheckoutSessionBaseMessagesItem_Info": ".checkout_session_base_messages_item",
    "CheckoutSessionBaseStatus": ".checkout_session_base_status",
    "CheckoutSessionWithOrder": ".checkout_session_with_order",
    "CustomAttribute": ".custom_attribute",
    "Disclosure": ".disclosure",
    "DisclosureContentType": ".disclosure_content_type",
    "DisclosureType": ".disclosure_type",
    "Error": ".error",
    "ErrorType": ".error_type",
    "FulfillmentDetails": ".fulfillment_details",
    "FulfillmentOptionDigital": ".fulfillment_option_digital",
    "FulfillmentOptionShipping": ".fulfillment_option_shipping",
    "IntentTrace": ".intent_trace",
    "IntentTraceMetadataValue": ".intent_trace_metadata_value",
    "IntentTraceReasonCode": ".intent_trace_reason_code",
    "Item": ".item",
    "LineItem": ".line_item",
    "Link": ".link",
    "LinkType": ".link_type",
    "MarketplaceSellerDetails": ".marketplace_seller_details",
    "MessageError": ".message_error",
    "MessageErrorCode": ".message_error_code",
    "MessageErrorContentType": ".message_error_content_type",
    "MessageInfo": ".message_info",
    "MessageInfoContentType": ".message_info_content_type",
    "Order": ".order",
    "PaymentData": ".payment_data",
    "PaymentDataProvider": ".payment_data_provider",
    "PaymentMethod": ".payment_method",
    "PaymentMethodSupportedCardNetworksItem": ".payment_method_supported_card_networks_item",
    "PaymentMethodType": ".payment_method_type",
    "PaymentProvider": ".payment_provider",
    "PaymentProviderProvider": ".payment_provider_provider",
    "SelectedDigitalFulfillmentOption": ".selected_digital_fulfillment_option",
    "SelectedFulfillmentOption": ".selected_fulfillment_option",
    "SelectedFulfillmentOptionOne": ".selected_fulfillment_option_one",
    "SelectedFulfillmentOptionOneType": ".selected_fulfillment_option_one_type",
    "SelectedFulfillmentOptionType": ".selected_fulfillment_option_type",
    "SelectedFulfillmentOptionZero": ".selected_fulfillment_option_zero",
    "SelectedFulfillmentOptionZeroType": ".selected_fulfillment_option_zero_type",
    "SelectedShippingFulfillmentOption": ".selected_shipping_fulfillment_option",
    "Total": ".total",
    "TotalType": ".total_type",
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
    "Address",
    "AffiliateAttribution",
    "AffiliateAttributionMetadata",
    "AffiliateAttributionMetadataValue",
    "AffiliateAttributionSource",
    "AffiliateAttributionSourceType",
    "AffiliateAttributionTouchpoint",
    "AuthenticationMetadata",
    "AuthenticationMetadataAcquirerDetails",
    "AuthenticationMetadataChannel",
    "AuthenticationMetadataChannelBrowser",
    "AuthenticationMetadataChannelType",
    "AuthenticationMetadataDirectoryServer",
    "AuthenticationMetadataFlowPreference",
    "AuthenticationMetadataFlowPreferenceChallenge",
    "AuthenticationMetadataFlowPreferenceChallengeType",
    "AuthenticationMetadataFlowPreferenceType",
    "AuthenticationResult",
    "AuthenticationResultOutcome",
    "AuthenticationResultOutcomeDetails",
    "AuthenticationResultOutcomeDetailsElectronicCommerceIndicator",
    "Buyer",
    "CheckoutSession",
    "CheckoutSessionBase",
    "CheckoutSessionBaseFulfillmentOptionsItem",
    "CheckoutSessionBaseFulfillmentOptionsItem_Digital",
    "CheckoutSessionBaseFulfillmentOptionsItem_Shipping",
    "CheckoutSessionBaseMessagesItem",
    "CheckoutSessionBaseMessagesItem_Error",
    "CheckoutSessionBaseMessagesItem_Info",
    "CheckoutSessionBaseStatus",
    "CheckoutSessionWithOrder",
    "CustomAttribute",
    "Disclosure",
    "DisclosureContentType",
    "DisclosureType",
    "Error",
    "ErrorType",
    "FulfillmentDetails",
    "FulfillmentOptionDigital",
    "FulfillmentOptionShipping",
    "IntentTrace",
    "IntentTraceMetadataValue",
    "IntentTraceReasonCode",
    "Item",
    "LineItem",
    "Link",
    "LinkType",
    "MarketplaceSellerDetails",
    "MessageError",
    "MessageErrorCode",
    "MessageErrorContentType",
    "MessageInfo",
    "MessageInfoContentType",
    "Order",
    "PaymentData",
    "PaymentDataProvider",
    "PaymentMethod",
    "PaymentMethodSupportedCardNetworksItem",
    "PaymentMethodType",
    "PaymentProvider",
    "PaymentProviderProvider",
    "SelectedDigitalFulfillmentOption",
    "SelectedFulfillmentOption",
    "SelectedFulfillmentOptionOne",
    "SelectedFulfillmentOptionOneType",
    "SelectedFulfillmentOptionType",
    "SelectedFulfillmentOptionZero",
    "SelectedFulfillmentOptionZeroType",
    "SelectedShippingFulfillmentOption",
    "Total",
    "TotalType",
]
