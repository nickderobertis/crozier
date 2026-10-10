



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import FieldRecord, FieldSummary, Preference, Reading, RegistrationBase, RunSettings
    from . import vault
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FieldRecord": ".types",
    "FieldSummary": ".types",
    "Preference": ".types",
    "Reading": ".types",
    "RegistrationBase": ".types",
    "RunSettings": ".types",
    "__version__": ".version",
    "vault": ".vault",
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
    "FieldRecord",
    "FieldSummary",
    "Preference",
    "Reading",
    "RegistrationBase",
    "RunSettings",
    "__version__",
    "vault",
]
