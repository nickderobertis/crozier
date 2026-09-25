



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CostCenterInput,
        ErrorResponse,
        Payable,
        Settlement,
        SettlementsResponse,
        SnapshotResponse,
        SupplierInput,
        TokenResponse,
        WebhookInput,
    )
    from .errors import BadRequestError, UnauthorizedError
    from . import accounting, analytical, authentication, purchase_orders, spend_data, suppliers, users, webhooks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .suppliers import UpdatesupplierstatusRequestStatus
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CostCenterInput": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Payable": ".types",
    "Settlement": ".types",
    "SettlementsResponse": ".types",
    "SnapshotResponse": ".types",
    "SupplierInput": ".types",
    "TokenResponse": ".types",
    "UnauthorizedError": ".errors",
    "UpdatesupplierstatusRequestStatus": ".suppliers",
    "WebhookInput": ".types",
    "__version__": ".version",
    "accounting": ".accounting",
    "analytical": ".analytical",
    "authentication": ".authentication",
    "purchase_orders": ".purchase_orders",
    "spend_data": ".spend_data",
    "suppliers": ".suppliers",
    "users": ".users",
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
    "AsyncFernApi",
    "BadRequestError",
    "CostCenterInput",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "Payable",
    "Settlement",
    "SettlementsResponse",
    "SnapshotResponse",
    "SupplierInput",
    "TokenResponse",
    "UnauthorizedError",
    "UpdatesupplierstatusRequestStatus",
    "WebhookInput",
    "__version__",
    "accounting",
    "analytical",
    "authentication",
    "purchase_orders",
    "spend_data",
    "suppliers",
    "users",
    "webhooks",
]
