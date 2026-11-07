



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_a_webhook_response import CreateAWebhookResponse
    from .delete_a_webhook_response import DeleteAWebhookResponse
    from .list_all_webhooks_response import ListAllWebhooksResponse
    from .list_all_webhooks_response_list_item import ListAllWebhooksResponseListItem
    from .retrieve_a_webhook_response import RetrieveAWebhookResponse
    from .update_a_webhook_response import UpdateAWebhookResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAWebhookResponse": ".create_a_webhook_response",
    "DeleteAWebhookResponse": ".delete_a_webhook_response",
    "ListAllWebhooksResponse": ".list_all_webhooks_response",
    "ListAllWebhooksResponseListItem": ".list_all_webhooks_response_list_item",
    "RetrieveAWebhookResponse": ".retrieve_a_webhook_response",
    "UpdateAWebhookResponse": ".update_a_webhook_response",
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
    "CreateAWebhookResponse",
    "DeleteAWebhookResponse",
    "ListAllWebhooksResponse",
    "ListAllWebhooksResponseListItem",
    "RetrieveAWebhookResponse",
    "UpdateAWebhookResponse",
]
