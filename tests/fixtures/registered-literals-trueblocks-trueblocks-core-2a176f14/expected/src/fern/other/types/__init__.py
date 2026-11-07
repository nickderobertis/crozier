



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .other_slurp_request_parts_item import OtherSlurpRequestPartsItem
    from .other_slurp_request_source import OtherSlurpRequestSource
    from .other_slurp_response import OtherSlurpResponse
    from .other_slurp_response_data_item import OtherSlurpResponseDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "OtherSlurpRequestPartsItem": ".other_slurp_request_parts_item",
    "OtherSlurpRequestSource": ".other_slurp_request_source",
    "OtherSlurpResponse": ".other_slurp_response",
    "OtherSlurpResponseDataItem": ".other_slurp_response_data_item",
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


__all__ = ["OtherSlurpRequestPartsItem", "OtherSlurpRequestSource", "OtherSlurpResponse", "OtherSlurpResponseDataItem"]
