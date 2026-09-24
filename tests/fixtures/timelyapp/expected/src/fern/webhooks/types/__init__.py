



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .v1webhooks_create_webhook import V1WebhooksCreateWebhook
    from .v1webhooks_create_webhook_subscriptions_item import V1WebhooksCreateWebhookSubscriptionsItem
    from .v1webhooks_update_webhook import V1WebhooksUpdateWebhook
    from .v1webhooks_update_webhook_subscriptions_item import V1WebhooksUpdateWebhookSubscriptionsItem
_dynamic_imports: typing.Dict[str, str] = {
    "V1WebhooksCreateWebhook": ".v1webhooks_create_webhook",
    "V1WebhooksCreateWebhookSubscriptionsItem": ".v1webhooks_create_webhook_subscriptions_item",
    "V1WebhooksUpdateWebhook": ".v1webhooks_update_webhook",
    "V1WebhooksUpdateWebhookSubscriptionsItem": ".v1webhooks_update_webhook_subscriptions_item",
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
    "V1WebhooksCreateWebhook",
    "V1WebhooksCreateWebhookSubscriptionsItem",
    "V1WebhooksUpdateWebhook",
    "V1WebhooksUpdateWebhookSubscriptionsItem",
]
