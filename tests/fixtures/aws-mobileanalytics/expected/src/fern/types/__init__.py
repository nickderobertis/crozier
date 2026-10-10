



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_exception import BadRequestException
    from .double import Double
    from .event import Event
    from .event_list_definition import EventListDefinition
    from .event_session import EventSession
    from .iso8601timestamp import Iso8601Timestamp
    from .long_ import Long
    from .map_of_string_to_number import MapOfStringToNumber
    from .map_of_string_to_string import MapOfStringToString
    from .put_events_input import PutEventsInput
    from .session import Session
    from .string import String
    from .string0to1000chars import String0To1000Chars
    from .string10chars import String10Chars
    from .string50chars import String50Chars
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestException": ".bad_request_exception",
    "Double": ".double",
    "Event": ".event",
    "EventListDefinition": ".event_list_definition",
    "EventSession": ".event_session",
    "Iso8601Timestamp": ".iso8601timestamp",
    "Long": ".long_",
    "MapOfStringToNumber": ".map_of_string_to_number",
    "MapOfStringToString": ".map_of_string_to_string",
    "PutEventsInput": ".put_events_input",
    "Session": ".session",
    "String": ".string",
    "String0To1000Chars": ".string0to1000chars",
    "String10Chars": ".string10chars",
    "String50Chars": ".string50chars",
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
    "BadRequestException",
    "Double",
    "Event",
    "EventListDefinition",
    "EventSession",
    "Iso8601Timestamp",
    "Long",
    "MapOfStringToNumber",
    "MapOfStringToString",
    "PutEventsInput",
    "Session",
    "String",
    "String0To1000Chars",
    "String10Chars",
    "String50Chars",
]
