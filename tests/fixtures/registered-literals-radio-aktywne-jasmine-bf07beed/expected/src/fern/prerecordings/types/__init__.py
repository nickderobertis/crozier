



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .prerecordings_event_list_request_after import PrerecordingsEventListRequestAfter
    from .prerecordings_event_list_request_before import PrerecordingsEventListRequestBefore
    from .prerecordings_event_list_request_limit import PrerecordingsEventListRequestLimit
    from .prerecordings_event_list_request_offset import PrerecordingsEventListRequestOffset
    from .prerecordings_event_list_request_order import PrerecordingsEventListRequestOrder
_dynamic_imports: typing.Dict[str, str] = {
    "PrerecordingsEventListRequestAfter": ".prerecordings_event_list_request_after",
    "PrerecordingsEventListRequestBefore": ".prerecordings_event_list_request_before",
    "PrerecordingsEventListRequestLimit": ".prerecordings_event_list_request_limit",
    "PrerecordingsEventListRequestOffset": ".prerecordings_event_list_request_offset",
    "PrerecordingsEventListRequestOrder": ".prerecordings_event_list_request_order",
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
    "PrerecordingsEventListRequestAfter",
    "PrerecordingsEventListRequestBefore",
    "PrerecordingsEventListRequestLimit",
    "PrerecordingsEventListRequestOffset",
    "PrerecordingsEventListRequestOrder",
]
