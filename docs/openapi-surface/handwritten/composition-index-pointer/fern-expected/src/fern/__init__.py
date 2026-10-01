



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Account,
        AccountCategory,
        AccountsWebhook,
        CategorisedAccount,
        Drawing,
        Shape,
        ShapeRadius,
        ShapeSide,
    )
    from .errors import NotFoundError
    from . import accounts, drawings, reports, webhooks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".types",
    "AccountCategory": ".types",
    "AccountsWebhook": ".types",
    "AsyncFernApi": ".client",
    "CategorisedAccount": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Drawing": ".types",
    "FernApi": ".client",
    "NotFoundError": ".errors",
    "Shape": ".types",
    "ShapeRadius": ".types",
    "ShapeSide": ".types",
    "__version__": ".version",
    "accounts": ".accounts",
    "drawings": ".drawings",
    "reports": ".reports",
    "webhooks": ".webhooks",
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
    "Account",
    "AccountCategory",
    "AccountsWebhook",
    "AsyncFernApi",
    "CategorisedAccount",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Drawing",
    "FernApi",
    "NotFoundError",
    "Shape",
    "ShapeRadius",
    "ShapeSide",
    "__version__",
    "accounts",
    "drawings",
    "reports",
    "webhooks",
]
