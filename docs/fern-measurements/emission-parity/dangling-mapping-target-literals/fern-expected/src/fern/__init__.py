



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Camera,
        CometReading,
        Instrument,
        Instrument_Camera,
        Instrument_Telescope,
        Logbook,
        MeteorReading,
        MeteorReadingKind,
        Reading,
        Reading_Comet,
        Reading_Meteor,
        Reading_Star,
        StarReading,
        StarReadingKind,
        Telescope,
        Trail,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Camera": ".types",
    "CometReading": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "Instrument": ".types",
    "Instrument_Camera": ".types",
    "Instrument_Telescope": ".types",
    "Logbook": ".types",
    "MeteorReading": ".types",
    "MeteorReadingKind": ".types",
    "Reading": ".types",
    "Reading_Comet": ".types",
    "Reading_Meteor": ".types",
    "Reading_Star": ".types",
    "StarReading": ".types",
    "StarReadingKind": ".types",
    "Telescope": ".types",
    "Trail": ".types",
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
    "AsyncFernApi",
    "Camera",
    "CometReading",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "Instrument",
    "Instrument_Camera",
    "Instrument_Telescope",
    "Logbook",
    "MeteorReading",
    "MeteorReadingKind",
    "Reading",
    "Reading_Comet",
    "Reading_Meteor",
    "Reading_Star",
    "StarReading",
    "StarReadingKind",
    "Telescope",
    "Trail",
    "__version__",
]
