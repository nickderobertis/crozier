



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .loom_reading import LoomReading
    from .loom_reading_payload import LoomReadingPayload
    from .loom_reading_payload_zero import LoomReadingPayloadZero
    from .loom_reading_shuttle import LoomReadingShuttle
    from .loom_reading_shuttle_pick import LoomReadingShuttlePick
    from .loom_reading_shuttle_pick_zero import LoomReadingShuttlePickZero
    from .loom_reading_tension import LoomReadingTension
    from .loom_reading_tension_zero import LoomReadingTensionZero
_dynamic_imports: typing.Dict[str, str] = {
    "LoomReading": ".loom_reading",
    "LoomReadingPayload": ".loom_reading_payload",
    "LoomReadingPayloadZero": ".loom_reading_payload_zero",
    "LoomReadingShuttle": ".loom_reading_shuttle",
    "LoomReadingShuttlePick": ".loom_reading_shuttle_pick",
    "LoomReadingShuttlePickZero": ".loom_reading_shuttle_pick_zero",
    "LoomReadingTension": ".loom_reading_tension",
    "LoomReadingTensionZero": ".loom_reading_tension_zero",
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
    "LoomReading",
    "LoomReadingPayload",
    "LoomReadingPayloadZero",
    "LoomReadingShuttle",
    "LoomReadingShuttlePick",
    "LoomReadingShuttlePickZero",
    "LoomReadingTension",
    "LoomReadingTensionZero",
]
