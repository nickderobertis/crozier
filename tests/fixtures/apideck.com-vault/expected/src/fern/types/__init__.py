



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .application_id import ApplicationId
    from .auth_type import AuthType
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .connection import Connection
    from .connection_configuration_item import ConnectionConfigurationItem
    from .connection_configuration_item_defaults_item import ConnectionConfigurationItemDefaultsItem
    from .connection_configuration_item_defaults_item_target import ConnectionConfigurationItemDefaultsItemTarget
    from .connection_configuration_item_defaults_item_value import ConnectionConfigurationItemDefaultsItemValue
    from .connection_configuration_item_defaults_item_value_four_item import (
        ConnectionConfigurationItemDefaultsItemValueFourItem,
    )
    from .connection_event import ConnectionEvent
    from .connection_metadata import ConnectionMetadata
    from .connection_state import ConnectionState
    from .connection_status import ConnectionStatus
    from .connection_webhook import ConnectionWebhook
    from .connection_webhook_disabled_reason import ConnectionWebhookDisabledReason
    from .connection_webhook_events_item import ConnectionWebhookEventsItem
    from .connection_webhook_status import ConnectionWebhookStatus
    from .consumer import Consumer
    from .consumer_connection import ConsumerConnection
    from .consumer_connection_state import ConsumerConnectionState
    from .consumer_id import ConsumerId
    from .consumer_metadata import ConsumerMetadata
    from .consumer_request_counts_in_date_range_response import ConsumerRequestCountsInDateRangeResponse
    from .consumer_request_counts_in_date_range_response_data import ConsumerRequestCountsInDateRangeResponseData
    from .create_connection_response import CreateConnectionResponse
    from .create_consumer_response import CreateConsumerResponse
    from .create_session_response import CreateSessionResponse
    from .create_session_response_data import CreateSessionResponseData
    from .delete_consumer_response import DeleteConsumerResponse
    from .delete_consumer_response_data import DeleteConsumerResponseData
    from .form_field import FormField
    from .form_field_option import FormFieldOption
    from .form_field_option_group import FormFieldOptionGroup
    from .form_field_type import FormFieldType
    from .get_connection_response import GetConnectionResponse
    from .get_connections_response import GetConnectionsResponse
    from .get_consumer_response import GetConsumerResponse
    from .get_consumers_response import GetConsumersResponse
    from .get_consumers_response_data_item import GetConsumersResponseDataItem
    from .get_logs_response import GetLogsResponse
    from .integration_state import IntegrationState
    from .links import Links
    from .log import Log
    from .log_operation import LogOperation
    from .log_service import LogService
    from .log_unified_api import LogUnifiedApi
    from .logs_filter import LogsFilter
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .o_auth_grant_type import OAuthGrantType
    from .payment_required_response import PaymentRequiredResponse
    from .proxy_request import ProxyRequest
    from .request_count_allocation import RequestCountAllocation
    from .simple_form_field_option import SimpleFormFieldOption
    from .simple_form_field_option_value import SimpleFormFieldOptionValue
    from .simple_form_field_option_value_four_item import SimpleFormFieldOptionValueFourItem
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_api_id import UnifiedApiId
    from .unprocessable_response import UnprocessableResponse
    from .update_connection_response import UpdateConnectionResponse
    from .update_consumer_response import UpdateConsumerResponse
    from .vault_event_type import VaultEventType
    from .webhook_subscription import WebhookSubscription
