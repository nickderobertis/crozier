



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import CheckHealthRequestDepth, CheckHealthResponse, CheckHealthResponseState
    from . import depots, letters, parcels
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .letters import ListLettersRequestCarrier, ListLettersRequestPriority
    from .parcels import ListParcelsRequestCarrier, ListParcelsRequestPriority
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CheckHealthRequestDepth": ".types",
    "CheckHealthResponse": ".types",
    "CheckHealthResponseState": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "ListLettersRequestCarrier": ".letters",
    "ListLettersRequestPriority": ".letters",
    "ListParcelsRequestCarrier": ".parcels",
    "ListParcelsRequestPriority": ".parcels",
    "__version__": ".version",
    "depots": ".depots",
    "letters": ".letters",
    "parcels": ".parcels",
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
    "CheckHealthRequestDepth",
    "CheckHealthResponse",
    "CheckHealthResponseState",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "ListLettersRequestCarrier",
    "ListLettersRequestPriority",
    "ListParcelsRequestCarrier",
    "ListParcelsRequestPriority",
    "__version__",
    "depots",
    "letters",
    "parcels",
]
