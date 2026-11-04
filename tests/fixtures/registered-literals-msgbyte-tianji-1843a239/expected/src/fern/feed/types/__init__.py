



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .feed_channel_info_response import FeedChannelInfoResponse
    from .feed_channel_info_response_notify_frequency import FeedChannelInfoResponseNotifyFrequency
    from .feed_channels_response_item import FeedChannelsResponseItem
    from .feed_channels_response_item_count import FeedChannelsResponseItemCount
    from .feed_channels_response_item_notify_frequency import FeedChannelsResponseItemNotifyFrequency
    from .feed_create_channel_request_notify_frequency import FeedCreateChannelRequestNotifyFrequency
    from .feed_create_channel_response import FeedCreateChannelResponse
    from .feed_create_channel_response_notify_frequency import FeedCreateChannelResponseNotifyFrequency
    from .feed_delete_channel_response import FeedDeleteChannelResponse
    from .feed_delete_channel_response_notify_frequency import FeedDeleteChannelResponseNotifyFrequency
    from .feed_disable_public_share_id_response import FeedDisablePublicShareIdResponse
    from .feed_fetch_events_by_cursor_response import FeedFetchEventsByCursorResponse
    from .feed_fetch_events_by_cursor_response_items_item import FeedFetchEventsByCursorResponseItemsItem
    from .feed_fetch_public_events_by_cursor_response import FeedFetchPublicEventsByCursorResponse
    from .feed_fetch_public_events_by_cursor_response_items_item import FeedFetchPublicEventsByCursorResponseItemsItem
    from .feed_get_channel_by_share_id_response import FeedGetChannelByShareIdResponse
    from .feed_refresh_public_share_id_response import FeedRefreshPublicShareIdResponse
    from .feed_send_event_response import FeedSendEventResponse
    from .feed_state_all_response_item import FeedStateAllResponseItem
    from .feed_state_all_response_item_status import FeedStateAllResponseItemStatus
    from .feed_state_resolve_response import FeedStateResolveResponse
    from .feed_state_resolve_response_status import FeedStateResolveResponseStatus
    from .feed_state_upsert_response import FeedStateUpsertResponse
    from .feed_state_upsert_response_status import FeedStateUpsertResponseStatus
    from .feed_update_channel_info_request_notify_frequency import FeedUpdateChannelInfoRequestNotifyFrequency
    from .feed_update_channel_info_response import FeedUpdateChannelInfoResponse
    from .feed_update_channel_info_response_notify_frequency import FeedUpdateChannelInfoResponseNotifyFrequency
_dynamic_imports: typing.Dict[str, str] = {
    "FeedChannelInfoResponse": ".feed_channel_info_response",
    "FeedChannelInfoResponseNotifyFrequency": ".feed_channel_info_response_notify_frequency",
    "FeedChannelsResponseItem": ".feed_channels_response_item",
    "FeedChannelsResponseItemCount": ".feed_channels_response_item_count",
    "FeedChannelsResponseItemNotifyFrequency": ".feed_channels_response_item_notify_frequency",
    "FeedCreateChannelRequestNotifyFrequency": ".feed_create_channel_request_notify_frequency",
    "FeedCreateChannelResponse": ".feed_create_channel_response",
    "FeedCreateChannelResponseNotifyFrequency": ".feed_create_channel_response_notify_frequency",
    "FeedDeleteChannelResponse": ".feed_delete_channel_response",
    "FeedDeleteChannelResponseNotifyFrequency": ".feed_delete_channel_response_notify_frequency",
    "FeedDisablePublicShareIdResponse": ".feed_disable_public_share_id_response",
    "FeedFetchEventsByCursorResponse": ".feed_fetch_events_by_cursor_response",
    "FeedFetchEventsByCursorResponseItemsItem": ".feed_fetch_events_by_cursor_response_items_item",
    "FeedFetchPublicEventsByCursorResponse": ".feed_fetch_public_events_by_cursor_response",
    "FeedFetchPublicEventsByCursorResponseItemsItem": ".feed_fetch_public_events_by_cursor_response_items_item",
    "FeedGetChannelByShareIdResponse": ".feed_get_channel_by_share_id_response",
    "FeedRefreshPublicShareIdResponse": ".feed_refresh_public_share_id_response",
    "FeedSendEventResponse": ".feed_send_event_response",
    "FeedStateAllResponseItem": ".feed_state_all_response_item",
    "FeedStateAllResponseItemStatus": ".feed_state_all_response_item_status",
    "FeedStateResolveResponse": ".feed_state_resolve_response",
    "FeedStateResolveResponseStatus": ".feed_state_resolve_response_status",
    "FeedStateUpsertResponse": ".feed_state_upsert_response",
    "FeedStateUpsertResponseStatus": ".feed_state_upsert_response_status",
    "FeedUpdateChannelInfoRequestNotifyFrequency": ".feed_update_channel_info_request_notify_frequency",
    "FeedUpdateChannelInfoResponse": ".feed_update_channel_info_response",
    "FeedUpdateChannelInfoResponseNotifyFrequency": ".feed_update_channel_info_response_notify_frequency",
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
