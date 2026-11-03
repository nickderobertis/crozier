



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import Tree
    from . import arboretum, yew_walk
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .arboretum import PlantTreeRequestZone
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
    from .yew_walk import TrimHedgeRequestFinish, TrimHedgeResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "PlantTreeRequestZone": ".arboretum",
    "Tree": ".types",
    "TrimHedgeRequestFinish": ".yew_walk",
    "TrimHedgeResponse": ".yew_walk",
    "__version__": ".version",
    "arboretum": ".arboretum",
    "yew_walk": ".yew_walk",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "PlantTreeRequestZone",
    "Tree",
    "TrimHedgeRequestFinish",
    "TrimHedgeResponse",
    "__version__",
    "arboretum",
    "yew_walk",
]
