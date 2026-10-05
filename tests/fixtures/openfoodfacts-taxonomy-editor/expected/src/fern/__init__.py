



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AncestorFilterSearchTerm,
        ChildFilterSearchTerm,
        DescendantFilterSearchTerm,
        EntryNode,
        EntryNodeSearchResult,
        EntryNodeSearchResultFiltersItem,
        EntryNodeSearchResultFiltersItem_Ancestor,
        EntryNodeSearchResultFiltersItem_Child,
        EntryNodeSearchResultFiltersItem_Descendant,
        EntryNodeSearchResultFiltersItem_Is,
        EntryNodeSearchResultFiltersItem_Language,
        EntryNodeSearchResultFiltersItem_Parent,
        EntryNodeSearchResultFiltersItem_Property,
        ErrorNode,
        HttpValidationError,
        IsFilterSearchTerm,
        IsFilterSearchTermFilterValue,
        IsFilterSearchTermFilterValueFour,
        IsFilterSearchTermFilterValueOne,
        IsFilterSearchTermFilterValueThree,
        IsFilterSearchTermFilterValueTwo,
        IsFilterSearchTermFilterValueZero,
        LanguageFilterSearchTerm,
        ParentFilterSearchTerm,
        Project,
        ProjectStatus,
        PropertyFilterSearchTerm,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import UnprocessableEntityError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AncestorFilterSearchTerm": ".types",
    "AsyncFernApi": ".client",
    "ChildFilterSearchTerm": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DescendantFilterSearchTerm": ".types",
    "EntryNode": ".types",
    "EntryNodeSearchResult": ".types",
    "EntryNodeSearchResultFiltersItem": ".types",
    "EntryNodeSearchResultFiltersItem_Ancestor": ".types",
    "EntryNodeSearchResultFiltersItem_Child": ".types",
    "EntryNodeSearchResultFiltersItem_Descendant": ".types",
    "EntryNodeSearchResultFiltersItem_Is": ".types",
    "EntryNodeSearchResultFiltersItem_Language": ".types",
    "EntryNodeSearchResultFiltersItem_Parent": ".types",
    "EntryNodeSearchResultFiltersItem_Property": ".types",
    "ErrorNode": ".types",
    "FernApi": ".client",
    "HttpValidationError": ".types",
    "IsFilterSearchTerm": ".types",
    "IsFilterSearchTermFilterValue": ".types",
    "IsFilterSearchTermFilterValueFour": ".types",
    "IsFilterSearchTermFilterValueOne": ".types",
    "IsFilterSearchTermFilterValueThree": ".types",
    "IsFilterSearchTermFilterValueTwo": ".types",
    "IsFilterSearchTermFilterValueZero": ".types",
    "LanguageFilterSearchTerm": ".types",
    "ParentFilterSearchTerm": ".types",
    "Project": ".types",
    "ProjectStatus": ".types",
    "PropertyFilterSearchTerm": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "ChildFilterSearchTerm",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
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
    "FernApi",
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
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
]
