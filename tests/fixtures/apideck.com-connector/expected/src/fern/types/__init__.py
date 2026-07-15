



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api import Api
    from .api_resource import ApiResource
    from .api_resource_coverage import ApiResourceCoverage
    from .api_resource_coverage_coverage_item import ApiResourceCoverageCoverageItem
    from .api_resource_linked_resources_item import ApiResourceLinkedResourcesItem
    from .api_resources_item import ApiResourcesItem
    from .api_status import ApiStatus
    from .api_type import ApiType
    from .apis_filter import ApisFilter
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .connector import Connector
    from .connector_auth_type import ConnectorAuthType
    from .connector_doc import ConnectorDoc
    from .connector_doc_audience import ConnectorDocAudience
    from .connector_doc_format import ConnectorDocFormat
    from .connector_event import ConnectorEvent
    from .connector_event_event_source import ConnectorEventEventSource
    from .connector_oauth_credentials_source import ConnectorOauthCredentialsSource
    from .connector_oauth_grant_type import ConnectorOauthGrantType
    from .connector_oauth_scopes_item import ConnectorOauthScopesItem
    from .connector_resource import ConnectorResource
    from .connector_setting import ConnectorSetting
    from .connector_setting_type import ConnectorSettingType
    from .connector_status import ConnectorStatus
    from .connector_tls_support import ConnectorTlsSupport
    from .connector_unified_apis_item import ConnectorUnifiedApisItem
    from .connector_unified_apis_item_oauth_scopes_item import ConnectorUnifiedApisItemOauthScopesItem
    from .connectors_filter import ConnectorsFilter
    from .get_api_resource_coverage_response import GetApiResourceCoverageResponse
    from .get_api_resource_response import GetApiResourceResponse
    from .get_api_response import GetApiResponse
    from .get_apis_response import GetApisResponse
    from .get_connector_resource_response import GetConnectorResourceResponse
    from .get_connector_response import GetConnectorResponse
    from .get_connectors_response import GetConnectorsResponse
    from .id import Id
    from .linked_connector_resource import LinkedConnectorResource
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .pagination_coverage import PaginationCoverage
    from .pagination_coverage_mode import PaginationCoverageMode
    from .payment_required_response import PaymentRequiredResponse
    from .resource_id import ResourceId
    from .resource_status import ResourceStatus
    from .supported_property import SupportedProperty
    from .supported_property_child_properties_item import SupportedPropertyChildPropertiesItem
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_api_id import UnifiedApiId
    from .unified_property import UnifiedProperty
    from .webhook_support import WebhookSupport
    from .webhook_support_managed_via import WebhookSupportManagedVia
    from .webhook_support_mode import WebhookSupportMode
    from .webhook_support_subscription_level import WebhookSupportSubscriptionLevel
    from .webhook_support_virtual_webhooks import WebhookSupportVirtualWebhooks
    from .webhook_support_virtual_webhooks_request_rate import WebhookSupportVirtualWebhooksRequestRate
    from .webhook_support_virtual_webhooks_request_rate_unit import WebhookSupportVirtualWebhooksRequestRateUnit
