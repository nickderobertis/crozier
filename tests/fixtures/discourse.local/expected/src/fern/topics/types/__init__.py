



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_topic_timer_response import CreateTopicTimerResponse
    from .get_specific_posts_from_topic_response import GetSpecificPostsFromTopicResponse
    from .get_specific_posts_from_topic_response_post_stream import GetSpecificPostsFromTopicResponsePostStream
    from .get_specific_posts_from_topic_response_post_stream_posts_item import (
        GetSpecificPostsFromTopicResponsePostStreamPostsItem,
    )
    from .get_specific_posts_from_topic_response_post_stream_posts_item_actions_summary_item import (
        GetSpecificPostsFromTopicResponsePostStreamPostsItemActionsSummaryItem,
    )
    from .get_topic_response import GetTopicResponse
    from .get_topic_response_actions_summary_item import GetTopicResponseActionsSummaryItem
    from .get_topic_response_details import GetTopicResponseDetails
    from .get_topic_response_details_created_by import GetTopicResponseDetailsCreatedBy
    from .get_topic_response_details_last_poster import GetTopicResponseDetailsLastPoster
    from .get_topic_response_details_participants_item import GetTopicResponseDetailsParticipantsItem
    from .get_topic_response_post_stream import GetTopicResponsePostStream
    from .get_topic_response_post_stream_posts_item import GetTopicResponsePostStreamPostsItem
    from .get_topic_response_post_stream_posts_item_actions_summary_item import (
        GetTopicResponsePostStreamPostsItemActionsSummaryItem,
    )
    from .get_topic_response_post_stream_posts_item_link_counts_item import (
        GetTopicResponsePostStreamPostsItemLinkCountsItem,
    )
    from .get_topic_response_suggested_topics_item import GetTopicResponseSuggestedTopicsItem
    from .get_topic_response_suggested_topics_item_posters_item import GetTopicResponseSuggestedTopicsItemPostersItem
    from .get_topic_response_suggested_topics_item_posters_item_user import (
        GetTopicResponseSuggestedTopicsItemPostersItemUser,
    )
    from .get_topic_response_suggested_topics_item_tags_descriptions import (
        GetTopicResponseSuggestedTopicsItemTagsDescriptions,
    )
    from .get_topic_response_tags_descriptions import GetTopicResponseTagsDescriptions
    from .invite_to_topic_response import InviteToTopicResponse
    from .invite_to_topic_response_user import InviteToTopicResponseUser
    from .list_latest_topics_response import ListLatestTopicsResponse
    from .list_latest_topics_response_topic_list import ListLatestTopicsResponseTopicList
    from .list_latest_topics_response_topic_list_topics_item import ListLatestTopicsResponseTopicListTopicsItem
    from .list_latest_topics_response_topic_list_topics_item_posters_item import (
        ListLatestTopicsResponseTopicListTopicsItemPostersItem,
    )
    from .list_latest_topics_response_users_item import ListLatestTopicsResponseUsersItem
    from .list_top_topics_response import ListTopTopicsResponse
    from .list_top_topics_response_topic_list import ListTopTopicsResponseTopicList
    from .list_top_topics_response_topic_list_topics_item import ListTopTopicsResponseTopicListTopicsItem
    from .list_top_topics_response_topic_list_topics_item_posters_item import (
        ListTopTopicsResponseTopicListTopicsItemPostersItem,
    )
    from .list_top_topics_response_users_item import ListTopTopicsResponseUsersItem
    from .set_notification_level_request_notification_level import SetNotificationLevelRequestNotificationLevel
    from .set_notification_level_response import SetNotificationLevelResponse
    from .update_topic_request_topic import UpdateTopicRequestTopic
    from .update_topic_response import UpdateTopicResponse
    from .update_topic_response_basic_topic import UpdateTopicResponseBasicTopic
    from .update_topic_status_request_enabled import UpdateTopicStatusRequestEnabled
    from .update_topic_status_request_status import UpdateTopicStatusRequestStatus
    from .update_topic_status_response import UpdateTopicStatusResponse
    from .update_topic_timestamp_response import UpdateTopicTimestampResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateTopicTimerResponse": ".create_topic_timer_response",
    "GetSpecificPostsFromTopicResponse": ".get_specific_posts_from_topic_response",
    "GetSpecificPostsFromTopicResponsePostStream": ".get_specific_posts_from_topic_response_post_stream",
    "GetSpecificPostsFromTopicResponsePostStreamPostsItem": ".get_specific_posts_from_topic_response_post_stream_posts_item",
    "GetSpecificPostsFromTopicResponsePostStreamPostsItemActionsSummaryItem": ".get_specific_posts_from_topic_response_post_stream_posts_item_actions_summary_item",
    "GetTopicResponse": ".get_topic_response",
    "GetTopicResponseActionsSummaryItem": ".get_topic_response_actions_summary_item",
    "GetTopicResponseDetails": ".get_topic_response_details",
    "GetTopicResponseDetailsCreatedBy": ".get_topic_response_details_created_by",
    "GetTopicResponseDetailsLastPoster": ".get_topic_response_details_last_poster",
    "GetTopicResponseDetailsParticipantsItem": ".get_topic_response_details_participants_item",
    "GetTopicResponsePostStream": ".get_topic_response_post_stream",
    "GetTopicResponsePostStreamPostsItem": ".get_topic_response_post_stream_posts_item",
    "GetTopicResponsePostStreamPostsItemActionsSummaryItem": ".get_topic_response_post_stream_posts_item_actions_summary_item",
    "GetTopicResponsePostStreamPostsItemLinkCountsItem": ".get_topic_response_post_stream_posts_item_link_counts_item",
    "GetTopicResponseSuggestedTopicsItem": ".get_topic_response_suggested_topics_item",
    "GetTopicResponseSuggestedTopicsItemPostersItem": ".get_topic_response_suggested_topics_item_posters_item",
    "GetTopicResponseSuggestedTopicsItemPostersItemUser": ".get_topic_response_suggested_topics_item_posters_item_user",
    "GetTopicResponseSuggestedTopicsItemTagsDescriptions": ".get_topic_response_suggested_topics_item_tags_descriptions",
    "GetTopicResponseTagsDescriptions": ".get_topic_response_tags_descriptions",
    "InviteToTopicResponse": ".invite_to_topic_response",
    "InviteToTopicResponseUser": ".invite_to_topic_response_user",
    "ListLatestTopicsResponse": ".list_latest_topics_response",
    "ListLatestTopicsResponseTopicList": ".list_latest_topics_response_topic_list",
    "ListLatestTopicsResponseTopicListTopicsItem": ".list_latest_topics_response_topic_list_topics_item",
    "ListLatestTopicsResponseTopicListTopicsItemPostersItem": ".list_latest_topics_response_topic_list_topics_item_posters_item",
    "ListLatestTopicsResponseUsersItem": ".list_latest_topics_response_users_item",
    "ListTopTopicsResponse": ".list_top_topics_response",
    "ListTopTopicsResponseTopicList": ".list_top_topics_response_topic_list",
    "ListTopTopicsResponseTopicListTopicsItem": ".list_top_topics_response_topic_list_topics_item",
    "ListTopTopicsResponseTopicListTopicsItemPostersItem": ".list_top_topics_response_topic_list_topics_item_posters_item",
    "ListTopTopicsResponseUsersItem": ".list_top_topics_response_users_item",
    "SetNotificationLevelRequestNotificationLevel": ".set_notification_level_request_notification_level",
    "SetNotificationLevelResponse": ".set_notification_level_response",
    "UpdateTopicRequestTopic": ".update_topic_request_topic",
    "UpdateTopicResponse": ".update_topic_response",
    "UpdateTopicResponseBasicTopic": ".update_topic_response_basic_topic",
    "UpdateTopicStatusRequestEnabled": ".update_topic_status_request_enabled",
    "UpdateTopicStatusRequestStatus": ".update_topic_status_request_status",
    "UpdateTopicStatusResponse": ".update_topic_status_response",
    "UpdateTopicTimestampResponse": ".update_topic_timestamp_response",
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
    "CreateTopicTimerResponse",
    "GetSpecificPostsFromTopicResponse",
    "GetSpecificPostsFromTopicResponsePostStream",
    "GetSpecificPostsFromTopicResponsePostStreamPostsItem",
    "GetSpecificPostsFromTopicResponsePostStreamPostsItemActionsSummaryItem",
    "GetTopicResponse",
    "GetTopicResponseActionsSummaryItem",
    "GetTopicResponseDetails",
    "GetTopicResponseDetailsCreatedBy",
    "GetTopicResponseDetailsLastPoster",
    "GetTopicResponseDetailsParticipantsItem",
    "GetTopicResponsePostStream",
    "GetTopicResponsePostStreamPostsItem",
    "GetTopicResponsePostStreamPostsItemActionsSummaryItem",
    "GetTopicResponsePostStreamPostsItemLinkCountsItem",
    "GetTopicResponseSuggestedTopicsItem",
    "GetTopicResponseSuggestedTopicsItemPostersItem",
    "GetTopicResponseSuggestedTopicsItemPostersItemUser",
    "GetTopicResponseSuggestedTopicsItemTagsDescriptions",
    "GetTopicResponseTagsDescriptions",
    "InviteToTopicResponse",
    "InviteToTopicResponseUser",
    "ListLatestTopicsResponse",
    "ListLatestTopicsResponseTopicList",
    "ListLatestTopicsResponseTopicListTopicsItem",
    "ListLatestTopicsResponseTopicListTopicsItemPostersItem",
    "ListLatestTopicsResponseUsersItem",
    "ListTopTopicsResponse",
    "ListTopTopicsResponseTopicList",
    "ListTopTopicsResponseTopicListTopicsItem",
    "ListTopTopicsResponseTopicListTopicsItemPostersItem",
    "ListTopTopicsResponseUsersItem",
    "SetNotificationLevelRequestNotificationLevel",
    "SetNotificationLevelResponse",
    "UpdateTopicRequestTopic",
    "UpdateTopicResponse",
    "UpdateTopicResponseBasicTopic",
    "UpdateTopicStatusRequestEnabled",
    "UpdateTopicStatusRequestStatus",
    "UpdateTopicStatusResponse",
    "UpdateTopicTimestampResponse",
]
