



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .application_id import ApplicationId
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .consumer_id import ConsumerId
    from .create_webhook_response import CreateWebhookResponse
    from .created_at import CreatedAt
    from .delete_webhook_response import DeleteWebhookResponse
    from .delivery_url import DeliveryUrl
    from .description import Description
    from .execute_base_url import ExecuteBaseUrl
    from .execute_webhook_event_request import ExecuteWebhookEventRequest
    from .execute_webhook_events_request import ExecuteWebhookEventsRequest
    from .execute_webhook_response import ExecuteWebhookResponse
    from .get_webhook_event_logs_response import GetWebhookEventLogsResponse
    from .get_webhook_response import GetWebhookResponse
    from .get_webhooks_response import GetWebhooksResponse
    from .links import Links
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .payment_required_response import PaymentRequiredResponse
    from .resolve_webhook_event_request import ResolveWebhookEventRequest
    from .resolve_webhook_events_request import ResolveWebhookEventsRequest
    from .resolve_webhook_response import ResolveWebhookResponse
    from .service_id import ServiceId
    from .status import Status
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_api_id import UnifiedApiId
    from .unprocessable_response import UnprocessableResponse
    from .update_webhook_response import UpdateWebhookResponse
    from .updated_at import UpdatedAt
    from .webhook import Webhook
    from .webhook_disabled_reason import WebhookDisabledReason
    from .webhook_event import WebhookEvent
    from .webhook_event_log import WebhookEventLog
    from .webhook_event_log_attempts_item import WebhookEventLogAttemptsItem
    from .webhook_event_log_service import WebhookEventLogService
    from .webhook_event_logs_filter import WebhookEventLogsFilter
    from .webhook_event_logs_filter_service import WebhookEventLogsFilterService
    from .webhook_event_type import WebhookEventType
_dynamic_imports: typing.Dict[str, str] = {
    "ApplicationId": ".application_id",
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "ConsumerId": ".consumer_id",
    "CreateWebhookResponse": ".create_webhook_response",
    "CreatedAt": ".created_at",
    "DeleteWebhookResponse": ".delete_webhook_response",
    "DeliveryUrl": ".delivery_url",
    "Description": ".description",
    "ExecuteBaseUrl": ".execute_base_url",
    "ExecuteWebhookEventRequest": ".execute_webhook_event_request",
    "ExecuteWebhookEventsRequest": ".execute_webhook_events_request",
    "ExecuteWebhookResponse": ".execute_webhook_response",
    "GetWebhookEventLogsResponse": ".get_webhook_event_logs_response",
    "GetWebhookResponse": ".get_webhook_response",
    "GetWebhooksResponse": ".get_webhooks_response",
    "Links": ".links",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PaymentRequiredResponse": ".payment_required_response",
    "ResolveWebhookEventRequest": ".resolve_webhook_event_request",
    "ResolveWebhookEventsRequest": ".resolve_webhook_events_request",
    "ResolveWebhookResponse": ".resolve_webhook_response",
    "ServiceId": ".service_id",
    "Status": ".status",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedApiId": ".unified_api_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateWebhookResponse": ".update_webhook_response",
    "UpdatedAt": ".updated_at",
    "Webhook": ".webhook",
    "WebhookDisabledReason": ".webhook_disabled_reason",
    "WebhookEvent": ".webhook_event",
    "WebhookEventLog": ".webhook_event_log",
    "WebhookEventLogAttemptsItem": ".webhook_event_log_attempts_item",
    "WebhookEventLogService": ".webhook_event_log_service",
    "WebhookEventLogsFilter": ".webhook_event_logs_filter",
    "WebhookEventLogsFilterService": ".webhook_event_logs_filter_service",
    "WebhookEventType": ".webhook_event_type",
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
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "ConsumerId",
    "CreateWebhookResponse",
    "CreatedAt",
    "DeleteWebhookResponse",
    "DeliveryUrl",
    "Description",
    "ExecuteBaseUrl",
    "ExecuteWebhookEventRequest",
    "ExecuteWebhookEventsRequest",
    "ExecuteWebhookResponse",
    "GetWebhookEventLogsResponse",
    "GetWebhookResponse",
    "GetWebhooksResponse",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredResponse",
    "ResolveWebhookEventRequest",
    "ResolveWebhookEventsRequest",
    "ResolveWebhookResponse",
    "ServiceId",
    "Status",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedApiId",
    "UnprocessableResponse",
    "UpdateWebhookResponse",
    "UpdatedAt",
    "Webhook",
    "WebhookDisabledReason",
    "WebhookEvent",
    "WebhookEventLog",
    "WebhookEventLogAttemptsItem",
    "WebhookEventLogService",
    "WebhookEventLogsFilter",
    "WebhookEventLogsFilterService",
    "WebhookEventType",
]
