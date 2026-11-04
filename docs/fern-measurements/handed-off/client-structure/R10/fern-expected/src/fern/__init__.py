



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PaymentRequestSource,
        PaymentRequestSourceCard,
        PaymentRequestSourceTag,
        PaymentRequestSource_Card,
        PaymentRequestSource_Tag,
    )
    from . import payments
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .payments import PayTollResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "PayTollResponse": ".payments",
    "PaymentRequestSource": ".types",
    "PaymentRequestSourceCard": ".types",
    "PaymentRequestSourceTag": ".types",
    "PaymentRequestSource_Card": ".types",
    "PaymentRequestSource_Tag": ".types",
    "__version__": ".version",
    "payments": ".payments",
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
    "PayTollResponse",
    "PaymentRequestSource",
    "PaymentRequestSourceCard",
    "PaymentRequestSourceTag",
    "PaymentRequestSource_Card",
    "PaymentRequestSource_Tag",
    "__version__",
    "payments",
]
