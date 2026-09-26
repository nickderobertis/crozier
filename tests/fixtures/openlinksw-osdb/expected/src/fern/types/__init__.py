



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action_description import ActionDescription
    from .action_help import ActionHelp
    from .action_help_response import ActionHelpResponse
    from .action_help_response_status import ActionHelpResponseStatus
    from .describe_action_response import DescribeActionResponse
    from .describe_action_response_status import DescribeActionResponseStatus
    from .describe_service_response import DescribeServiceResponse
    from .describe_service_response_status import DescribeServiceResponseStatus
    from .entry_point import EntryPoint
    from .entry_point_http_method import EntryPointHttpMethod
    from .entry_point_parameter import EntryPointParameter
    from .entry_point_parameter_type import EntryPointParameterType
    from .error_model import ErrorModel
    from .error_model_status import ErrorModelStatus
    from .list_actions_response import ListActionsResponse
    from .list_actions_response_status import ListActionsResponseStatus
    from .list_services_response import ListServicesResponse
    from .list_services_response_status import ListServicesResponseStatus
    from .login_response import LoginResponse
    from .login_response_response import LoginResponseResponse
    from .login_response_status import LoginResponseStatus
    from .logout_response import LogoutResponse
    from .logout_response_response import LogoutResponseResponse
    from .logout_response_status import LogoutResponseStatus
    from .service_description import ServiceDescription
_dynamic_imports: typing.Dict[str, str] = {
    "ActionDescription": ".action_description",
    "ActionHelp": ".action_help",
    "ActionHelpResponse": ".action_help_response",
    "ActionHelpResponseStatus": ".action_help_response_status",
    "DescribeActionResponse": ".describe_action_response",
    "DescribeActionResponseStatus": ".describe_action_response_status",
    "DescribeServiceResponse": ".describe_service_response",
    "DescribeServiceResponseStatus": ".describe_service_response_status",
    "EntryPoint": ".entry_point",
    "EntryPointHttpMethod": ".entry_point_http_method",
    "EntryPointParameter": ".entry_point_parameter",
    "EntryPointParameterType": ".entry_point_parameter_type",
    "ErrorModel": ".error_model",
    "ErrorModelStatus": ".error_model_status",
    "ListActionsResponse": ".list_actions_response",
    "ListActionsResponseStatus": ".list_actions_response_status",
    "ListServicesResponse": ".list_services_response",
    "ListServicesResponseStatus": ".list_services_response_status",
    "LoginResponse": ".login_response",
    "LoginResponseResponse": ".login_response_response",
    "LoginResponseStatus": ".login_response_status",
    "LogoutResponse": ".logout_response",
    "LogoutResponseResponse": ".logout_response_response",
    "LogoutResponseStatus": ".logout_response_status",
    "ServiceDescription": ".service_description",
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
    "ListActionsResponse",
    "ListActionsResponseStatus",
    "ListServicesResponse",
    "ListServicesResponseStatus",
    "LoginResponse",
    "LoginResponseResponse",
    "LoginResponseStatus",
    "LogoutResponse",
    "LogoutResponseResponse",
    "LogoutResponseStatus",
    "ServiceDescription",
]
