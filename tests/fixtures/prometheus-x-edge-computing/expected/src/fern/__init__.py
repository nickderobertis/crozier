



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AccessToken,
        ConsentId,
        ContractId,
        DataId,
        DataProviderId,
        ExecutionResult,
        ExecutionResultMetrics,
        Function,
        FunctionId,
        FunctionProviderId,
        PrivacyZoneData,
        PrivacyZoneId,
        PrivateData,
        PrivateExecutionResult,
        PrivateExecutionResultMetrics,
    )
    from .errors import (
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        PreconditionFailedError,
        RequestTimeoutError,
        ServiceUnavailableError,
        UnauthorizedError,
    )
    from . import connector_api, customer_api
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AccessToken": ".types",
    "AsyncFernApi": ".client",
    "ConsentId": ".types",
    "ContractId": ".types",
    "DataId": ".types",
    "DataProviderId": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ExecutionResult": ".types",
    "ExecutionResultMetrics": ".types",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "Function": ".types",
    "FunctionId": ".types",
    "FunctionProviderId": ".types",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "PreconditionFailedError": ".errors",
    "PrivacyZoneData": ".types",
    "PrivacyZoneId": ".types",
    "PrivateData": ".types",
    "PrivateExecutionResult": ".types",
    "PrivateExecutionResultMetrics": ".types",
    "RequestTimeoutError": ".errors",
    "ServiceUnavailableError": ".errors",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "connector_api": ".connector_api",
    "customer_api": ".customer_api",
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
    "AccessToken",
    "AsyncFernApi",
    "ConsentId",
    "ContractId",
    "DataId",
    "DataProviderId",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ExecutionResult",
    "ExecutionResultMetrics",
    "FernApi",
    "ForbiddenError",
    "Function",
    "FunctionId",
    "FunctionProviderId",
    "InternalServerError",
    "NotFoundError",
    "PreconditionFailedError",
    "PrivacyZoneData",
    "PrivacyZoneId",
    "PrivateData",
    "PrivateExecutionResult",
    "PrivateExecutionResultMetrics",
    "RequestTimeoutError",
    "ServiceUnavailableError",
    "UnauthorizedError",
    "__version__",
    "connector_api",
    "customer_api",
]
