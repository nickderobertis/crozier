



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ApiKeyOut,
        ApiKeySecretOut,
        ClusterOut,
        DashboardOut,
        DeploymentOut,
        GatewayError,
        GatewayErrorError,
        GpuOut,
        HttpValidationError,
        InstanceOut,
        ManualGpuSelection,
        ModelOut,
        TokenResponse,
        UserOut,
        ValidationError,
        ValidationErrorLocItem,
        WorkerOut,
    )
    from .errors import (
        BadGatewayError,
        BadRequestError,
        ContentTooLargeError,
        ForbiddenError,
        NotFoundError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import (
        auth,
        clusters,
        compatibility,
        dashboard,
        deployments,
        gateway,
        instances,
        keys,
        models,
        users,
        workers,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .instances import (
        DeployRequestEngine,
        DeployRequestGpuSelection,
        DeployRequestGpuSelectionOne,
        DeployRequestProfile,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApiKeyOut": ".types",
    "ApiKeySecretOut": ".types",
    "AsyncFernApi": ".client",
    "BadGatewayError": ".errors",
    "BadRequestError": ".errors",
    "ClusterOut": ".types",
    "ContentTooLargeError": ".errors",
    "DashboardOut": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeployRequestEngine": ".instances",
    "DeployRequestGpuSelection": ".instances",
    "DeployRequestGpuSelectionOne": ".instances",
    "DeployRequestProfile": ".instances",
    "DeploymentOut": ".types",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "GatewayError": ".types",
    "GatewayErrorError": ".types",
    "GpuOut": ".types",
    "HttpValidationError": ".types",
    "InstanceOut": ".types",
    "ManualGpuSelection": ".types",
    "ModelOut": ".types",
    "NotFoundError": ".errors",
    "TokenResponse": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "UserOut": ".types",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "WorkerOut": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "clusters": ".clusters",
    "compatibility": ".compatibility",
    "dashboard": ".dashboard",
    "deployments": ".deployments",
    "gateway": ".gateway",
    "instances": ".instances",
    "keys": ".keys",
    "models": ".models",
    "users": ".users",
    "workers": ".workers",
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
    "AsyncFernApi",
    "BadGatewayError",
    "BadRequestError",
    "ClusterOut",
    "ContentTooLargeError",
    "DashboardOut",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeployRequestEngine",
    "DeployRequestGpuSelection",
    "DeployRequestGpuSelectionOne",
    "DeployRequestProfile",
    "DeploymentOut",
    "FernApi",
    "ForbiddenError",
    "GatewayError",
    "GatewayErrorError",
    "GpuOut",
    "HttpValidationError",
    "InstanceOut",
    "ManualGpuSelection",
    "ModelOut",
    "NotFoundError",
    "TokenResponse",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "UserOut",
    "ValidationError",
    "ValidationErrorLocItem",
    "WorkerOut",
    "__version__",
    "auth",
    "clusters",
    "compatibility",
    "dashboard",
    "deployments",
    "gateway",
    "instances",
    "keys",
    "models",
    "users",
    "workers",
]