_dynamic_imports: typing.Dict[str, str] = {
    "ApplicationId": ".application_id",
    "AuthType": ".auth_type",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "Connection": ".connection",
    "ConnectionConfigurationItem": ".connection_configuration_item",
    "ConnectionConfigurationItemDefaultsItem": ".connection_configuration_item_defaults_item",
    "ConnectionConfigurationItemDefaultsItemTarget": ".connection_configuration_item_defaults_item_target",
    "ConnectionConfigurationItemDefaultsItemValue": ".connection_configuration_item_defaults_item_value",
    "ConnectionConfigurationItemDefaultsItemValueFourItem": ".connection_configuration_item_defaults_item_value_four_item",
    "ConnectionEvent": ".connection_event",
    "ConnectionMetadata": ".connection_metadata",
    "ConnectionState": ".connection_state",
    "ConnectionStatus": ".connection_status",
    "ConnectionWebhook": ".connection_webhook",
    "ConnectionWebhookDisabledReason": ".connection_webhook_disabled_reason",
    "ConnectionWebhookEventsItem": ".connection_webhook_events_item",
    "ConnectionWebhookStatus": ".connection_webhook_status",
    "Consumer": ".consumer",
    "ConsumerConnection": ".consumer_connection",
    "ConsumerConnectionState": ".consumer_connection_state",
    "ConsumerId": ".consumer_id",
    "ConsumerMetadata": ".consumer_metadata",
    "ConsumerRequestCountsInDateRangeResponse": ".consumer_request_counts_in_date_range_response",
    "ConsumerRequestCountsInDateRangeResponseData": ".consumer_request_counts_in_date_range_response_data",
    "CreateConnectionResponse": ".create_connection_response",
    "CreateConsumerResponse": ".create_consumer_response",
    "CreateSessionResponse": ".create_session_response",
    "CreateSessionResponseData": ".create_session_response_data",
    "DeleteConsumerResponse": ".delete_consumer_response",
    "DeleteConsumerResponseData": ".delete_consumer_response_data",
    "FormField": ".form_field",
    "FormFieldOption": ".form_field_option",
    "FormFieldOptionGroup": ".form_field_option_group",
    "FormFieldType": ".form_field_type",
    "GetConnectionResponse": ".get_connection_response",
    "GetConnectionsResponse": ".get_connections_response",
    "GetConsumerResponse": ".get_consumer_response",
    "GetConsumersResponse": ".get_consumers_response",
    "GetConsumersResponseDataItem": ".get_consumers_response_data_item",
    "GetLogsResponse": ".get_logs_response",
    "IntegrationState": ".integration_state",
    "Links": ".links",
    "Log": ".log",
    "LogOperation": ".log_operation",
    "LogService": ".log_service",
    "LogUnifiedApi": ".log_unified_api",
    "LogsFilter": ".logs_filter",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "OAuthGrantType": ".o_auth_grant_type",
    "PaymentRequiredResponse": ".payment_required_response",
    "ProxyRequest": ".proxy_request",
    "RequestCountAllocation": ".request_count_allocation",
    "SimpleFormFieldOption": ".simple_form_field_option",
    "SimpleFormFieldOptionValue": ".simple_form_field_option_value",
    "SimpleFormFieldOptionValueFourItem": ".simple_form_field_option_value_four_item",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedApiId": ".unified_api_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateConnectionResponse": ".update_connection_response",
    "UpdateConsumerResponse": ".update_consumer_response",
    "VaultEventType": ".vault_event_type",
    "WebhookSubscription": ".webhook_subscription",
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
    "ApplicationId",
    "AuthType",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "Connection",
    "ConnectionConfigurationItem",
    "ConnectionConfigurationItemDefaultsItem",
    "ConnectionConfigurationItemDefaultsItemTarget",
    "ConnectionConfigurationItemDefaultsItemValue",
    "ConnectionConfigurationItemDefaultsItemValueFourItem",
    "ConnectionEvent",
    "ConnectionMetadata",
    "ConnectionState",
    "ConnectionStatus",
    "ConnectionWebhook",
    "ConnectionWebhookDisabledReason",
    "ConnectionWebhookEventsItem",
    "ConnectionWebhookStatus",
    "Consumer",
    "ConsumerConnection",
    "ConsumerConnectionState",
    "ConsumerId",
    "ConsumerMetadata",
    "ConsumerRequestCountsInDateRangeResponse",
    "ConsumerRequestCountsInDateRangeResponseData",
    "CreateConnectionResponse",
    "CreateConsumerResponse",
    "CreateSessionResponse",
    "CreateSessionResponseData",
    "DeleteConsumerResponse",
    "DeleteConsumerResponseData",
    "FormField",
    "FormFieldOption",
    "FormFieldOptionGroup",
    "FormFieldType",
    "GetConnectionResponse",
    "GetConnectionsResponse",
    "GetConsumerResponse",
    "GetConsumersResponse",
    "GetConsumersResponseDataItem",
    "GetLogsResponse",
    "IntegrationState",
    "Links",
    "Log",
    "LogOperation",
    "LogService",
    "LogUnifiedApi",
    "LogsFilter",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "OAuthGrantType",
    "PaymentRequiredResponse",
    "ProxyRequest",
    "RequestCountAllocation",
    "SimpleFormFieldOption",
    "SimpleFormFieldOptionValue",
    "SimpleFormFieldOptionValueFourItem",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedApiId",
    "UnprocessableResponse",
    "UpdateConnectionResponse",
    "UpdateConsumerResponse",
    "VaultEventType",
    "WebhookSubscription",
]
