



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import NullableColor, Shade
    from . import simple_encoding
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .simple_encoding import EncodeValueRequestXInlineNullableEnum
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EncodeValueRequestXInlineNullableEnum": ".simple_encoding",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "NullableColor": ".types",
    "Shade": ".types",
    "__version__": ".version",
    "simple_encoding": ".simple_encoding",
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
    "EncodeValueRequestXInlineNullableEnum",
    "FernApi",
    "FernApiEnvironment",
    "NullableColor",
    "Shade",
    "__version__",
    "simple_encoding",
]
