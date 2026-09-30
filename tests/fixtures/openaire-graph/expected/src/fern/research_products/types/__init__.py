



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .search1request_best_open_access_right_label_item import Search1RequestBestOpenAccessRightLabelItem
    from .search1request_citation_count_class_item import Search1RequestCitationCountClassItem
    from .search1request_impulse_class_item import Search1RequestImpulseClassItem
    from .search1request_influence_class_item import Search1RequestInfluenceClassItem
    from .search1request_logical_operator import Search1RequestLogicalOperator
    from .search1request_open_access_color_item import Search1RequestOpenAccessColorItem
    from .search1request_popularity_class_item import Search1RequestPopularityClassItem
    from .search1request_type_item import Search1RequestTypeItem
    from .search_request_best_open_access_right_label_item import SearchRequestBestOpenAccessRightLabelItem
    from .search_request_citation_count_class_item import SearchRequestCitationCountClassItem
    from .search_request_impulse_class_item import SearchRequestImpulseClassItem
    from .search_request_influence_class_item import SearchRequestInfluenceClassItem
    from .search_request_logical_operator import SearchRequestLogicalOperator
    from .search_request_open_access_color_item import SearchRequestOpenAccessColorItem
    from .search_request_popularity_class_item import SearchRequestPopularityClassItem
    from .search_request_type_item import SearchRequestTypeItem
_dynamic_imports: typing.Dict[str, str] = {
    "Search1RequestBestOpenAccessRightLabelItem": ".search1request_best_open_access_right_label_item",
    "Search1RequestCitationCountClassItem": ".search1request_citation_count_class_item",
    "Search1RequestImpulseClassItem": ".search1request_impulse_class_item",
    "Search1RequestInfluenceClassItem": ".search1request_influence_class_item",
    "Search1RequestLogicalOperator": ".search1request_logical_operator",
    "Search1RequestOpenAccessColorItem": ".search1request_open_access_color_item",
    "Search1RequestPopularityClassItem": ".search1request_popularity_class_item",
    "Search1RequestTypeItem": ".search1request_type_item",
    "SearchRequestBestOpenAccessRightLabelItem": ".search_request_best_open_access_right_label_item",
    "SearchRequestCitationCountClassItem": ".search_request_citation_count_class_item",
    "SearchRequestImpulseClassItem": ".search_request_impulse_class_item",
    "SearchRequestInfluenceClassItem": ".search_request_influence_class_item",
    "SearchRequestLogicalOperator": ".search_request_logical_operator",
    "SearchRequestOpenAccessColorItem": ".search_request_open_access_color_item",
    "SearchRequestPopularityClassItem": ".search_request_popularity_class_item",
    "SearchRequestTypeItem": ".search_request_type_item",
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
    "Search1RequestBestOpenAccessRightLabelItem",
    "Search1RequestCitationCountClassItem",
    "Search1RequestImpulseClassItem",
    "Search1RequestInfluenceClassItem",
    "Search1RequestLogicalOperator",
    "Search1RequestOpenAccessColorItem",
    "Search1RequestPopularityClassItem",
    "Search1RequestTypeItem",
    "SearchRequestBestOpenAccessRightLabelItem",
    "SearchRequestCitationCountClassItem",
    "SearchRequestImpulseClassItem",
    "SearchRequestInfluenceClassItem",
    "SearchRequestLogicalOperator",
    "SearchRequestOpenAccessColorItem",
    "SearchRequestPopularityClassItem",
    "SearchRequestTypeItem",
]
