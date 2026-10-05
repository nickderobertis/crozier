



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ancestor_filter_search_term import AncestorFilterSearchTerm
    from .child_filter_search_term import ChildFilterSearchTerm
    from .descendant_filter_search_term import DescendantFilterSearchTerm
    from .entry_node import EntryNode
    from .entry_node_search_result import EntryNodeSearchResult
    from .entry_node_search_result_filters_item import (
        EntryNodeSearchResultFiltersItem,
        EntryNodeSearchResultFiltersItem_Ancestor,
        EntryNodeSearchResultFiltersItem_Child,
        EntryNodeSearchResultFiltersItem_Descendant,
        EntryNodeSearchResultFiltersItem_Is,
        EntryNodeSearchResultFiltersItem_Language,
        EntryNodeSearchResultFiltersItem_Parent,
        EntryNodeSearchResultFiltersItem_Property,
    )
    from .error_node import ErrorNode
    from .http_validation_error import HttpValidationError
    from .is_filter_search_term import IsFilterSearchTerm
    from .is_filter_search_term_filter_value import IsFilterSearchTermFilterValue
    from .is_filter_search_term_filter_value_four import IsFilterSearchTermFilterValueFour
    from .is_filter_search_term_filter_value_one import IsFilterSearchTermFilterValueOne
    from .is_filter_search_term_filter_value_three import IsFilterSearchTermFilterValueThree
    from .is_filter_search_term_filter_value_two import IsFilterSearchTermFilterValueTwo
    from .is_filter_search_term_filter_value_zero import IsFilterSearchTermFilterValueZero
    from .language_filter_search_term import LanguageFilterSearchTerm
    from .parent_filter_search_term import ParentFilterSearchTerm
    from .project import Project
    from .project_status import ProjectStatus
    from .property_filter_search_term import PropertyFilterSearchTerm
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "AncestorFilterSearchTerm": ".ancestor_filter_search_term",
    "ChildFilterSearchTerm": ".child_filter_search_term",
    "DescendantFilterSearchTerm": ".descendant_filter_search_term",
    "EntryNode": ".entry_node",
    "EntryNodeSearchResult": ".entry_node_search_result",
    "EntryNodeSearchResultFiltersItem": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Ancestor": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Child": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Descendant": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Is": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Language": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Parent": ".entry_node_search_result_filters_item",
    "EntryNodeSearchResultFiltersItem_Property": ".entry_node_search_result_filters_item",
    "ErrorNode": ".error_node",
    "HttpValidationError": ".http_validation_error",
    "IsFilterSearchTerm": ".is_filter_search_term",
    "IsFilterSearchTermFilterValue": ".is_filter_search_term_filter_value",
    "IsFilterSearchTermFilterValueFour": ".is_filter_search_term_filter_value_four",
    "IsFilterSearchTermFilterValueOne": ".is_filter_search_term_filter_value_one",
    "IsFilterSearchTermFilterValueThree": ".is_filter_search_term_filter_value_three",
    "IsFilterSearchTermFilterValueTwo": ".is_filter_search_term_filter_value_two",
    "IsFilterSearchTermFilterValueZero": ".is_filter_search_term_filter_value_zero",
    "LanguageFilterSearchTerm": ".language_filter_search_term",
    "ParentFilterSearchTerm": ".parent_filter_search_term",
    "Project": ".project",
    "ProjectStatus": ".project_status",
    "PropertyFilterSearchTerm": ".property_filter_search_term",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "AncestorFilterSearchTerm",
    "ChildFilterSearchTerm",
    "DescendantFilterSearchTerm",
    "EntryNode",
    "EntryNodeSearchResult",
    "EntryNodeSearchResultFiltersItem",
    "EntryNodeSearchResultFiltersItem_Ancestor",
    "EntryNodeSearchResultFiltersItem_Child",
    "EntryNodeSearchResultFiltersItem_Descendant",
    "EntryNodeSearchResultFiltersItem_Is",
    "EntryNodeSearchResultFiltersItem_Language",
    "EntryNodeSearchResultFiltersItem_Parent",
    "EntryNodeSearchResultFiltersItem_Property",
    "ErrorNode",
    "HttpValidationError",
    "IsFilterSearchTerm",
    "IsFilterSearchTermFilterValue",
    "IsFilterSearchTermFilterValueFour",
    "IsFilterSearchTermFilterValueOne",
    "IsFilterSearchTermFilterValueThree",
    "IsFilterSearchTermFilterValueTwo",
    "IsFilterSearchTermFilterValueZero",
    "LanguageFilterSearchTerm",
    "ParentFilterSearchTerm",
    "Project",
    "ProjectStatus",
    "PropertyFilterSearchTerm",
    "ValidationError",
    "ValidationErrorLocItem",
]
