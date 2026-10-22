



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_webhook_request_source import CreateWebhookRequestSource
    from .create_webhook_request_triggers_item import CreateWebhookRequestTriggersItem
    from .create_webhook_response import CreateWebhookResponse
    from .create_webhook_response_source import CreateWebhookResponseSource
    from .create_webhook_response_triggers_item import CreateWebhookResponseTriggersItem
    from .delete_webhook_response import DeleteWebhookResponse
    from .delete_webhook_response_source import DeleteWebhookResponseSource
    from .delete_webhook_response_triggers_item import DeleteWebhookResponseTriggersItem
    from .get_webhook_response import GetWebhookResponse
    from .get_webhook_response_source import GetWebhookResponseSource
    from .get_webhook_response_triggers_item import GetWebhookResponseTriggersItem
    from .get_webhooks_request_filter_date_field import GetWebhooksRequestFilterDateField
    from .get_webhooks_request_order import GetWebhooksRequestOrder
    from .get_webhooks_request_sort_by import GetWebhooksRequestSortBy
    from .get_webhooks_response import GetWebhooksResponse
    from .get_webhooks_response_data_item import GetWebhooksResponseDataItem
    from .get_webhooks_response_data_item_source import GetWebhooksResponseDataItemSource
    from .get_webhooks_response_data_item_triggers_item import GetWebhooksResponseDataItemTriggersItem
    from .get_webhooks_response_meta import GetWebhooksResponseMeta
    from .update_webhook_request_source import UpdateWebhookRequestSource
    from .update_webhook_request_triggers_item import UpdateWebhookRequestTriggersItem
    from .update_webhook_response import UpdateWebhookResponse
    from .update_webhook_response_source import UpdateWebhookResponseSource
    from .update_webhook_response_triggers_item import UpdateWebhookResponseTriggersItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateWebhookRequestSource": ".create_webhook_request_source",
    "CreateWebhookRequestTriggersItem": ".create_webhook_request_triggers_item",
    "CreateWebhookResponse": ".create_webhook_response",
    "CreateWebhookResponseSource": ".create_webhook_response_source",
    "CreateWebhookResponseTriggersItem": ".create_webhook_response_triggers_item",
    "DeleteWebhookResponse": ".delete_webhook_response",
    "DeleteWebhookResponseSource": ".delete_webhook_response_source",
    "DeleteWebhookResponseTriggersItem": ".delete_webhook_response_triggers_item",
    "GetWebhookResponse": ".get_webhook_response",
    "GetWebhookResponseSource": ".get_webhook_response_source",
    "GetWebhookResponseTriggersItem": ".get_webhook_response_triggers_item",
    "GetWebhooksRequestFilterDateField": ".get_webhooks_request_filter_date_field",
    "GetWebhooksRequestOrder": ".get_webhooks_request_order",
    "GetWebhooksRequestSortBy": ".get_webhooks_request_sort_by",
    "GetWebhooksResponse": ".get_webhooks_response",
    "GetWebhooksResponseDataItem": ".get_webhooks_response_data_item",
    "GetWebhooksResponseDataItemSource": ".get_webhooks_response_data_item_source",
    "GetWebhooksResponseDataItemTriggersItem": ".get_webhooks_response_data_item_triggers_item",
    "GetWebhooksResponseMeta": ".get_webhooks_response_meta",
    "UpdateWebhookRequestSource": ".update_webhook_request_source",
    "UpdateWebhookRequestTriggersItem": ".update_webhook_request_triggers_item",
    "UpdateWebhookResponse": ".update_webhook_response",
    "UpdateWebhookResponseSource": ".update_webhook_response_source",
    "UpdateWebhookResponseTriggersItem": ".update_webhook_response_triggers_item",
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
    "CreateWebhookRequestSource",
    "CreateWebhookRequestTriggersItem",
    "CreateWebhookResponse",
    "CreateWebhookResponseSource",
    "CreateWebhookResponseTriggersItem",
    "DeleteWebhookResponse",
    "DeleteWebhookResponseSource",
    "DeleteWebhookResponseTriggersItem",
    "GetWebhookResponse",
    "GetWebhookResponseSource",
    "GetWebhookResponseTriggersItem",
    "GetWebhooksRequestFilterDateField",
    "GetWebhooksRequestOrder",
    "GetWebhooksRequestSortBy",
    "GetWebhooksResponse",
    "GetWebhooksResponseDataItem",
    "GetWebhooksResponseDataItemSource",
    "GetWebhooksResponseDataItemTriggersItem",
    "GetWebhooksResponseMeta",
    "UpdateWebhookRequestSource",
    "UpdateWebhookRequestTriggersItem",
    "UpdateWebhookResponse",
    "UpdateWebhookResponseSource",
    "UpdateWebhookResponseTriggersItem",
]
