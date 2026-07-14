



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_topic_post_pm_response import CreateTopicPostPmResponse
    from .create_topic_post_pm_response_actions_summary_item import CreateTopicPostPmResponseActionsSummaryItem
    from .get_post_response import GetPostResponse
    from .get_post_response_actions_summary_item import GetPostResponseActionsSummaryItem
    from .list_posts_response import ListPostsResponse
    from .list_posts_response_latest_posts_item import ListPostsResponseLatestPostsItem
    from .list_posts_response_latest_posts_item_actions_summary_item import (
        ListPostsResponseLatestPostsItemActionsSummaryItem,
    )
    from .lock_post_response import LockPostResponse
    from .perform_post_action_response import PerformPostActionResponse
    from .perform_post_action_response_actions_summary_item import PerformPostActionResponseActionsSummaryItem
    from .post_replies_response_item import PostRepliesResponseItem
    from .post_replies_response_item_actions_summary_item import PostRepliesResponseItemActionsSummaryItem
    from .post_replies_response_item_reply_to_user import PostRepliesResponseItemReplyToUser
    from .update_post_request_post import UpdatePostRequestPost
    from .update_post_response import UpdatePostResponse
    from .update_post_response_post import UpdatePostResponsePost
    from .update_post_response_post_actions_summary_item import UpdatePostResponsePostActionsSummaryItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateTopicPostPmResponse": ".create_topic_post_pm_response",
    "CreateTopicPostPmResponseActionsSummaryItem": ".create_topic_post_pm_response_actions_summary_item",
    "GetPostResponse": ".get_post_response",
    "GetPostResponseActionsSummaryItem": ".get_post_response_actions_summary_item",
    "ListPostsResponse": ".list_posts_response",
    "ListPostsResponseLatestPostsItem": ".list_posts_response_latest_posts_item",
    "ListPostsResponseLatestPostsItemActionsSummaryItem": ".list_posts_response_latest_posts_item_actions_summary_item",
    "LockPostResponse": ".lock_post_response",
    "PerformPostActionResponse": ".perform_post_action_response",
    "PerformPostActionResponseActionsSummaryItem": ".perform_post_action_response_actions_summary_item",
    "PostRepliesResponseItem": ".post_replies_response_item",
    "PostRepliesResponseItemActionsSummaryItem": ".post_replies_response_item_actions_summary_item",
    "PostRepliesResponseItemReplyToUser": ".post_replies_response_item_reply_to_user",
    "UpdatePostRequestPost": ".update_post_request_post",
    "UpdatePostResponse": ".update_post_response",
    "UpdatePostResponsePost": ".update_post_response_post",
    "UpdatePostResponsePostActionsSummaryItem": ".update_post_response_post_actions_summary_item",
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
    "CreateTopicPostPmResponse",
    "CreateTopicPostPmResponseActionsSummaryItem",
    "GetPostResponse",
    "GetPostResponseActionsSummaryItem",
    "ListPostsResponse",
    "ListPostsResponseLatestPostsItem",
    "ListPostsResponseLatestPostsItemActionsSummaryItem",
    "LockPostResponse",
    "PerformPostActionResponse",
    "PerformPostActionResponseActionsSummaryItem",
    "PostRepliesResponseItem",
    "PostRepliesResponseItemActionsSummaryItem",
    "PostRepliesResponseItemReplyToUser",
    "UpdatePostRequestPost",
    "UpdatePostResponse",
    "UpdatePostResponsePost",
    "UpdatePostResponsePostActionsSummaryItem",
]
