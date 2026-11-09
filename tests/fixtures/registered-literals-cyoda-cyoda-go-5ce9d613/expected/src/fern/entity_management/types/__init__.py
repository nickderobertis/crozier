



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_collection_request_format import CreateCollectionRequestFormat
    from .create_request_format import CreateRequestFormat
    from .update_collection_request_body_item import UpdateCollectionRequestBodyItem
    from .update_collection_request_format import UpdateCollectionRequestFormat
    from .update_single_request_format import UpdateSingleRequestFormat
    from .update_single_with_loopback_request_format import UpdateSingleWithLoopbackRequestFormat
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCollectionRequestFormat": ".create_collection_request_format",
    "CreateRequestFormat": ".create_request_format",
    "UpdateCollectionRequestBodyItem": ".update_collection_request_body_item",
    "UpdateCollectionRequestFormat": ".update_collection_request_format",
    "UpdateSingleRequestFormat": ".update_single_request_format",
    "UpdateSingleWithLoopbackRequestFormat": ".update_single_with_loopback_request_format",
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
    "CreateCollectionRequestFormat",
    "CreateRequestFormat",
    "UpdateCollectionRequestBodyItem",
    "UpdateCollectionRequestFormat",
    "UpdateSingleRequestFormat",
    "UpdateSingleWithLoopbackRequestFormat",
]
