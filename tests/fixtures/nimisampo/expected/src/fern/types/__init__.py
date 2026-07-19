



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_full_text_search_response import GetFullTextSearchResponse
    from .post_faceted_search_facet_class_facet_id_response import PostFacetedSearchFacetClassFacetIdResponse
    from .post_faceted_search_facet_class_facet_id_response_data import PostFacetedSearchFacetClassFacetIdResponseData
    from .post_faceted_search_result_class_count_response import PostFacetedSearchResultClassCountResponse
    from .post_faceted_search_result_class_paginated_response import PostFacetedSearchResultClassPaginatedResponse
    from .post_result_class_page_uri_response import PostResultClassPageUriResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetFullTextSearchResponse": ".get_full_text_search_response",
    "PostFacetedSearchFacetClassFacetIdResponse": ".post_faceted_search_facet_class_facet_id_response",
    "PostFacetedSearchFacetClassFacetIdResponseData": ".post_faceted_search_facet_class_facet_id_response_data",
    "PostFacetedSearchResultClassCountResponse": ".post_faceted_search_result_class_count_response",
    "PostFacetedSearchResultClassPaginatedResponse": ".post_faceted_search_result_class_paginated_response",
    "PostResultClassPageUriResponse": ".post_result_class_page_uri_response",
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
    "GetFullTextSearchResponse",
    "PostFacetedSearchFacetClassFacetIdResponse",
    "PostFacetedSearchFacetClassFacetIdResponseData",
    "PostFacetedSearchResultClassCountResponse",
    "PostFacetedSearchResultClassPaginatedResponse",
    "PostResultClassPageUriResponse",
]
