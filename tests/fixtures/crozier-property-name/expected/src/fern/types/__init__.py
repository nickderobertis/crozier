



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .practice_closed import PracticeClosed
    from .practice_event import PracticeEvent, PracticeEvent_Closed, PracticeEvent_Opened
    from .practice_intent import PracticeIntent
    from .practice_opened import PracticeOpened
    from .practice_service_metadata import PracticeServiceMetadata
_dynamic_imports: typing.Dict[str, str] = {
    "PracticeClosed": ".practice_closed",
    "PracticeEvent": ".practice_event",
    "PracticeEvent_Closed": ".practice_event",
    "PracticeEvent_Opened": ".practice_event",
    "PracticeIntent": ".practice_intent",
    "PracticeOpened": ".practice_opened",
    "PracticeServiceMetadata": ".practice_service_metadata",
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
    "PracticeClosed",
    "PracticeEvent",
    "PracticeEvent_Closed",
    "PracticeEvent_Opened",
    "PracticeIntent",
    "PracticeOpened",
    "PracticeServiceMetadata",
]
