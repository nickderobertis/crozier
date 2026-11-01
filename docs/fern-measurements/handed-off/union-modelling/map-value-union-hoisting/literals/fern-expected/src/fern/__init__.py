



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Buoy,
        BuoysByStation,
        Depth,
        DepthsByStation,
        SoundingsByStation,
        SoundingsByStationValue,
        StationBoard,
        TideGrid,
        TideGridItemItemValue,
        TideGridItemItemValueTrend,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Buoy": ".types",
    "BuoysByStation": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Depth": ".types",
    "DepthsByStation": ".types",
    "FernApi": ".client",
    "SoundingsByStation": ".types",
    "SoundingsByStationValue": ".types",
    "StationBoard": ".types",
    "TideGrid": ".types",
    "TideGridItemItemValue": ".types",
    "TideGridItemItemValueTrend": ".types",
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
    "Buoy",
    "BuoysByStation",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Depth",
    "DepthsByStation",
    "FernApi",
    "SoundingsByStation",
    "SoundingsByStationValue",
    "StationBoard",
    "TideGrid",
    "TideGridItemItemValue",
    "TideGridItemItemValueTrend",
    "__version__",
]
