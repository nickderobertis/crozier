



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ClockRequestAction,
        DeleteMockserverCassettesResponse,
        GetMockserverBreakpointMatchersResponse,
        GetMockserverBreakpointMatchersResponseMatchersItem,
        GetMockserverCassettesResponse,
        GetMockserverHttp3StatusResponse,
        GetMockserverModeResponse,
        GetMockserverModeResponseMode,
        GetMockserverProxyConfigurationResponse,
        GetMockserverProxyConfigurationResponseEnvironmentVariables,
        GetMockserverReadyResponse,
        GetMockserverReadyResponseStatus,
        PutMockserverBreakpointMatcherClearResponse,
        PutMockserverBreakpointMatcherRemoveResponse,
        PutMockserverBreakpointMatcherRequestPhasesItem,
        PutMockserverBreakpointMatcherResponse,
        PutMockserverBreakpointMatchersResponse,
        PutMockserverCassettesResponse,
        PutMockserverClearRequestBody,
        PutMockserverClearRequestType,
        PutMockserverModeRequestMode,
        PutMockserverModeResponse,
        PutMockserverModeResponseMode,
        PutMockserverRetrieveRequestBody,
        PutMockserverRetrieveRequestFormat,
        PutMockserverRetrieveRequestType,
        PutMockserverRetrieveResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ClockRequestAction": ".types",
    "DeleteMockserverCassettesResponse": ".types",
    "GetMockserverBreakpointMatchersResponse": ".types",
    "GetMockserverBreakpointMatchersResponseMatchersItem": ".types",
    "GetMockserverCassettesResponse": ".types",
    "GetMockserverHttp3StatusResponse": ".types",
    "GetMockserverModeResponse": ".types",
    "GetMockserverModeResponseMode": ".types",
    "GetMockserverProxyConfigurationResponse": ".types",
    "GetMockserverProxyConfigurationResponseEnvironmentVariables": ".types",
    "GetMockserverReadyResponse": ".types",
    "GetMockserverReadyResponseStatus": ".types",
    "PutMockserverBreakpointMatcherClearResponse": ".types",
    "PutMockserverBreakpointMatcherRemoveResponse": ".types",
    "PutMockserverBreakpointMatcherRequestPhasesItem": ".types",
    "PutMockserverBreakpointMatcherResponse": ".types",
    "PutMockserverBreakpointMatchersResponse": ".types",
    "PutMockserverCassettesResponse": ".types",
    "PutMockserverClearRequestBody": ".types",
    "PutMockserverClearRequestType": ".types",
    "PutMockserverModeRequestMode": ".types",
    "PutMockserverModeResponse": ".types",
    "PutMockserverModeResponseMode": ".types",
    "PutMockserverRetrieveRequestBody": ".types",
    "PutMockserverRetrieveRequestFormat": ".types",
    "PutMockserverRetrieveRequestType": ".types",
    "PutMockserverRetrieveResponse": ".types",
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
    "ClockRequestAction",
    "DeleteMockserverCassettesResponse",
    "GetMockserverBreakpointMatchersResponse",
    "GetMockserverBreakpointMatchersResponseMatchersItem",
    "GetMockserverCassettesResponse",
    "GetMockserverHttp3StatusResponse",
    "GetMockserverModeResponse",
    "GetMockserverModeResponseMode",
    "GetMockserverProxyConfigurationResponse",
    "GetMockserverProxyConfigurationResponseEnvironmentVariables",
    "GetMockserverReadyResponse",
    "GetMockserverReadyResponseStatus",
    "PutMockserverBreakpointMatcherClearResponse",
    "PutMockserverBreakpointMatcherRemoveResponse",
    "PutMockserverBreakpointMatcherRequestPhasesItem",
    "PutMockserverBreakpointMatcherResponse",
    "PutMockserverBreakpointMatchersResponse",
    "PutMockserverCassettesResponse",
    "PutMockserverClearRequestBody",
    "PutMockserverClearRequestType",
    "PutMockserverModeRequestMode",
    "PutMockserverModeResponse",
    "PutMockserverModeResponseMode",
    "PutMockserverRetrieveRequestBody",
    "PutMockserverRetrieveRequestFormat",
    "PutMockserverRetrieveRequestType",
    "PutMockserverRetrieveResponse",
]
