



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateCommentReplyCommentsResponse,
        CreateCommentReplyCommentsResponseAuthor,
        CreateCommentReplyCommentsResponseMentionedUsersItem,
        GetCommentThreadCommentsRequestSortBy,
        GetCommentThreadCommentsRequestSortOrder,
        GetCommentThreadCommentsResponse,
        GetCommentThreadCommentsResponseAuthor,
        GetCommentThreadCommentsResponseMentionedUsersItem,
        ListCommentRepliesCommentsRequestSortBy,
        ListCommentRepliesCommentsRequestSortOrder,
        ListCommentRepliesCommentsResponse,
        ListCommentRepliesCommentsResponseCommentsItem,
        ListCommentRepliesCommentsResponseCommentsItemAuthor,
        ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem,
        ListCommentRepliesCommentsResponsePagination,
        ListCommentThreadsCommentsRequestSortBy,
        ListCommentThreadsCommentsRequestSortOrder,
        ListCommentThreadsCommentsResponse,
        ListCommentThreadsCommentsResponseCommentsItem,
        ListCommentThreadsCommentsResponseCommentsItemAuthor,
        ListCommentThreadsCommentsResponseCommentsItemMentionedUsersItem,
        ListCommentThreadsCommentsResponsePagination,
        ResolveCommentThreadCommentsResponse,
        ResolveCommentThreadCommentsResponseAuthor,
        ResolveCommentThreadCommentsResponseMentionedUsersItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCommentReplyCommentsResponse": ".types",
    "CreateCommentReplyCommentsResponseAuthor": ".types",
    "CreateCommentReplyCommentsResponseMentionedUsersItem": ".types",
    "GetCommentThreadCommentsRequestSortBy": ".types",
    "GetCommentThreadCommentsRequestSortOrder": ".types",
    "GetCommentThreadCommentsResponse": ".types",
    "GetCommentThreadCommentsResponseAuthor": ".types",
    "GetCommentThreadCommentsResponseMentionedUsersItem": ".types",
    "ListCommentRepliesCommentsRequestSortBy": ".types",
    "ListCommentRepliesCommentsRequestSortOrder": ".types",
    "ListCommentRepliesCommentsResponse": ".types",
    "ListCommentRepliesCommentsResponseCommentsItem": ".types",
    "ListCommentRepliesCommentsResponseCommentsItemAuthor": ".types",
    "ListCommentRepliesCommentsResponseCommentsItemMentionedUsersItem": ".types",
    "ListCommentRepliesCommentsResponsePagination": ".types",
    "ListCommentThreadsCommentsRequestSortBy": ".types",
    "ListCommentThreadsCommentsRequestSortOrder": ".types",
    "ListCommentThreadsCommentsResponse": ".types",
    "ListCommentThreadsCommentsResponseCommentsItem": ".types",
    "ListCommentThreadsCommentsResponseCommentsItemAuthor": ".types",
    "ListCommentThreadsCommentsResponseCommentsItemMentionedUsersItem": ".types",
    "ListCommentThreadsCommentsResponsePagination": ".types",
    "ResolveCommentThreadCommentsResponse": ".types",
    "ResolveCommentThreadCommentsResponseAuthor": ".types",
    "ResolveCommentThreadCommentsResponseMentionedUsersItem": ".types",
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
