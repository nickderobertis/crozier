



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DeleteWatchersIdResponse,
        DeleteWebhooksIdResponse,
        GetWatchersIdResponse,
        GetWatchersIdResponseWatcher,
        GetWatchersIdResponseWatcherDelivery,
        GetWatchersIdResponseWatcherKind,
        GetWatchersIdResponseWatcherLastDelivery,
        GetWatchersIdResponseWatcherStatus,
        GetWatchersIdRunsResponse,
        GetWatchersIdRunsResponseRunsItem,
        GetWatchersIdRunsResponseRunsItemStatus,
        GetWatchersResponse,
        GetWatchersResponseWatchersItem,
        GetWatchersResponseWatchersItemDelivery,
        GetWatchersResponseWatchersItemKind,
        GetWatchersResponseWatchersItemLastDelivery,
        GetWatchersResponseWatchersItemStatus,
        GetWebhooksResponse,
        GetWebhooksResponseWebhooksItem,
        PatchWatchersIdResponse,
        PatchWatchersIdResponseWatcher,
        PatchWatchersIdResponseWatcherDelivery,
        PatchWatchersIdResponseWatcherKind,
        PatchWatchersIdResponseWatcherLastDelivery,
        PatchWatchersIdResponseWatcherStatus,
        PatchWebhooksIdResponse,
        PatchWebhooksIdResponseWebhook,
        PatchWebhooksIdResponseWebhookCreatedAt,
        PatchWebhooksIdResponseWebhookOne,
        PostWatchersRequestKind,
        PostWatchersResponse,
        PostWatchersResponseWatcher,
        PostWatchersResponseWatcherDelivery,
        PostWatchersResponseWatcherKind,
        PostWatchersResponseWatcherLastDelivery,
        PostWatchersResponseWatcherStatus,
        PostWebhooksIdTestResponse,
        PostWebhooksResponse,
        PostWebhooksResponseWebhook,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteWatchersIdResponse": ".types",
    "DeleteWebhooksIdResponse": ".types",
    "GetWatchersIdResponse": ".types",
    "GetWatchersIdResponseWatcher": ".types",
    "GetWatchersIdResponseWatcherDelivery": ".types",
    "GetWatchersIdResponseWatcherKind": ".types",
    "GetWatchersIdResponseWatcherLastDelivery": ".types",
    "GetWatchersIdResponseWatcherStatus": ".types",
    "GetWatchersIdRunsResponse": ".types",
    "GetWatchersIdRunsResponseRunsItem": ".types",
    "GetWatchersIdRunsResponseRunsItemStatus": ".types",
    "GetWatchersResponse": ".types",
    "GetWatchersResponseWatchersItem": ".types",
    "GetWatchersResponseWatchersItemDelivery": ".types",
    "GetWatchersResponseWatchersItemKind": ".types",
    "GetWatchersResponseWatchersItemLastDelivery": ".types",
    "GetWatchersResponseWatchersItemStatus": ".types",
    "GetWebhooksResponse": ".types",
    "GetWebhooksResponseWebhooksItem": ".types",
    "PatchWatchersIdResponse": ".types",
    "PatchWatchersIdResponseWatcher": ".types",
    "PatchWatchersIdResponseWatcherDelivery": ".types",
    "PatchWatchersIdResponseWatcherKind": ".types",
    "PatchWatchersIdResponseWatcherLastDelivery": ".types",
    "PatchWatchersIdResponseWatcherStatus": ".types",
    "PatchWebhooksIdResponse": ".types",
    "PatchWebhooksIdResponseWebhook": ".types",
    "PatchWebhooksIdResponseWebhookCreatedAt": ".types",
    "PatchWebhooksIdResponseWebhookOne": ".types",
    "PostWatchersRequestKind": ".types",
    "PostWatchersResponse": ".types",
    "PostWatchersResponseWatcher": ".types",
    "PostWatchersResponseWatcherDelivery": ".types",
    "PostWatchersResponseWatcherKind": ".types",
    "PostWatchersResponseWatcherLastDelivery": ".types",
    "PostWatchersResponseWatcherStatus": ".types",
    "PostWebhooksIdTestResponse": ".types",
    "PostWebhooksResponse": ".types",
    "PostWebhooksResponseWebhook": ".types",
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
