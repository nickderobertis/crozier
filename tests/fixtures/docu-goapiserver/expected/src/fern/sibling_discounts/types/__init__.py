



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_sibling_discounts_v3request_active_sibling_filter import GetSiblingDiscountsV3RequestActiveSiblingFilter
    from .get_sibling_discounts_v3request_sibling_filter import GetSiblingDiscountsV3RequestSiblingFilter
    from .get_sibling_discounts_v3request_sort_by import GetSiblingDiscountsV3RequestSortBy
    from .get_sibling_discounts_v3request_status import GetSiblingDiscountsV3RequestStatus
_dynamic_imports: typing.Dict[str, str] = {
    "GetSiblingDiscountsV3RequestActiveSiblingFilter": ".get_sibling_discounts_v3request_active_sibling_filter",
    "GetSiblingDiscountsV3RequestSiblingFilter": ".get_sibling_discounts_v3request_sibling_filter",
    "GetSiblingDiscountsV3RequestSortBy": ".get_sibling_discounts_v3request_sort_by",
    "GetSiblingDiscountsV3RequestStatus": ".get_sibling_discounts_v3request_status",
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
    "GetSiblingDiscountsV3RequestActiveSiblingFilter",
    "GetSiblingDiscountsV3RequestSiblingFilter",
    "GetSiblingDiscountsV3RequestSortBy",
    "GetSiblingDiscountsV3RequestStatus",
]
