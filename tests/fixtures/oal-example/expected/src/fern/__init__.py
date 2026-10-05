



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415,
        Obj1,
        Obj2,
        Obj3,
        Obj3Stuff,
        Obj3StuffZero,
    )
    from . import blah
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415": ".types",
    "Obj1": ".types",
    "Obj2": ".types",
    "Obj3": ".types",
    "Obj3Stuff": ".types",
    "Obj3StuffZero": ".types",
    "__version__": ".version",
    "blah": ".blah",
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
    "HashD31B2F251C984Df5575331831C174F719158747Bfcbc58788D44Da87Badfa415",
    "Obj1",
    "Obj2",
    "Obj3",
    "Obj3Stuff",
    "Obj3StuffZero",
    "__version__",
    "blah",
]
