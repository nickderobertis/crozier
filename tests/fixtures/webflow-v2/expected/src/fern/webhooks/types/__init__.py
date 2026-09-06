



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_webhooks_request_filter import CreateWebhooksRequestFilter
    from .create_webhooks_request_trigger_type import CreateWebhooksRequestTriggerType
    from .create_webhooks_response import CreateWebhooksResponse
    from .create_webhooks_response_filter import CreateWebhooksResponseFilter
    from .create_webhooks_response_trigger_type import CreateWebhooksResponseTriggerType
    from .get_webhooks_response import GetWebhooksResponse
    from .get_webhooks_response_filter import GetWebhooksResponseFilter
    from .get_webhooks_response_trigger_type import GetWebhooksResponseTriggerType
    from .list_webhooks_response import ListWebhooksResponse
    from .list_webhooks_response_pagination import ListWebhooksResponsePagination
    from .list_webhooks_response_webhooks_item import ListWebhooksResponseWebhooksItem
    from .list_webhooks_response_webhooks_item_filter import ListWebhooksResponseWebhooksItemFilter
    from .list_webhooks_response_webhooks_item_trigger_type import ListWebhooksResponseWebhooksItemTriggerType
_dynamic_imports: typing.Dict[str, str] = {
    "CreateWebhooksRequestFilter": ".create_webhooks_request_filter",
    "CreateWebhooksRequestTriggerType": ".create_webhooks_request_trigger_type",
    "CreateWebhooksResponse": ".create_webhooks_response",
    "CreateWebhooksResponseFilter": ".create_webhooks_response_filter",
    "CreateWebhooksResponseTriggerType": ".create_webhooks_response_trigger_type",
    "GetWebhooksResponse": ".get_webhooks_response",
    "GetWebhooksResponseFilter": ".get_webhooks_response_filter",
    "GetWebhooksResponseTriggerType": ".get_webhooks_response_trigger_type",
    "ListWebhooksResponse": ".list_webhooks_response",
    "ListWebhooksResponsePagination": ".list_webhooks_response_pagination",
    "ListWebhooksResponseWebhooksItem": ".list_webhooks_response_webhooks_item",
    "ListWebhooksResponseWebhooksItemFilter": ".list_webhooks_response_webhooks_item_filter",
    "ListWebhooksResponseWebhooksItemTriggerType": ".list_webhooks_response_webhooks_item_trigger_type",
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
    "CreateWebhooksRequestFilter",
    "CreateWebhooksRequestTriggerType",
    "CreateWebhooksResponse",
    "CreateWebhooksResponseFilter",
    "CreateWebhooksResponseTriggerType",
    "GetWebhooksResponse",
    "GetWebhooksResponseFilter",
    "GetWebhooksResponseTriggerType",
    "ListWebhooksResponse",
    "ListWebhooksResponsePagination",
    "ListWebhooksResponseWebhooksItem",
    "ListWebhooksResponseWebhooksItemFilter",
    "ListWebhooksResponseWebhooksItemTriggerType",
]
