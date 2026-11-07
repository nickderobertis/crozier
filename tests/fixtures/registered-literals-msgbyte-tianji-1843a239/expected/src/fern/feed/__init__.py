



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        FeedChannelInfoResponse,
        FeedChannelInfoResponseNotifyFrequency,
        FeedChannelsResponseItem,
        FeedChannelsResponseItemCount,
        FeedChannelsResponseItemNotifyFrequency,
        FeedCreateChannelRequestNotifyFrequency,
        FeedCreateChannelResponse,
        FeedCreateChannelResponseNotifyFrequency,
        FeedDeleteChannelResponse,
        FeedDeleteChannelResponseNotifyFrequency,
        FeedDisablePublicShareIdResponse,
        FeedFetchEventsByCursorResponse,
        FeedFetchEventsByCursorResponseItemsItem,
        FeedFetchPublicEventsByCursorResponse,
        FeedFetchPublicEventsByCursorResponseItemsItem,
        FeedGetChannelByShareIdResponse,
        FeedRefreshPublicShareIdResponse,
        FeedSendEventResponse,
        FeedStateAllResponseItem,
        FeedStateAllResponseItemStatus,
        FeedStateResolveResponse,
        FeedStateResolveResponseStatus,
        FeedStateUpsertResponse,
        FeedStateUpsertResponseStatus,
        FeedUpdateChannelInfoRequestNotifyFrequency,
        FeedUpdateChannelInfoResponse,
        FeedUpdateChannelInfoResponseNotifyFrequency,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "FeedChannelInfoResponse": ".types",
    "FeedChannelInfoResponseNotifyFrequency": ".types",
    "FeedChannelsResponseItem": ".types",
    "FeedChannelsResponseItemCount": ".types",
    "FeedChannelsResponseItemNotifyFrequency": ".types",
    "FeedCreateChannelRequestNotifyFrequency": ".types",
    "FeedCreateChannelResponse": ".types",
    "FeedCreateChannelResponseNotifyFrequency": ".types",
    "FeedDeleteChannelResponse": ".types",
    "FeedDeleteChannelResponseNotifyFrequency": ".types",
    "FeedDisablePublicShareIdResponse": ".types",
    "FeedFetchEventsByCursorResponse": ".types",
    "FeedFetchEventsByCursorResponseItemsItem": ".types",
    "FeedFetchPublicEventsByCursorResponse": ".types",
    "FeedFetchPublicEventsByCursorResponseItemsItem": ".types",
    "FeedGetChannelByShareIdResponse": ".types",
    "FeedRefreshPublicShareIdResponse": ".types",
    "FeedSendEventResponse": ".types",
    "FeedStateAllResponseItem": ".types",
    "FeedStateAllResponseItemStatus": ".types",
    "FeedStateResolveResponse": ".types",
    "FeedStateResolveResponseStatus": ".types",
    "FeedStateUpsertResponse": ".types",
    "FeedStateUpsertResponseStatus": ".types",
    "FeedUpdateChannelInfoRequestNotifyFrequency": ".types",
    "FeedUpdateChannelInfoResponse": ".types",
    "FeedUpdateChannelInfoResponseNotifyFrequency": ".types",
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
    "FeedChannelInfoResponse",
    "FeedChannelInfoResponseNotifyFrequency",
    "FeedChannelsResponseItem",
    "FeedChannelsResponseItemCount",
    "FeedChannelsResponseItemNotifyFrequency",
    "FeedCreateChannelRequestNotifyFrequency",
    "FeedCreateChannelResponse",
    "FeedCreateChannelResponseNotifyFrequency",
    "FeedDeleteChannelResponse",
    "FeedDeleteChannelResponseNotifyFrequency",
    "FeedDisablePublicShareIdResponse",
    "FeedFetchEventsByCursorResponse",
    "FeedFetchEventsByCursorResponseItemsItem",
    "FeedFetchPublicEventsByCursorResponse",
    "FeedFetchPublicEventsByCursorResponseItemsItem",
    "FeedGetChannelByShareIdResponse",
    "FeedRefreshPublicShareIdResponse",
    "FeedSendEventResponse",
    "FeedStateAllResponseItem",
    "FeedStateAllResponseItemStatus",
    "FeedStateResolveResponse",
    "FeedStateResolveResponseStatus",
    "FeedStateUpsertResponse",
    "FeedStateUpsertResponseStatus",
    "FeedUpdateChannelInfoRequestNotifyFrequency",
    "FeedUpdateChannelInfoResponse",
    "FeedUpdateChannelInfoResponseNotifyFrequency",
]
