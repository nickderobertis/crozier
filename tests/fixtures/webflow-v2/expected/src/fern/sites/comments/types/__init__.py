



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_comment_reply_comments_response import CreateCommentReplyCommentsResponse
    from .create_comment_reply_comments_response_author import CreateCommentReplyCommentsResponseAuthor
    from .create_comment_reply_comments_response_mentioned_users_item import (
        CreateCommentReplyCommentsResponseMentionedUsersItem,
    )
    from .get_comment_thread_comments_request_sort_by import GetCommentThreadCommentsRequestSortBy
    from .get_comment_thread_comments_request_sort_order import GetCommentThreadCommentsRequestSortOrder
    from .get_comment_thread_comments_response import GetCommentThreadCommentsResponse
    from .get_comment_thread_comments_response_author import GetCommentThreadCommentsResponseAuthor
    from .get_comment_thread_comments_response_mentioned_users_item import (
        GetCommentThreadCommentsResponseMentionedUsersItem,
    )
    from .list_comment_replies_comments_request_sort_by import ListCommentRepliesCommentsRequestSortBy
    from .list_comment_replies_comments_request_sort_order import ListCommentRepliesCommentsRequestSortOrder
    from .list_comment_replies_comments_response import ListCommentRepliesCommentsResponse
    from .list_comment_replies_comments_response_comments_item import ListCommentRepliesCommentsResponseCommentsItem
    from .list_comment_replies_comments_response_comments_item_author import (
        ListCommentRepliesCommentsResponseCommentsItemAuthor,
    )
    from .list_comment_replies_comments_response_comments_item_mentioned_users_item import (
        ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem,
    )
    from .list_comment_replies_comments_response_pagination import ListCommentRepliesCommentsResponsePagination
    from .list_comment_threads_comments_request_sort_by import ListCommentThreadsCommentsRequestSortBy
    from .list_comment_threads_comments_request_sort_order import ListCommentThreadsCommentsRequestSortOrder
    from .list_comment_threads_comments_response import ListCommentThreadsCommentsResponse
    from .list_comment_threads_comments_response_comments_item import ListCommentThreadsCommentsResponseCommentsItem
    from .list_comment_threads_comments_response_comments_item_author import (
        ListCommentThreadsCommentsResponseCommentsItemAuthor,
    )
    from .list_comment_threads_comments_response_comments_item_mentioned_users_item import (
        ListCommentThreadsCommentsResponseCommentsItemMentionedUsersItem,
    )
    from .list_comment_threads_comments_response_pagination import ListCommentThreadsCommentsResponsePagination
    from .resolve_comment_thread_comments_response import ResolveCommentThreadCommentsResponse
    from .resolve_comment_thread_comments_response_author import ResolveCommentThreadCommentsResponseAuthor
    from .resolve_comment_thread_comments_response_mentioned_users_item import (
        ResolveCommentThreadCommentsResponseMentionedUsersItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCommentReplyCommentsResponse": ".create_comment_reply_comments_response",
    "CreateCommentReplyCommentsResponseAuthor": ".create_comment_reply_comments_response_author",
    "CreateCommentReplyCommentsResponseMentionedUsersItem": ".create_comment_reply_comments_response_mentioned_users_item",
    "GetCommentThreadCommentsRequestSortBy": ".get_comment_thread_comments_request_sort_by",
    "GetCommentThreadCommentsRequestSortOrder": ".get_comment_thread_comments_request_sort_order",
    "GetCommentThreadCommentsResponse": ".get_comment_thread_comments_response",
    "GetCommentThreadCommentsResponseAuthor": ".get_comment_thread_comments_response_author",
    "GetCommentThreadCommentsResponseMentionedUsersItem": ".get_comment_thread_comments_response_mentioned_users_item",
    "ListCommentRepliesCommentsRequestSortBy": ".list_comment_replies_comments_request_sort_by",
    "ListCommentRepliesCommentsRequestSortOrder": ".list_comment_replies_comments_request_sort_order",
    "ListCommentRepliesCommentsResponse": ".list_comment_replies_comments_response",
    "ListCommentRepliesCommentsResponseCommentsItem": ".list_comment_replies_comments_response_comments_item",
    "ListCommentRepliesCommentsResponseCommentsItemAuthor": ".list_comment_replies_comments_response_comments_item_author",
    "ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem": ".list_comment_replies_comments_response_comments_item_mentioned_users_item",
    "ListCommentRepliesCommentsResponsePagination": ".list_comment_replies_comments_response_pagination",
    "ListCommentThreadsCommentsRequestSortBy": ".list_comment_threads_comments_request_sort_by",
    "ListCommentThreadsCommentsRequestSortOrder": ".list_comment_threads_comments_request_sort_order",
    "ListCommentThreadsCommentsResponse": ".list_comment_threads_comments_response",
    "ListCommentThreadsCommentsResponseCommentsItem": ".list_comment_threads_comments_response_comments_item",
    "ListCommentThreadsCommentsResponseCommentsItemAuthor": ".list_comment_threads_comments_response_comments_item_author",
    "ListCommentThreadsCommentsResponseCommentsItemMentionedUsersItem": ".list_comment_threads_comments_response_comments_item_mentioned_users_item",
    "ListCommentThreadsCommentsResponsePagination": ".list_comment_threads_comments_response_pagination",
    "ResolveCommentThreadCommentsResponse": ".resolve_comment_thread_comments_response",
    "ResolveCommentThreadCommentsResponseAuthor": ".resolve_comment_thread_comments_response_author",
    "ResolveCommentThreadCommentsResponseMentionedUsersItem": ".resolve_comment_thread_comments_response_mentioned_users_item",
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
    "CreateCommentReplyCommentsResponse",
    "CreateCommentReplyCommentsResponseAuthor",
    "CreateCommentReplyCommentsResponseMentionedUsersItem",
    "GetCommentThreadCommentsRequestSortBy",
    "GetCommentThreadCommentsRequestSortOrder",
    "GetCommentThreadCommentsResponse",
    "GetCommentThreadCommentsResponseAuthor",
    "GetCommentThreadCommentsResponseMentionedUsersItem",
    "ListCommentRepliesCommentsRequestSortBy",
    "ListCommentRepliesCommentsRequestSortOrder",
    "ListCommentRepliesCommentsResponse",
    "ListCommentRepliesCommentsResponseCommentsItem",
    "ListCommentRepliesCommentsResponseCommentsItemAuthor",
    "ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem",
    "ListCommentRepliesCommentsResponsePagination",
    "ListCommentThreadsCommentsRequestSortBy",
    "ListCommentThreadsCommentsRequestSortOrder",
    "ListCommentThreadsCommentsResponse",
    "ListCommentThreadsCommentsResponseCommentsItem",
    "ListCommentThreadsCommentsResponseCommentsItemAuthor",
    "ListCommentThreadsCommentsResponseCommentsItemMentionedUsersItem",
    "ListCommentThreadsCommentsResponsePagination",
    "ResolveCommentThreadCommentsResponse",
    "ResolveCommentThreadCommentsResponseAuthor",
    "ResolveCommentThreadCommentsResponseMentionedUsersItem",
]
