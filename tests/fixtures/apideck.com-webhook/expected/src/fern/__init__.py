



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ApplicationId,
        BadRequestResponse,
        BadRequestResponseDetail,
        ConsumerId,
        CreateWebhookResponse,
        CreatedAt,
        DeleteWebhookResponse,
        DeliveryUrl,
        Description,
        ExecuteBaseUrl,
        ExecuteWebhookEventRequest,
        ExecuteWebhookEventsRequest,
        ExecuteWebhookResponse,
        GetWebhookEventLogsResponse,
        GetWebhookResponse,
        GetWebhooksResponse,
        Links,
        Meta,
        MetaCursors,
        NotFoundResponse,
        NotFoundResponseDetail,
        NotImplementedResponse,
        NotImplementedResponseDetail,
        PaymentRequiredResponse,
        ResolveWebhookEventRequest,
        ResolveWebhookEventsRequest,
        ResolveWebhookResponse,
        ServiceId,
        Status,
        UnauthorizedResponse,
        UnexpectedErrorResponse,
        UnexpectedErrorResponseDetail,
        UnifiedApiId,
        UnprocessableResponse,
        UpdateWebhookResponse,
        UpdatedAt,
        Webhook,
        WebhookDisabledReason,
        WebhookEvent,
        WebhookEventLog,
        WebhookEventLogAttemptsItem,
        WebhookEventLogService,
        WebhookEventLogsFilter,
        WebhookEventLogsFilterService,
        WebhookEventType,
    )
    from .errors import (
        BadRequestError,
        NotFoundError,
        PaymentRequiredError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import webhooks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
    from .webhooks import WebhooksExecuteRequestBody, WebhooksResolveRequestBody, WebhooksShortExecuteRequestBody
_dynamic_imports: typing.Dict[str, str] = {
    "ApplicationId": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestResponse": ".types",
    "BadRequestResponseDetail": ".types",
    "ConsumerId": ".types",
    "CreateWebhookResponse": ".types",
    "CreatedAt": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeleteWebhookResponse": ".types",
    "DeliveryUrl": ".types",
    "Description": ".types",
    "ExecuteBaseUrl": ".types",
    "ExecuteWebhookEventRequest": ".types",
    "ExecuteWebhookEventsRequest": ".types",
    "ExecuteWebhookResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetWebhookEventLogsResponse": ".types",
    "GetWebhookResponse": ".types",
    "GetWebhooksResponse": ".types",
    "Links": ".types",
    "Meta": ".types",
    "MetaCursors": ".types",
    "NotFoundError": ".errors",
    "NotFoundResponse": ".types",
    "NotFoundResponseDetail": ".types",
    "NotImplementedResponse": ".types",
    "NotImplementedResponseDetail": ".types",
    "PaymentRequiredError": ".errors",
    "PaymentRequiredResponse": ".types",
    "ResolveWebhookEventRequest": ".types",
    "ResolveWebhookEventsRequest": ".types",
    "ResolveWebhookResponse": ".types",
    "ServiceId": ".types",
    "Status": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedResponse": ".types",
    "UnexpectedErrorResponse": ".types",
    "UnexpectedErrorResponseDetail": ".types",
    "UnifiedApiId": ".types",
    "UnprocessableEntityError": ".errors",
    "UnprocessableResponse": ".types",
    "UpdateWebhookResponse": ".types",
    "UpdatedAt": ".types",
    "Webhook": ".types",
    "WebhookDisabledReason": ".types",
    "WebhookEvent": ".types",
    "WebhookEventLog": ".types",
    "WebhookEventLogAttemptsItem": ".types",
    "WebhookEventLogService": ".types",
    "WebhookEventLogsFilter": ".types",
    "WebhookEventLogsFilterService": ".types",
    "WebhookEventType": ".types",
    "WebhooksExecuteRequestBody": ".webhooks",
    "WebhooksResolveRequestBody": ".webhooks",
    "WebhooksShortExecuteRequestBody": ".webhooks",
    "__version__": ".version",
    "webhooks": ".webhooks",
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
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "ConsumerId",
    "CreateWebhookResponse",
    "CreatedAt",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeleteWebhookResponse",
    "DeliveryUrl",
    "Description",
    "ExecuteBaseUrl",
    "ExecuteWebhookEventRequest",
    "ExecuteWebhookEventsRequest",
    "ExecuteWebhookResponse",
    "FernApi",
    "FernApiEnvironment",
    "GetWebhookEventLogsResponse",
    "GetWebhookResponse",
    "GetWebhooksResponse",
    "Links",
    "Meta",
    "MetaCursors",
    "NotFoundError",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredError",
    "PaymentRequiredResponse",
    "ResolveWebhookEventRequest",
    "ResolveWebhookEventsRequest",
    "ResolveWebhookResponse",
    "ServiceId",
    "Status",
    "UnauthorizedError",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedApiId",
    "UnprocessableEntityError",
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
    "WebhooksExecuteRequestBody",
    "WebhooksResolveRequestBody",
    "WebhooksShortExecuteRequestBody",
    "__version__",
    "webhooks",
]
