



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_tags_search_request import PostTagsSearchRequest
    from .post_tags_search_request_target import PostTagsSearchRequestTarget
    from .post_tags_search_request_target_entity import PostTagsSearchRequestTargetEntity
    from .post_tags_search_request_targets import PostTagsSearchRequestTargets
    from .post_tags_search_request_targets_entity import PostTagsSearchRequestTargetsEntity
    from .post_tags_search_response import PostTagsSearchResponse
    from .post_tags_synchronization_request_entity import PostTagsSynchronizationRequestEntity
_dynamic_imports: typing.Dict[str, str] = {
    "PostTagsSearchRequest": ".post_tags_search_request",
    "PostTagsSearchRequestTarget": ".post_tags_search_request_target",
    "PostTagsSearchRequestTargetEntity": ".post_tags_search_request_target_entity",
    "PostTagsSearchRequestTargets": ".post_tags_search_request_targets",
    "PostTagsSearchRequestTargetsEntity": ".post_tags_search_request_targets_entity",
    "PostTagsSearchResponse": ".post_tags_search_response",
    "PostTagsSynchronizationRequestEntity": ".post_tags_synchronization_request_entity",
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
    "PostTagsSearchRequest",
    "PostTagsSearchRequestTarget",
    "PostTagsSearchRequestTargetEntity",
    "PostTagsSearchRequestTargets",
    "PostTagsSearchRequestTargetsEntity",
    "PostTagsSearchResponse",
    "PostTagsSynchronizationRequestEntity",
]
