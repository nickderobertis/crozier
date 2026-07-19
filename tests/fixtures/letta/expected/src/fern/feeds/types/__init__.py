



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .feeds_backfill_subscription_response import FeedsBackfillSubscriptionResponse
    from .feeds_create_feed_response import FeedsCreateFeedResponse
    from .feeds_delete_feed_request_body import FeedsDeleteFeedRequestBody
    from .feeds_delete_feed_response import FeedsDeleteFeedResponse
    from .feeds_delete_subscription_request_body import FeedsDeleteSubscriptionRequestBody
    from .feeds_delete_subscription_response import FeedsDeleteSubscriptionResponse
    from .feeds_get_feed_response import FeedsGetFeedResponse
    from .feeds_get_message_response import FeedsGetMessageResponse
    from .feeds_get_message_response_message import FeedsGetMessageResponseMessage
    from .feeds_list_feeds_response import FeedsListFeedsResponse
    from .feeds_list_feeds_response_feeds_item import FeedsListFeedsResponseFeedsItem
    from .feeds_list_messages_response import FeedsListMessagesResponse
    from .feeds_list_messages_response_messages_item import FeedsListMessagesResponseMessagesItem
    from .feeds_list_subscription_history_response import FeedsListSubscriptionHistoryResponse
    from .feeds_list_subscription_history_response_runs_item import FeedsListSubscriptionHistoryResponseRunsItem
    from .feeds_list_subscription_history_response_runs_item_status import (
        FeedsListSubscriptionHistoryResponseRunsItemStatus,
    )
    from .feeds_list_subscription_history_response_runs_item_type import (
        FeedsListSubscriptionHistoryResponseRunsItemType,
    )
    from .feeds_list_subscriptions_response import FeedsListSubscriptionsResponse
    from .feeds_list_subscriptions_response_subscriptions_item import FeedsListSubscriptionsResponseSubscriptionsItem
    from .feeds_list_subscriptions_response_subscriptions_item_merge_strategy import (
        FeedsListSubscriptionsResponseSubscriptionsItemMergeStrategy,
    )
    from .feeds_publish_messages_request_messages_item import FeedsPublishMessagesRequestMessagesItem
    from .feeds_publish_messages_response import FeedsPublishMessagesResponse
    from .feeds_subscribe_agent_response import FeedsSubscribeAgentResponse
    from .feeds_subscribe_agent_response_merge_strategy import FeedsSubscribeAgentResponseMergeStrategy
    from .feeds_trigger_subscription_response import FeedsTriggerSubscriptionResponse
    from .feeds_unsubscribe_agent_response import FeedsUnsubscribeAgentResponse
    from .feeds_update_all_subscriptions_cron_response import FeedsUpdateAllSubscriptionsCronResponse
    from .feeds_update_subscription_response import FeedsUpdateSubscriptionResponse
    from .feeds_update_subscription_response_merge_strategy import FeedsUpdateSubscriptionResponseMergeStrategy
_dynamic_imports: typing.Dict[str, str] = {
    "FeedsBackfillSubscriptionResponse": ".feeds_backfill_subscription_response",
    "FeedsCreateFeedResponse": ".feeds_create_feed_response",
    "FeedsDeleteFeedRequestBody": ".feeds_delete_feed_request_body",
    "FeedsDeleteFeedResponse": ".feeds_delete_feed_response",
    "FeedsDeleteSubscriptionRequestBody": ".feeds_delete_subscription_request_body",
    "FeedsDeleteSubscriptionResponse": ".feeds_delete_subscription_response",
    "FeedsGetFeedResponse": ".feeds_get_feed_response",
    "FeedsGetMessageResponse": ".feeds_get_message_response",
    "FeedsGetMessageResponseMessage": ".feeds_get_message_response_message",
    "FeedsListFeedsResponse": ".feeds_list_feeds_response",
    "FeedsListFeedsResponseFeedsItem": ".feeds_list_feeds_response_feeds_item",
    "FeedsListMessagesResponse": ".feeds_list_messages_response",
    "FeedsListMessagesResponseMessagesItem": ".feeds_list_messages_response_messages_item",
    "FeedsListSubscriptionHistoryResponse": ".feeds_list_subscription_history_response",
    "FeedsListSubscriptionHistoryResponseRunsItem": ".feeds_list_subscription_history_response_runs_item",
    "FeedsListSubscriptionHistoryResponseRunsItemStatus": ".feeds_list_subscription_history_response_runs_item_status",
    "FeedsListSubscriptionHistoryResponseRunsItemType": ".feeds_list_subscription_history_response_runs_item_type",
    "FeedsListSubscriptionsResponse": ".feeds_list_subscriptions_response",
    "FeedsListSubscriptionsResponseSubscriptionsItem": ".feeds_list_subscriptions_response_subscriptions_item",
    "FeedsListSubscriptionsResponseSubscriptionsItemMergeStrategy": ".feeds_list_subscriptions_response_subscriptions_item_merge_strategy",
    "FeedsPublishMessagesRequestMessagesItem": ".feeds_publish_messages_request_messages_item",
    "FeedsPublishMessagesResponse": ".feeds_publish_messages_response",
    "FeedsSubscribeAgentResponse": ".feeds_subscribe_agent_response",
    "FeedsSubscribeAgentResponseMergeStrategy": ".feeds_subscribe_agent_response_merge_strategy",
    "FeedsTriggerSubscriptionResponse": ".feeds_trigger_subscription_response",
    "FeedsUnsubscribeAgentResponse": ".feeds_unsubscribe_agent_response",
    "FeedsUpdateAllSubscriptionsCronResponse": ".feeds_update_all_subscriptions_cron_response",
    "FeedsUpdateSubscriptionResponse": ".feeds_update_subscription_response",
    "FeedsUpdateSubscriptionResponseMergeStrategy": ".feeds_update_subscription_response_merge_strategy",
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
    "FeedsBackfillSubscriptionResponse",
    "FeedsCreateFeedResponse",
    "FeedsDeleteFeedRequestBody",
    "FeedsDeleteFeedResponse",
    "FeedsDeleteSubscriptionRequestBody",
    "FeedsDeleteSubscriptionResponse",
    "FeedsGetFeedResponse",
    "FeedsGetMessageResponse",
    "FeedsGetMessageResponseMessage",
    "FeedsListFeedsResponse",
    "FeedsListFeedsResponseFeedsItem",
    "FeedsListMessagesResponse",
    "FeedsListMessagesResponseMessagesItem",
    "FeedsListSubscriptionHistoryResponse",
    "FeedsListSubscriptionHistoryResponseRunsItem",
    "FeedsListSubscriptionHistoryResponseRunsItemStatus",
    "FeedsListSubscriptionHistoryResponseRunsItemType",
    "FeedsListSubscriptionsResponse",
    "FeedsListSubscriptionsResponseSubscriptionsItem",
    "FeedsListSubscriptionsResponseSubscriptionsItemMergeStrategy",
    "FeedsPublishMessagesRequestMessagesItem",
    "FeedsPublishMessagesResponse",
    "FeedsSubscribeAgentResponse",
    "FeedsSubscribeAgentResponseMergeStrategy",
    "FeedsTriggerSubscriptionResponse",
    "FeedsUnsubscribeAgentResponse",
    "FeedsUpdateAllSubscriptionsCronResponse",
    "FeedsUpdateSubscriptionResponse",
    "FeedsUpdateSubscriptionResponseMergeStrategy",
]
