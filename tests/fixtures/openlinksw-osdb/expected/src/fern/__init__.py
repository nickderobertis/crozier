



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ActionDescription,
        ActionHelp,
        ActionHelpResponse,
        ActionHelpResponseStatus,
        DescribeActionResponse,
        DescribeActionResponseStatus,
        DescribeServiceResponse,
        DescribeServiceResponseStatus,
        EntryPoint,
        EntryPointHttpMethod,
        EntryPointParameter,
        EntryPointParameterType,
        ErrorModel,
        ErrorModelStatus,
        ListActionsResponse,
        ListActionsResponseStatus,
        ListServicesResponse,
        ListServicesResponseStatus,
        LoginResponse,
        LoginResponseResponse,
        LoginResponseStatus,
        LogoutResponse,
        LogoutResponseResponse,
        LogoutResponseStatus,
        ServiceDescription,
    )
    from . import osdb
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .osdb import (
        ExecBodyOsdbOutputType,
        LoadServiceResponse,
        LoadServiceResponseStatus,
        UnloadServiceResponse,
        UnloadServiceResponseStatus,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ActionDescription": ".types",
    "ActionHelp": ".types",
    "ActionHelpResponse": ".types",
    "ActionHelpResponseStatus": ".types",
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DescribeActionResponse": ".types",
    "DescribeActionResponseStatus": ".types",
    "DescribeServiceResponse": ".types",
    "DescribeServiceResponseStatus": ".types",
    "EntryPoint": ".types",
    "EntryPointHttpMethod": ".types",
    "EntryPointParameter": ".types",
    "EntryPointParameterType": ".types",
    "ErrorModel": ".types",
    "ErrorModelStatus": ".types",
    "ExecBodyOsdbOutputType": ".osdb",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ListActionsResponse": ".types",
    "ListActionsResponseStatus": ".types",
    "ListServicesResponse": ".types",
    "ListServicesResponseStatus": ".types",
    "LoadServiceResponse": ".osdb",
    "LoadServiceResponseStatus": ".osdb",
    "LoginResponse": ".types",
    "LoginResponseResponse": ".types",
    "LoginResponseStatus": ".types",
    "LogoutResponse": ".types",
    "LogoutResponseResponse": ".types",
    "LogoutResponseStatus": ".types",
    "ServiceDescription": ".types",
    "UnloadServiceResponse": ".osdb",
    "UnloadServiceResponseStatus": ".osdb",
    "__version__": ".version",
    "osdb": ".osdb",
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
    "ActionDescription",
    "ActionHelp",
    "ActionHelpResponse",
    "ActionHelpResponseStatus",
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DescribeActionResponse",
    "DescribeActionResponseStatus",
    "DescribeServiceResponse",
    "DescribeServiceResponseStatus",
    "EntryPoint",
    "EntryPointHttpMethod",
    "EntryPointParameter",
    "EntryPointParameterType",
    "ErrorModel",
    "ErrorModelStatus",
    "ExecBodyOsdbOutputType",
    "FernApi",
    "FernApiEnvironment",
    "ListActionsResponse",
    "ListActionsResponseStatus",
    "ListServicesResponse",
    "ListServicesResponseStatus",
    "LoadServiceResponse",
    "LoadServiceResponseStatus",
    "LoginResponse",
    "LoginResponseResponse",
    "LoginResponseStatus",
    "LogoutResponse",
    "LogoutResponseResponse",
    "LogoutResponseStatus",
    "ServiceDescription",
    "UnloadServiceResponse",
    "UnloadServiceResponseStatus",
    "__version__",
    "osdb",
]