_dynamic_imports: typing.Dict[str, str] = {
    "Api": ".api",
    "ApiResource": ".api_resource",
    "ApiResourceCoverage": ".api_resource_coverage",
    "ApiResourceCoverageCoverageItem": ".api_resource_coverage_coverage_item",
    "ApiResourceLinkedResourcesItem": ".api_resource_linked_resources_item",
    "ApiResourcesItem": ".api_resources_item",
    "ApiStatus": ".api_status",
    "ApiType": ".api_type",
    "ApisFilter": ".apis_filter",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "Connector": ".connector",
    "ConnectorAuthType": ".connector_auth_type",
    "ConnectorDoc": ".connector_doc",
    "ConnectorDocAudience": ".connector_doc_audience",
    "ConnectorDocFormat": ".connector_doc_format",
    "ConnectorEvent": ".connector_event",
    "ConnectorEventEventSource": ".connector_event_event_source",
    "ConnectorOauthCredentialsSource": ".connector_oauth_credentials_source",
    "ConnectorOauthGrantType": ".connector_oauth_grant_type",
    "ConnectorOauthScopesItem": ".connector_oauth_scopes_item",
    "ConnectorResource": ".connector_resource",
    "ConnectorSetting": ".connector_setting",
    "ConnectorSettingType": ".connector_setting_type",
    "ConnectorStatus": ".connector_status",
    "ConnectorTlsSupport": ".connector_tls_support",
    "ConnectorUnifiedApisItem": ".connector_unified_apis_item",
    "ConnectorUnifiedApisItemOauthScopesItem": ".connector_unified_apis_item_oauth_scopes_item",
    "ConnectorsFilter": ".connectors_filter",
    "GetApiResourceCoverageResponse": ".get_api_resource_coverage_response",
    "GetApiResourceResponse": ".get_api_resource_response",
    "GetApiResponse": ".get_api_response",
    "GetApisResponse": ".get_apis_response",
    "GetConnectorResourceResponse": ".get_connector_resource_response",
    "GetConnectorResponse": ".get_connector_response",
    "GetConnectorsResponse": ".get_connectors_response",
    "Id": ".id",
    "LinkedConnectorResource": ".linked_connector_resource",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "PaginationCoverage": ".pagination_coverage",
    "PaginationCoverageMode": ".pagination_coverage_mode",
    "PaymentRequiredResponse": ".payment_required_response",
    "ResourceId": ".resource_id",
    "ResourceStatus": ".resource_status",
    "SupportedProperty": ".supported_property",
    "SupportedPropertyChildPropertiesItem": ".supported_property_child_properties_item",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedApiId": ".unified_api_id",
    "UnifiedProperty": ".unified_property",
    "WebhookSupport": ".webhook_support",
    "WebhookSupportManagedVia": ".webhook_support_managed_via",
    "WebhookSupportMode": ".webhook_support_mode",
    "WebhookSupportSubscriptionLevel": ".webhook_support_subscription_level",
    "WebhookSupportVirtualWebhooks": ".webhook_support_virtual_webhooks",
    "WebhookSupportVirtualWebhooksRequestRate": ".webhook_support_virtual_webhooks_request_rate",
    "WebhookSupportVirtualWebhooksRequestRateUnit": ".webhook_support_virtual_webhooks_request_rate_unit",
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
    "Api",
    "ApiResource",
    "ApiResourceCoverage",
    "ApiResourceCoverageCoverageItem",
    "ApiResourceLinkedResourcesItem",
    "ApiResourcesItem",
    "ApiStatus",
    "ApiType",
    "ApisFilter",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "Connector",
    "ConnectorAuthType",
    "ConnectorDoc",
    "ConnectorDocAudience",
    "ConnectorDocFormat",
    "ConnectorEvent",
    "ConnectorEventEventSource",
    "ConnectorOauthCredentialsSource",
    "ConnectorOauthGrantType",
    "ConnectorOauthScopesItem",
    "ConnectorResource",
    "ConnectorSetting",
    "ConnectorSettingType",
    "ConnectorStatus",
    "ConnectorTlsSupport",
    "ConnectorUnifiedApisItem",
    "ConnectorUnifiedApisItemOauthScopesItem",
    "ConnectorsFilter",
    "GetApiResourceCoverageResponse",
    "GetApiResourceResponse",
    "GetApiResponse",
    "GetApisResponse",
    "GetConnectorResourceResponse",
    "GetConnectorResponse",
    "GetConnectorsResponse",
    "Id",
    "LinkedConnectorResource",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "PaginationCoverage",
    "PaginationCoverageMode",
    "PaymentRequiredResponse",
    "ResourceId",
    "ResourceStatus",
    "SupportedProperty",
    "SupportedPropertyChildPropertiesItem",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedApiId",
    "UnifiedProperty",
    "WebhookSupport",
    "WebhookSupportManagedVia",
    "WebhookSupportMode",
    "WebhookSupportSubscriptionLevel",
    "WebhookSupportVirtualWebhooks",
    "WebhookSupportVirtualWebhooksRequestRate",
    "WebhookSupportVirtualWebhooksRequestRateUnit",
]
