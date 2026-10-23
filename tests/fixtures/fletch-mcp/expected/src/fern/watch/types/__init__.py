



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_watchers_id_response import DeleteWatchersIdResponse
    from .delete_webhooks_id_response import DeleteWebhooksIdResponse
    from .get_watchers_id_response import GetWatchersIdResponse
    from .get_watchers_id_response_watcher import GetWatchersIdResponseWatcher
    from .get_watchers_id_response_watcher_delivery import GetWatchersIdResponseWatcherDelivery
    from .get_watchers_id_response_watcher_kind import GetWatchersIdResponseWatcherKind
    from .get_watchers_id_response_watcher_last_delivery import GetWatchersIdResponseWatcherLastDelivery
    from .get_watchers_id_response_watcher_status import GetWatchersIdResponseWatcherStatus
    from .get_watchers_id_runs_response import GetWatchersIdRunsResponse
    from .get_watchers_id_runs_response_runs_item import GetWatchersIdRunsResponseRunsItem
    from .get_watchers_id_runs_response_runs_item_status import GetWatchersIdRunsResponseRunsItemStatus
    from .get_watchers_response import GetWatchersResponse
    from .get_watchers_response_watchers_item import GetWatchersResponseWatchersItem
    from .get_watchers_response_watchers_item_delivery import GetWatchersResponseWatchersItemDelivery
    from .get_watchers_response_watchers_item_kind import GetWatchersResponseWatchersItemKind
    from .get_watchers_response_watchers_item_last_delivery import GetWatchersResponseWatchersItemLastDelivery
    from .get_watchers_response_watchers_item_status import GetWatchersResponseWatchersItemStatus
    from .get_webhooks_response import GetWebhooksResponse
    from .get_webhooks_response_webhooks_item import GetWebhooksResponseWebhooksItem
    from .patch_watchers_id_response import PatchWatchersIdResponse
    from .patch_watchers_id_response_watcher import PatchWatchersIdResponseWatcher
    from .patch_watchers_id_response_watcher_delivery import PatchWatchersIdResponseWatcherDelivery
    from .patch_watchers_id_response_watcher_kind import PatchWatchersIdResponseWatcherKind
    from .patch_watchers_id_response_watcher_last_delivery import PatchWatchersIdResponseWatcherLastDelivery
    from .patch_watchers_id_response_watcher_status import PatchWatchersIdResponseWatcherStatus
    from .patch_webhooks_id_response import PatchWebhooksIdResponse
    from .patch_webhooks_id_response_webhook import PatchWebhooksIdResponseWebhook
    from .patch_webhooks_id_response_webhook_created_at import PatchWebhooksIdResponseWebhookCreatedAt
    from .patch_webhooks_id_response_webhook_one import PatchWebhooksIdResponseWebhookOne
    from .post_watchers_request_kind import PostWatchersRequestKind
    from .post_watchers_response import PostWatchersResponse
    from .post_watchers_response_watcher import PostWatchersResponseWatcher
    from .post_watchers_response_watcher_delivery import PostWatchersResponseWatcherDelivery
    from .post_watchers_response_watcher_kind import PostWatchersResponseWatcherKind
    from .post_watchers_response_watcher_last_delivery import PostWatchersResponseWatcherLastDelivery
    from .post_watchers_response_watcher_status import PostWatchersResponseWatcherStatus
    from .post_webhooks_id_test_response import PostWebhooksIdTestResponse
    from .post_webhooks_response import PostWebhooksResponse
    from .post_webhooks_response_webhook import PostWebhooksResponseWebhook
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteWatchersIdResponse": ".delete_watchers_id_response",
    "DeleteWebhooksIdResponse": ".delete_webhooks_id_response",
    "GetWatchersIdResponse": ".get_watchers_id_response",
    "GetWatchersIdResponseWatcher": ".get_watchers_id_response_watcher",
    "GetWatchersIdResponseWatcherDelivery": ".get_watchers_id_response_watcher_delivery",
    "GetWatchersIdResponseWatcherKind": ".get_watchers_id_response_watcher_kind",
    "GetWatchersIdResponseWatcherLastDelivery": ".get_watchers_id_response_watcher_last_delivery",
    "GetWatchersIdResponseWatcherStatus": ".get_watchers_id_response_watcher_status",
    "GetWatchersIdRunsResponse": ".get_watchers_id_runs_response",
    "GetWatchersIdRunsResponseRunsItem": ".get_watchers_id_runs_response_runs_item",
    "GetWatchersIdRunsResponseRunsItemStatus": ".get_watchers_id_runs_response_runs_item_status",
    "GetWatchersResponse": ".get_watchers_response",
    "GetWatchersResponseWatchersItem": ".get_watchers_response_watchers_item",
    "GetWatchersResponseWatchersItemDelivery": ".get_watchers_response_watchers_item_delivery",
    "GetWatchersResponseWatchersItemKind": ".get_watchers_response_watchers_item_kind",
    "GetWatchersResponseWatchersItemLastDelivery": ".get_watchers_response_watchers_item_last_delivery",
    "GetWatchersResponseWatchersItemStatus": ".get_watchers_response_watchers_item_status",
    "GetWebhooksResponse": ".get_webhooks_response",
    "GetWebhooksResponseWebhooksItem": ".get_webhooks_response_webhooks_item",
    "PatchWatchersIdResponse": ".patch_watchers_id_response",
    "PatchWatchersIdResponseWatcher": ".patch_watchers_id_response_watcher",
    "PatchWatchersIdResponseWatcherDelivery": ".patch_watchers_id_response_watcher_delivery",
    "PatchWatchersIdResponseWatcherKind": ".patch_watchers_id_response_watcher_kind",
    "PatchWatchersIdResponseWatcherLastDelivery": ".patch_watchers_id_response_watcher_last_delivery",
    "PatchWatchersIdResponseWatcherStatus": ".patch_watchers_id_response_watcher_status",
    "PatchWebhooksIdResponse": ".patch_webhooks_id_response",
    "PatchWebhooksIdResponseWebhook": ".patch_webhooks_id_response_webhook",
    "PatchWebhooksIdResponseWebhookCreatedAt": ".patch_webhooks_id_response_webhook_created_at",
    "PatchWebhooksIdResponseWebhookOne": ".patch_webhooks_id_response_webhook_one",
    "PostWatchersRequestKind": ".post_watchers_request_kind",
    "PostWatchersResponse": ".post_watchers_response",
    "PostWatchersResponseWatcher": ".post_watchers_response_watcher",
    "PostWatchersResponseWatcherDelivery": ".post_watchers_response_watcher_delivery",
    "PostWatchersResponseWatcherKind": ".post_watchers_response_watcher_kind",
    "PostWatchersResponseWatcherLastDelivery": ".post_watchers_response_watcher_last_delivery",
    "PostWatchersResponseWatcherStatus": ".post_watchers_response_watcher_status",
    "PostWebhooksIdTestResponse": ".post_webhooks_id_test_response",
    "PostWebhooksResponse": ".post_webhooks_response",
    "PostWebhooksResponseWebhook": ".post_webhooks_response_webhook",
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
    "DeleteWatchersIdResponse",
    "DeleteWebhooksIdResponse",
    "GetWatchersIdResponse",
    "GetWatchersIdResponseWatcher",
    "GetWatchersIdResponseWatcherDelivery",
    "GetWatchersIdResponseWatcherKind",
    "GetWatchersIdResponseWatcherLastDelivery",
    "GetWatchersIdResponseWatcherStatus",
    "GetWatchersIdRunsResponse",
    "GetWatchersIdRunsResponseRunsItem",
    "GetWatchersIdRunsResponseRunsItemStatus",
    "GetWatchersResponse",
    "GetWatchersResponseWatchersItem",
    "GetWatchersResponseWatchersItemDelivery",
    "GetWatchersResponseWatchersItemKind",
    "GetWatchersResponseWatchersItemLastDelivery",
    "GetWatchersResponseWatchersItemStatus",
    "GetWebhooksResponse",
    "GetWebhooksResponseWebhooksItem",
    "PatchWatchersIdResponse",
    "PatchWatchersIdResponseWatcher",
    "PatchWatchersIdResponseWatcherDelivery",
    "PatchWatchersIdResponseWatcherKind",
    "PatchWatchersIdResponseWatcherLastDelivery",
    "PatchWatchersIdResponseWatcherStatus",
    "PatchWebhooksIdResponse",
    "PatchWebhooksIdResponseWebhook",
    "PatchWebhooksIdResponseWebhookCreatedAt",
    "PatchWebhooksIdResponseWebhookOne",
    "PostWatchersRequestKind",
    "PostWatchersResponse",
    "PostWatchersResponseWatcher",
    "PostWatchersResponseWatcherDelivery",
    "PostWatchersResponseWatcherKind",
    "PostWatchersResponseWatcherLastDelivery",
    "PostWatchersResponseWatcherStatus",
    "PostWebhooksIdTestResponse",
    "PostWebhooksResponse",
    "PostWebhooksResponseWebhook",
]
