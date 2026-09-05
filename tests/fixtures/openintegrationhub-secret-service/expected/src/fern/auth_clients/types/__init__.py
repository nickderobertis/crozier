



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_client_response import CreateClientResponse
    from .get_client_by_id_response import GetClientByIdResponse
    from .get_clients_response import GetClientsResponse
    from .start_platform_auth_flow_response import StartPlatformAuthFlowResponse
    from .start_platform_auth_flow_response_data import StartPlatformAuthFlowResponseData
    from .update_client_response import UpdateClientResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateClientResponse": ".create_client_response",
    "GetClientByIdResponse": ".get_client_by_id_response",
    "GetClientsResponse": ".get_clients_response",
    "StartPlatformAuthFlowResponse": ".start_platform_auth_flow_response",
    "StartPlatformAuthFlowResponseData": ".start_platform_auth_flow_response_data",
    "UpdateClientResponse": ".update_client_response",
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
    "CreateClientResponse",
    "GetClientByIdResponse",
    "GetClientsResponse",
    "StartPlatformAuthFlowResponse",
    "StartPlatformAuthFlowResponseData",
    "UpdateClientResponse",
]
