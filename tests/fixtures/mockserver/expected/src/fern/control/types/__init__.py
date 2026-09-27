



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .clock_request_action import ClockRequestAction
    from .delete_mockserver_cassettes_response import DeleteMockserverCassettesResponse
    from .get_mockserver_breakpoint_matchers_response import GetMockserverBreakpointMatchersResponse
    from .get_mockserver_breakpoint_matchers_response_matchers_item import (
        GetMockserverBreakpointMatchersResponseMatchersItem,
    )
    from .get_mockserver_cassettes_response import GetMockserverCassettesResponse
    from .get_mockserver_http3status_response import GetMockserverHttp3StatusResponse
    from .get_mockserver_mode_response import GetMockserverModeResponse
    from .get_mockserver_mode_response_mode import GetMockserverModeResponseMode
    from .get_mockserver_proxy_configuration_response import GetMockserverProxyConfigurationResponse
    from .get_mockserver_proxy_configuration_response_environment_variables import (
        GetMockserverProxyConfigurationResponseEnvironmentVariables,
    )
    from .get_mockserver_ready_response import GetMockserverReadyResponse
    from .get_mockserver_ready_response_status import GetMockserverReadyResponseStatus
    from .put_mockserver_breakpoint_matcher_clear_response import PutMockserverBreakpointMatcherClearResponse
    from .put_mockserver_breakpoint_matcher_remove_response import PutMockserverBreakpointMatcherRemoveResponse
    from .put_mockserver_breakpoint_matcher_request_phases_item import PutMockserverBreakpointMatcherRequestPhasesItem
    from .put_mockserver_breakpoint_matcher_response import PutMockserverBreakpointMatcherResponse
    from .put_mockserver_breakpoint_matchers_response import PutMockserverBreakpointMatchersResponse
    from .put_mockserver_cassettes_response import PutMockserverCassettesResponse
    from .put_mockserver_clear_request_body import PutMockserverClearRequestBody
    from .put_mockserver_clear_request_type import PutMockserverClearRequestType
    from .put_mockserver_mode_request_mode import PutMockserverModeRequestMode
    from .put_mockserver_mode_response import PutMockserverModeResponse
    from .put_mockserver_mode_response_mode import PutMockserverModeResponseMode
    from .put_mockserver_retrieve_request_body import PutMockserverRetrieveRequestBody
    from .put_mockserver_retrieve_request_format import PutMockserverRetrieveRequestFormat
    from .put_mockserver_retrieve_request_type import PutMockserverRetrieveRequestType
    from .put_mockserver_retrieve_response import PutMockserverRetrieveResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ClockRequestAction": ".clock_request_action",
    "DeleteMockserverCassettesResponse": ".delete_mockserver_cassettes_response",
    "GetMockserverBreakpointMatchersResponse": ".get_mockserver_breakpoint_matchers_response",
    "GetMockserverBreakpointMatchersResponseMatchersItem": ".get_mockserver_breakpoint_matchers_response_matchers_item",
    "GetMockserverCassettesResponse": ".get_mockserver_cassettes_response",
    "GetMockserverHttp3StatusResponse": ".get_mockserver_http3status_response",
    "GetMockserverModeResponse": ".get_mockserver_mode_response",
    "GetMockserverModeResponseMode": ".get_mockserver_mode_response_mode",
    "GetMockserverProxyConfigurationResponse": ".get_mockserver_proxy_configuration_response",
    "GetMockserverProxyConfigurationResponseEnvironmentVariables": ".get_mockserver_proxy_configuration_response_environment_variables",
    "GetMockserverReadyResponse": ".get_mockserver_ready_response",
    "GetMockserverReadyResponseStatus": ".get_mockserver_ready_response_status",
    "PutMockserverBreakpointMatcherClearResponse": ".put_mockserver_breakpoint_matcher_clear_response",
    "PutMockserverBreakpointMatcherRemoveResponse": ".put_mockserver_breakpoint_matcher_remove_response",
    "PutMockserverBreakpointMatcherRequestPhasesItem": ".put_mockserver_breakpoint_matcher_request_phases_item",
    "PutMockserverBreakpointMatcherResponse": ".put_mockserver_breakpoint_matcher_response",
    "PutMockserverBreakpointMatchersResponse": ".put_mockserver_breakpoint_matchers_response",
    "PutMockserverCassettesResponse": ".put_mockserver_cassettes_response",
    "PutMockserverClearRequestBody": ".put_mockserver_clear_request_body",
    "PutMockserverClearRequestType": ".put_mockserver_clear_request_type",
    "PutMockserverModeRequestMode": ".put_mockserver_mode_request_mode",
    "PutMockserverModeResponse": ".put_mockserver_mode_response",
    "PutMockserverModeResponseMode": ".put_mockserver_mode_response_mode",
    "PutMockserverRetrieveRequestBody": ".put_mockserver_retrieve_request_body",
    "PutMockserverRetrieveRequestFormat": ".put_mockserver_retrieve_request_format",
    "PutMockserverRetrieveRequestType": ".put_mockserver_retrieve_request_type",
    "PutMockserverRetrieveResponse": ".put_mockserver_retrieve_response",
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
