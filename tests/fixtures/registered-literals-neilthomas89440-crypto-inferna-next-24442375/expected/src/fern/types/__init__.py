



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_key_out import ApiKeyOut
    from .api_key_secret_out import ApiKeySecretOut
    from .cluster_out import ClusterOut
    from .dashboard_out import DashboardOut
    from .deployment_out import DeploymentOut
    from .gateway_error import GatewayError
    from .gateway_error_error import GatewayErrorError
    from .gpu_out import GpuOut
    from .http_validation_error import HttpValidationError
    from .instance_out import InstanceOut
    from .manual_gpu_selection import ManualGpuSelection
    from .model_out import ModelOut
    from .token_response import TokenResponse
    from .user_out import UserOut
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .worker_out import WorkerOut
_dynamic_imports: typing.Dict[str, str] = {
    "ApiKeyOut": ".api_key_out",
    "ApiKeySecretOut": ".api_key_secret_out",
    "ClusterOut": ".cluster_out",
    "DashboardOut": ".dashboard_out",
    "DeploymentOut": ".deployment_out",
    "GatewayError": ".gateway_error",
    "GatewayErrorError": ".gateway_error_error",
    "GpuOut": ".gpu_out",
    "HttpValidationError": ".http_validation_error",
    "InstanceOut": ".instance_out",
    "ManualGpuSelection": ".manual_gpu_selection",
    "ModelOut": ".model_out",
    "TokenResponse": ".token_response",
    "UserOut": ".user_out",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "WorkerOut": ".worker_out",
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
    "ApiKeyOut",
    "ApiKeySecretOut",
    "ClusterOut",
    "DashboardOut",
    "DeploymentOut",
    "GatewayError",
    "GatewayErrorError",
    "GpuOut",
    "HttpValidationError",
    "InstanceOut",
    "ManualGpuSelection",
    "ModelOut",
    "TokenResponse",
    "UserOut",
    "ValidationError",
    "ValidationErrorLocItem",
    "WorkerOut",
]
