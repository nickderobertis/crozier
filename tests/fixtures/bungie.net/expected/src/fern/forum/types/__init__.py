



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .forum_get_core_topics_paged_response import ForumGetCoreTopicsPagedResponse
    from .forum_get_forum_tag_suggestions_response import ForumGetForumTagSuggestionsResponse
    from .forum_get_poll_response import ForumGetPollResponse
    from .forum_get_post_and_parent_awaiting_approval_response import ForumGetPostAndParentAwaitingApprovalResponse
    from .forum_get_post_and_parent_response import ForumGetPostAndParentResponse
    from .forum_get_posts_threaded_paged_from_child_response import ForumGetPostsThreadedPagedFromChildResponse
    from .forum_get_posts_threaded_paged_response import ForumGetPostsThreadedPagedResponse
    from .forum_get_recruitment_thread_summaries_response import ForumGetRecruitmentThreadSummariesResponse
    from .forum_get_topic_for_content_response import ForumGetTopicForContentResponse
    from .forum_get_topics_paged_response import ForumGetTopicsPagedResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ForumGetCoreTopicsPagedResponse": ".forum_get_core_topics_paged_response",
    "ForumGetForumTagSuggestionsResponse": ".forum_get_forum_tag_suggestions_response",
    "ForumGetPollResponse": ".forum_get_poll_response",
    "ForumGetPostAndParentAwaitingApprovalResponse": ".forum_get_post_and_parent_awaiting_approval_response",
    "ForumGetPostAndParentResponse": ".forum_get_post_and_parent_response",
    "ForumGetPostsThreadedPagedFromChildResponse": ".forum_get_posts_threaded_paged_from_child_response",
    "ForumGetPostsThreadedPagedResponse": ".forum_get_posts_threaded_paged_response",
    "ForumGetRecruitmentThreadSummariesResponse": ".forum_get_recruitment_thread_summaries_response",
    "ForumGetTopicForContentResponse": ".forum_get_topic_for_content_response",
    "ForumGetTopicsPagedResponse": ".forum_get_topics_paged_response",
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
    "ForumGetCoreTopicsPagedResponse",
    "ForumGetForumTagSuggestionsResponse",
    "ForumGetPollResponse",
    "ForumGetPostAndParentAwaitingApprovalResponse",
    "ForumGetPostAndParentResponse",
    "ForumGetPostsThreadedPagedFromChildResponse",
    "ForumGetPostsThreadedPagedResponse",
    "ForumGetRecruitmentThreadSummariesResponse",
    "ForumGetTopicForContentResponse",
    "ForumGetTopicsPagedResponse",
]
