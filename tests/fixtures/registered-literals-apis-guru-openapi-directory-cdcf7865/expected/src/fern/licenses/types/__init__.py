



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .license_list_response_item import LicenseListResponseItem
    from .license_list_response_item_attributes import LicenseListResponseItemAttributes
    from .license_list_response_item_links import LicenseListResponseItemLinks
    from .licenses_read_response import LicensesReadResponse
    from .licenses_read_response_attributes import LicensesReadResponseAttributes
    from .licenses_read_response_links import LicensesReadResponseLinks
_dynamic_imports: typing.Dict[str, str] = {
    "LicenseListResponseItem": ".license_list_response_item",
    "LicenseListResponseItemAttributes": ".license_list_response_item_attributes",
    "LicenseListResponseItemLinks": ".license_list_response_item_links",
    "LicensesReadResponse": ".licenses_read_response",
    "LicensesReadResponseAttributes": ".licenses_read_response_attributes",
    "LicensesReadResponseLinks": ".licenses_read_response_links",
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
    "LicenseListResponseItem",
    "LicenseListResponseItemAttributes",
    "LicenseListResponseItemLinks",
    "LicensesReadResponse",
    "LicensesReadResponseAttributes",
    "LicensesReadResponseLinks",
]
