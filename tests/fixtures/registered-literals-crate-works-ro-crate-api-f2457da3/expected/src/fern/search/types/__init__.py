



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .search_entities_request_bounding_box import SearchEntitiesRequestBoundingBox
    from .search_entities_request_bounding_box_bottom_left import SearchEntitiesRequestBoundingBoxBottomLeft
    from .search_entities_request_bounding_box_top_right import SearchEntitiesRequestBoundingBoxTopRight
    from .search_entities_request_filters_value import SearchEntitiesRequestFiltersValue
    from .search_entities_request_search_type import SearchEntitiesRequestSearchType
    from .search_entities_request_sort import SearchEntitiesRequestSort
    from .search_entities_response import SearchEntitiesResponse
    from .search_entities_response_entities_item import SearchEntitiesResponseEntitiesItem
    from .search_entities_response_facets_value_item import SearchEntitiesResponseFacetsValueItem
_dynamic_imports: typing.Dict[str, str] = {
    "SearchEntitiesRequestBoundingBox": ".search_entities_request_bounding_box",
    "SearchEntitiesRequestBoundingBoxBottomLeft": ".search_entities_request_bounding_box_bottom_left",
    "SearchEntitiesRequestBoundingBoxTopRight": ".search_entities_request_bounding_box_top_right",
    "SearchEntitiesRequestFiltersValue": ".search_entities_request_filters_value",
    "SearchEntitiesRequestSearchType": ".search_entities_request_search_type",
    "SearchEntitiesRequestSort": ".search_entities_request_sort",
    "SearchEntitiesResponse": ".search_entities_response",
    "SearchEntitiesResponseEntitiesItem": ".search_entities_response_entities_item",
    "SearchEntitiesResponseFacetsValueItem": ".search_entities_response_facets_value_item",
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
    "SearchEntitiesRequestBoundingBox",
    "SearchEntitiesRequestBoundingBoxBottomLeft",
    "SearchEntitiesRequestBoundingBoxTopRight",
    "SearchEntitiesRequestFiltersValue",
    "SearchEntitiesRequestSearchType",
    "SearchEntitiesRequestSort",
    "SearchEntitiesResponse",
    "SearchEntitiesResponseEntitiesItem",
    "SearchEntitiesResponseFacetsValueItem",
]
