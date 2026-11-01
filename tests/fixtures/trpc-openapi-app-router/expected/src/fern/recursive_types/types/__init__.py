



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .recursive_types_category_response import RecursiveTypesCategoryResponse
    from .recursive_types_category_response_result import RecursiveTypesCategoryResponseResult
    from .recursive_types_linked_list_response import RecursiveTypesLinkedListResponse
    from .recursive_types_linked_list_response_result import RecursiveTypesLinkedListResponseResult
    from .recursive_types_tree_response import RecursiveTypesTreeResponse
    from .recursive_types_tree_response_result import RecursiveTypesTreeResponseResult
_dynamic_imports: typing.Dict[str, str] = {
    "RecursiveTypesCategoryResponse": ".recursive_types_category_response",
    "RecursiveTypesCategoryResponseResult": ".recursive_types_category_response_result",
    "RecursiveTypesLinkedListResponse": ".recursive_types_linked_list_response",
    "RecursiveTypesLinkedListResponseResult": ".recursive_types_linked_list_response_result",
    "RecursiveTypesTreeResponse": ".recursive_types_tree_response",
    "RecursiveTypesTreeResponseResult": ".recursive_types_tree_response_result",
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
    "RecursiveTypesCategoryResponse",
    "RecursiveTypesCategoryResponseResult",
    "RecursiveTypesLinkedListResponse",
    "RecursiveTypesLinkedListResponseResult",
    "RecursiveTypesTreeResponse",
    "RecursiveTypesTreeResponseResult",
]
