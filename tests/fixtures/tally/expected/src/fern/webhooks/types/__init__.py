



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_webhook_request_http_headers_item import CreateWebhookRequestHttpHeadersItem
    from .create_webhook_response import CreateWebhookResponse
    from .list_webhook_events_response import ListWebhookEventsResponse
    from .list_webhook_events_response_events_item import ListWebhookEventsResponseEventsItem
    from .list_webhook_events_response_events_item_delivery_status import (
        ListWebhookEventsResponseEventsItemDeliveryStatus,
    )
    from .list_webhook_events_response_events_item_event_type import ListWebhookEventsResponseEventsItemEventType
    from .list_webhooks_response import ListWebhooksResponse
    from .list_webhooks_response_webhooks_item import ListWebhooksResponseWebhooksItem
    from .list_webhooks_response_webhooks_item_http_headers_item import ListWebhooksResponseWebhooksItemHttpHeadersItem
    from .update_webhook_request_http_headers_item import UpdateWebhookRequestHttpHeadersItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateWebhookRequestHttpHeadersItem": ".create_webhook_request_http_headers_item",
    "CreateWebhookResponse": ".create_webhook_response",
    "ListWebhookEventsResponse": ".list_webhook_events_response",
    "ListWebhookEventsResponseEventsItem": ".list_webhook_events_response_events_item",
    "ListWebhookEventsResponseEventsItemDeliveryStatus": ".list_webhook_events_response_events_item_delivery_status",
    "ListWebhookEventsResponseEventsItemEventType": ".list_webhook_events_response_events_item_event_type",
    "ListWebhooksResponse": ".list_webhooks_response",
    "ListWebhooksResponseWebhooksItem": ".list_webhooks_response_webhooks_item",
    "ListWebhooksResponseWebhooksItemHttpHeadersItem": ".list_webhooks_response_webhooks_item_http_headers_item",
    "UpdateWebhookRequestHttpHeadersItem": ".update_webhook_request_http_headers_item",
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
    "CreateWebhookRequestHttpHeadersItem",
    "CreateWebhookResponse",
    "ListWebhookEventsResponse",
    "ListWebhookEventsResponseEventsItem",
    "ListWebhookEventsResponseEventsItemDeliveryStatus",
    "ListWebhookEventsResponseEventsItemEventType",
    "ListWebhooksResponse",
    "ListWebhooksResponseWebhooksItem",
    "ListWebhooksResponseWebhooksItemHttpHeadersItem",
    "UpdateWebhookRequestHttpHeadersItem",
]
